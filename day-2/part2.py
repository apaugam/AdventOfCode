#!/usr/bin/python3
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


rules = { "blue": 14, "red": 12, "green": 13}

def game_power(game):
    fewest_cubes = { "blue": 0, "red": 0, "green": 0}
    draw_power_score = 1
    for draw in game.split(";"):
        for cubes in draw.split(','):
            cubes_drawn = re.search('(\d+) (\w+)', cubes).group(1)
            cubes_color = re.search('(\d+) (\w+)', cubes).group(2)
            for _, fewest_cubes_number in fewest_cubes.items():
                if int(cubes_drawn) > fewest_cubes[cubes_color]:
                    fewest_cubes[cubes_color] = int(cubes_drawn)
    for _, fewest_cubes_number in fewest_cubes.items():
        draw_power_score = draw_power_score * fewest_cubes_number
    print(draw_power_score)
    return draw_power_score

with open(os.path.join(__location__)+"/input", "r") as f:
    score = 0
    for line in f:
        game_id = int(re.match('Game (\d+):', line).group(1))
        game = re.sub(r'Game (\d+):','',line).strip()
        score += game_power(game)
    print(score)