#!/usr/bin/python3
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__)+"/input", "r") as f:
    score = 0
    grid = f.read().splitlines()
    for line in grid:
        line = line[10:]
        # print(re.findall(r'\d+', line.split('|')[0]))
        winning_nb = re.findall(r'\d+', line.split('|')[0])
        drawn_nb = re.findall(r'\d+', line.split('|')[1])
        won = set(winning_nb) & set(drawn_nb)
        if len(won) > 0:
            # print(len(won), won, pow(2, (len(won)-1)) )
            score += 2 ** (len(won)-1)
    print(score)
