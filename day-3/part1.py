#!/usr/bin/python3
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__)+"/input", "r") as f:
    grid = f.read().splitlines()
    position = set() # position of the first matching digit
    for row_id, row in enumerate(grid):
        for char_id, char in enumerate(row):
            if char.isdigit() or char == '.':
                continue
            for current_row in [row_id - 1, row_id, row_id + 1]:
                for current_col in [ char_id - 1, char_id, char_id + 1 ]:
                    if ( current_row < 0
                        or current_row >= len(grid)
                        or current_col < 0
                        or current_col >= len(grid[current_row])
                        or not grid[current_row][current_col].isdigit()):
                        continue
                    while current_col > 0 and grid[current_row][current_col - 1].isdigit():
                        current_col -= 1
                    position.add((current_row, current_col))

    number_table = []
    for row, col in position:
        current_number = ''
        while (col < len(grid[row])
               and grid[row][col].isdigit()):
            current_number += grid[row][col]
            col += 1 # go to the right take the next digit
        number_table.append(int(current_number))
    print(number_table)
    print(sum(number_table))