# Tic Tac Toe with Recursive Depth Levels

## Introduction:
Welcome to the recursive Tic Tac Toe project! This program extends the classic game Tic Tac Toe by introducing arbitrary levels of recursion, adding depth and complexity for those who wish for something bigger than Super Tick Tac Toe. This README provides an overview of how the game works, its features, and discussion into both the front end and back end implementation.

## Features:

    Arbitrary Recursion Levels: Choose the depth of recursion for a more challenging game. Higher depths lead to more complex gameplay (And Lag!).
    Dynamic Board Rendering: The game dynamically renders the game boards and adjusts based on player moves like super Tic Tac Toe, making it intuitive and interactive.
    Win Detection: The game accurately detects wins at various recursion levels, ensuring a fair and challenging gameplay experience.
    UI Customization: Customize UI settings such as window size, colors for X, O, and tie symbols, enabling a personalized gaming experience.
    This program allows for the random generation of moves leading to quick examples, this si hsown in the current code and can be striked out.

## Gameplay Overview:
The game follows the standard rules of Tic Tac Toe, where players aim to align three symbols (X or O) in a row, column, or diagonal. However, with recursive depth levels, the game expands into nested boards, where winning a smaller board influences the larger board.

## Back End Implementation:
The back end of the game is structured using Python classes, facilitating efficient board management and win detection. Key components include:

    Piece Class: Represents X, O, or an empty cell on the board.
    GameBoard Class: Represents a Tic Tac Toe board, capable of recursive nesting for arbitrary depth levels.
    TicTacToe Class: Handles game logic, including moves, win detection, and board resolution.

## Front End Implementation:
The front end of the game is built using Tkinter, providing a graphical interface for players to interact with. Features include:

    Dynamic Rendering: The game renders boards dynamically, adjusting to player moves and recursion levels.
    Interactive Clicking: Players can make moves by clicking on the desired position, triggering updates on the game board.
    Visual Customization: UI settings allow customization of window size, colors, and symbol rendering, enhancing the visual appeal.

## Conclusion:
This recursive Tic Tac Toe project offers an engaging and challenging gaming experience, extending the classic game with depth and complexity. With customizable UI settings and intuitive gameplay mechanics, it provides a platform for players to enjoy strategic gameplay across various recursion levels.

Contributions and Feedback:
Feel free to explore the code and contribute to the project.
