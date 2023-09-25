#! /usr/bin/env python3


"""
* ncurses를 사용한다.
* 현재 시간을 보여준다.
* 1초마다 다시 그린다.
* 일하는 시간은 `-w`, `--work`로 받아오고 기본은 25분이다.
* 쉬는 시간은 `-r`, `--rest`로 받아오고 기본은 5분이다.
* 시작은 스페이스바로 하고 알람 종료도 스페이스바로 한다.
"""

import datetime
import time
import curses


ZERO = ["██████", "██  ██", "██  ██", "██  ██", "██████"]
ONE = ["  ████", "    ██", "    ██", "    ██", "    ██"]
TWO = ["██████", "    ██", "██████", "██    ", "██████"]
THREE = ["██████", "    ██", " █████", "    ██", "██████"]
FOUR = ["██  ██", "██  ██", "██████", "    ██", "    ██"]
FIVE = ["██████", "██    ", "██████", "    ██", "██████"]
SIX = ["██████", "██    ", "██████", "██  ██", "██████"]
SEVEN = ["██████", "    ██", "    ██", "    ██", "    ██"]
EIGHT = ["██████", "██  ██", "██████", "██  ██", "██████"]
NINE = ["██████", "██  ██", "██████", "    ██", "██████"]

DIGITS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]

WORK_MINUTES = 24
REST_MINUTES = 4


def show_current_time():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    if 0 <= hour <= 9:
        hour = f"0{hour}"

    if 0 <= minute <= 9:
        minute = f"0{minute}"

    if 0 <= second <= 9:
        second = f"0{second}"

    return f"{hour}:{minute}:{second}"


def countdown(stdscr):
    stdscr.clear()

    is_work = True
    left_time = WORK_MINUTES
    seconds = 59

    width, height = stdscr.getmaxyx()
    y = width // 2
    x = height // 2 - 17

    while True:
        input_key = ''
        #
        # input_key = stdscr.getch()
        # if input_key == 'q':
        #     stdscr.addstr(y+8, x+17, "빠빠이")
        #     break

        if seconds == 0:
            left_time -= 1
            seconds = 59

        if left_time == 0 and is_work:
            is_work = False
            left_time = REST_MINUTES
            stdscr.addstr(y+8, x+17, "쉬고 싶으면 스페이스바: ")
            input_key = stdscr.getch()
            if input_key == ' ':
                continue
            else:
                break
            # TODO 계속할지 안할지
            # TODO 스페이스 누르면 시작
        elif left_time == 0 and not is_work:
            is_work = True
            left_time = WORK_MINUTES
            # TODO 계속할지 안할지
            # TODO 스페이스 누르면 시작

        # TODO same codes must be eliminated!
        # TODO print big digits
        if is_work:
            if 0 <= left_time <= 9:
                minute_zero = '0'
            else:
                minute_zero = ''
            if 0 <= seconds <= 9:
                second_zero = '0'
            else:
                second_zero = ''
            current_time = f"{minute_zero}{left_time}{second_zero}{seconds}"

            for i in range(5):
                now = ''
                is_dot = 0
                for n in current_time:
                    now += DIGITS[int(n)][i] + ' '
                    is_dot += 1
                    if i in (1, 3) and is_dot == 2 and seconds % 2 == 0:
                        now += '██ '
                    else:
                        now += '   '

                stdscr.addstr(y + i, x, now)
        else:
            if 0 <= left_time <= 9:
                minute_zero = '0'
            else:
                minute_zero = ''
            if 0 <= seconds <= 9:
                second_zero = '0'
            else:
                second_zero = ''
            # stdscr.addstr(x, y, f"{minute_zero}{left_time} : {second_zero}{seconds}", curses.A_REVERSE)
            current_time = f"{minute_zero}{left_time}{second_zero}{seconds}"
            for i in range(5):
                now = ''
                is_dot = 0
                for n in current_time:
                    now += DIGITS[int(n)][i] + ' '
                    is_dot += 1
                    if i in (1, 3) and is_dot == 2:
                        now += '██ '
                    else:
                        now += '   '
                stdscr.addstr(y + i, x, now)

        if is_work:
            stdscr.addstr(y - 3, x + 12, "Working")
        else:
            stdscr.addstr(y - 3, x + 12, "Take a Rest")

        stdscr.addstr(y + 7, x + 8, "현재 시간: " + show_current_time())

        seconds -= 1
        stdscr.refresh()
        time.sleep(1)


def main(stdscr):
    curses.curs_set(0)
    countdown(stdscr=stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
