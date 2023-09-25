"""
* 아무것도 안 할 때는 현재 시간 보여주기
* 일할 때 25분 카운트다운하기
* 쉴 때 5분 카운트다운하기
* 몇 번 실시했는지 기록하기
"""


import datetime
import time
import os


DEBUG = False
if DEBUG:
    SLEEP_TIME = 0.01
else:
    SLEEP_TIME = 1


Today = datetime.date.today()
year = Today.year
if Today.month < 10:
    month = f"0{Today.month}"
else:
    month = f"{Today.month}"
if Today.day < 10:
    day = f"0{Today.day}"
else:
    day = f"{Today.day}"
log_file = f"{year}-{month}-{day}.txt"


def get_working_times(file=log_file):
    if not file:
        return 0
    with open(file, 'r') as f:
        i = 0
        for line in f.readlines():
            # print(line, end='')
            i += 1
        return i


def logged(file=log_file, working_times=0):
    now = datetime.datetime.now()
    if now.hour < 10:
        hour = f"0{now.hour}"
    else:
        hour = f"{now.hour}"
    if now.minute < 10:
        min = f"0{now.minute}"
    else:
        min = f"{now.minute}"
    finish_time = f"{hour}:{min}"
    message = f"{working_times}번째 작업 완료. ({finish_time})\n"
    with open(file, "a") as f:
        f.write(message)
    print(f"{message}\n"
          f"위 메시지를 기록하였습니다.")


def timer(minutes=2):
    seconds = 0
    while True:
        if minutes < 10:
            min = f"0{minutes}"
        else:
            min = f"{minutes}"
        if seconds < 10:
            sec = f"0{seconds}"
        else:
            sec = f"{seconds}"

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{min}:{sec}")

        time.sleep(SLEEP_TIME)
        if seconds == 0:
            seconds = 59
            minutes -= 1
        else:
            seconds -= 1

        if minutes == 0 and seconds == 0:
            print("Time out!!!")
            return True


def main():
    menu = """
1. 25분 작업하기
2. 5분 휴식하기
3. 끝내기
    """
    working_times = get_working_times()
    while True:
        print(menu)
        try:
            choice = int(input())
        except ValueError:
            print("다시 입력하세요")
            continue

        if choice == 1:
            working_times += 1
            timer(25)
            logged(working_times=working_times)
        elif choice == 2:
            timer(5)
        elif choice == 3:
            print("빠빠이~~~")
            break
        else:
            print("다시 입력하세요")
            continue


if __name__ == "__main__":
    main()
