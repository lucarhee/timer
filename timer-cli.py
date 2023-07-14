#! /usr/bin/env python3

import os
import time
import datetime

"""
0  1  2
3     4
5  6  7
8     9
10 11 12
"""


ONE = (0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)
TWO = (1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1)
THREE = (1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1)
FOUR = (1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1)
FIVE = (1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1)
SIX = (1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1)
SEVEN = (1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1)
EIGHT = (1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1)
NINE = (1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1)
ZERO = (1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1)

NUMBERS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

filled_cell = f"{chr(0x2588) * 2}"
empty_cell = f"  "

 

# 40분 집중하고
# 20분 휴식한다.
working_time = int(input("몇 분 집중: "))
resting_time = 60 - working_time

left_time = working_time - 1
sixty_seconds = 59
current_time = datetime.datetime.now()
current_time += datetime.timedelta(minutes=40)

while left_time:
    os.system('clear')

    if 0 < left_time < 10:
        minutes = f"0{left_time}"
    else:
        minutes = f"{left_time}"

    if 0 <= sixty_seconds < 10:
        seconds = f"0{sixty_seconds}"
    else:
        seconds = f"{sixty_seconds}"

    if sixty_seconds == 0:
        left_time -= 1
        sixty_seconds = 59

    print(f"{current_time.hour}시 {current_time.minute}분까지 집중합시다.")
    print(f"남은 시간: {minutes}:{seconds}")

    sixty_seconds -= 1
    time.sleep(1)

current_time = datetime.datetime.now()
current_time += datetime.timedelta(minutes=20)

print(f"{current_time.hour}시 {current_time.minute}분까지 20분 휴식합시다.")

left_time = 19
while left_time:
    os.system('clear')

    if 0 < left_time < 10:
        minutes = f"0{left_time}"
    else:
        minutes = f"{left_time}"

    if 0 <= sixty_seconds < 10:
        seconds = f"0{sixty_seconds}"
    else:
        seconds = f"{sixty_seconds}"

    if sixty_seconds == 0:
        left_time -= 1
        sixty_seconds = 59

    print(f"{current_time.hour}시 {current_time.minute}분까지 집중합시다.")
    print(f"남은 시간: {minutes}:{seconds}")

    sixty_seconds -= 1
    time.sleep(1)
