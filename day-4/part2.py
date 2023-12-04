#!/usr/bin/python3
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__)+"/input", "r") as f:
    score = 0
    grid = f.read().strip().split("\n")
    cards = []

    for line_id, line in enumerate(grid):
        line = line[10:]
        winning_nb = set(re.findall(r'\d+', line.split('|')[0]))
        drawn_nb = set(re.findall(r'\d+', line.split('|')[1]))
        cards.append([1, winning_nb, drawn_nb])

    for i, card in enumerate(cards):
        count, win, drawn = card
        won = len(win & drawn)
        if won == 0:
            continue

        for j in range(i+1, i+1+won):
            cards[j][0] += count

    for card in cards:
        score += card[0]
    print(score)