#!/usr/bin/python3
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__)+"/input", "r") as f:
    res = []
    number_table = []
    total = 0
    for line in f:
        res.append(''.join(re.findall(r'\d+', line)))

    [ number_table.append(number[0]+number[-1]) for number in res ]

    for number in number_table:
        total += int(number)
    print(total)
