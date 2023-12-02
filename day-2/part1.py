#!/usr/bin/python3
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


rules = { "blue": 14, "red": 12, "green": 13}

def is_game_possible(game):
    for draw in game.split(";"):
        for cubes in draw.split(','):
            cubes_drawn = re.search('(\d+) (\w+)', cubes).group(1)
            cubes_color = re.search('(\d+) (\w+)', cubes).group(2)
            for rule_cube_color, rule_max_cube in rules.items():
                if int(cubes_drawn) > rules[cubes_color]:
                    return False
    return True

with open(os.path.join(__location__)+"/input", "r") as f:
    score = 0
    for line in f:
        game_id = int(re.match('Game (\d+):', line).group(1))
        game = re.sub(r'Game (\d+):','',line).strip()
        if is_game_possible(game):
            print('Game possible id:' + str(game_id))
            score += game_id
        else:
            print('Game impossible id:' + str(game_id))
    
    print(score)