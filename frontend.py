from backend import *
from tkinter import *
from PIL import Image, ImageTk
import random


windowsize = 729
depth = int(input("Enter game depth: "))
drawtiesymbols = True
drawtieshading = True
drawtopboard = True
XCOLOR = "red"
OCOLOR = "blue"
TIECOLOR = "medium sea green"
TIESHADING = "black"
gameboard = TicTacToe(depth)


cordtopos = gameboard.conversions

win = Tk()

win.geometry(str(windowsize) + "x" + str(windowsize))

canvas = Canvas(win, width=windowsize, height=windowsize)

canvas.configure(bg="white")

canvas.pack()

win.resizable(width=0, height=0)

win.winfo_toplevel().title("TicTacToe (Depth = "+str(depth)+")")

images = []


def create_rectangle(x, y, a, b, **options):

    if "alpha" in options:

        # Calculate the alpha transparency for every color(RGB)

        alpha = int(options.pop("alpha") * 255)

        # Use the fill variable to fill the shape with transparent color

        fill = options.pop("fill")

        fill = win.winfo_rgb(fill) + (alpha,)

        image = Image.new("RGBA", (a - x, b - y), fill)

        images.append(ImageTk.PhotoImage(image))

        canvas.create_image(x, y, image=images[-1], anchor="nw")

        canvas.create_rectangle(x, y, a, b, **options)


def drawx(x, y, size, w):

    canvas.create_line(x, y, x + size, y + size, fill=XCOLOR, width=w)

    canvas.create_line(x + size, y, x, y + size, fill=XCOLOR, width=w)


def drawo(x, y, size, w):

    canvas.create_oval(x, y, x + size, y + size, outline=OCOLOR, width=w)


def drawtie(x, y, size, w):
    canvas.create_rectangle(
        x, y, x + size, y + size, outline=TIECOLOR, width=w
    )


def drawboard(
    game, x, y, size
):  # game parameter is used to pass in the tic tac toe object to retrieve x and o values
    w = game.depth*2+1
    if game.depth != 0:
        dif = size / 3
        

        canvas.create_line(x + dif, y, x + dif, y + size, fill="black", width=w)

        canvas.create_line(x + 2 * dif, y, x + 2 * dif, y + size, fill="black", width=w)

        canvas.create_line(x, y + dif, x + size, y + dif, fill="black", width=w)

        canvas.create_line(x, y + 2 * dif, x + size, y + 2 * dif, fill="black", width=w)

        for i in range(3):

            for j in range(3):

                drawboard(game.board[j + 3 * i], x + j * dif, y + i * dif, dif)

    if game.state != 0 and game.depth != 0 and ((game.state != 2) or drawtieshading):

        if game.state == 1:

            color = XCOLOR

        elif game.state == -1:

            color = OCOLOR

        elif game.isresolved == True:

            color = TIESHADING

        if game.depth != gameboard.game.depth:

            # canvas.create_rectangle(round(x+1), round(y+1), round(x+size-1), round(y+size-1), fill="white", width = 0)

            create_rectangle(
                round(x),
                round(y),
                round(x + size),
                round(y + size),
                fill=color,
                width=0,
                alpha=0.2 - game.depth / 100,
            )

    if game.depth != gameboard.game.depth or drawtopboard:
        symbolwidth = w*2
        if game.state == 1:

            drawx(x + size * 0.1, y + size * 0.1, size * 0.8, symbolwidth)

        elif game.state == -1:

            drawo(x + size * 0.1, y + size * 0.1, size * 0.8, symbolwidth)

        elif game.state == 2 and drawtiesymbols:

            drawtie(x + size * 0.1, y + size * 0.1, size * 0.8, symbolwidth)

    if (
        game.depth != 0
        and game.ismovezone == True
        and not gameboard.game.isresolved
    ):

        create_rectangle(
            round(x),
            round(y),
            round(x + size),
            round(y + size),
            fill="black",
            width=0,
            alpha=0.2,
        )


drawboard(gameboard.game, 0, 0, windowsize)

canvas.focus_set()


def boardclicked(event):

    x, y = event.x, event.y

    pixels = windowsize / (3**gameboard.depth)

    x, y = x // pixels, y // pixels
    gameboard.move(*cordtopos[int(x + y * (3**gameboard.depth))])

    canvas.delete("all")
    drawboard(gameboard.game, 0, 0, windowsize)


canvas.bind("<Button-1>", boardclicked)


def  randomlymove():

    for i in range(10000):
        pos = gameboard.movezone

        while len(pos) < gameboard.depth:

            pos = pos + (int(random.randint(0, 8)),)
        gameboard.move(*pos)

    canvas.delete("all")
    drawboard(gameboard.game, 0, 0, windowsize)
    if gameboard.game.state != 0:

        return

    win.after(1000, randomlymove)


win.after(500, randomlymove)
win.mainloop()
