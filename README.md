# Rush Hour Game in Python

This repository contains an object-oriented Python implementation of the Rush Hour game.

## Overview
- Goal: Move a car (usually red) out of a traffic jam through the exit.
- Board: 7x7 grid with exit at coordinate (3,7).
- Cars move according to orientation: horizontal cars move left/right, vertical cars move up/down.
- User inputs car name and direction. Invalid input triggers an error message.

## Project Structure
- `car.py` - Class representing a car with attributes and movement functions.
- `board.py` - Class representing the game board and checking moves.
- `game.py` - Main game loop, handling user input and printing the board.
- `helper.py` - Helper functions, including `load_json` to read board configuration from a JSON file.
- `car_config.json` - Example JSON configuration for initial board setup.

## How to Run
```bash
python3 game.py path_to_json/car_config.json
