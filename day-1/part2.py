#!/usr/bin/python3
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

number_words = (
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)
digits = (
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
)

words_to_digits = dict(zip(number_words, digits))
regex_pattern = r"(?=(" + "|".join(number_words + digits) + "))"
total = 0
with open(os.path.join(__location__)+"/input", "r") as f:
    for line in f:
        found = []
        matches = re.findall(regex_pattern, line)
        for match in matches:
            found.append(
                words_to_digits.get(match) if match in words_to_digits.keys() else match
            )
        total = total + int(found[0] + found[-1])
    print(total)