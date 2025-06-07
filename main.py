from time import sleep
from typing import Optional
import os

LONG_P: tuple = ("10m", "50m")
SHORT_P: tuple = ("5m", "25m")
CURRENT_P: tuple = SHORT_P

BAR_REVERSE = False

FINAL_MESSAGE: str = "Time's up"

ZERO = "▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
TEN = "██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
TWENTY = "████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
THIRTY = "██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒"
FORTY = "████████▒▒▒▒▒▒▒▒▒▒▒▒"
FIFTY = "██████████▒▒▒▒▒▒▒▒▒▒"
SIXTY = "████████████▒▒▒▒▒▒▒▒"
SEVENTY = "██████████████▒▒▒▒▒▒"
EIGHTY = "████████████████▒▒▒▒"
NINETY = "██████████████████▒▒"
HUNDRED = "████████████████████"
bar = [ZERO, TEN, TWENTY, THIRTY, FORTY, FIFTY, SIXTY, SEVENTY, EIGHTY, NINETY,
    HUNDRED]

if BAR_REVERSE:
    bar.reverse()
    bar.append(ZERO)
else:
    bar.append(HUNDRED)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def get_percentage(total_time: int, current_time: int) -> int:
    """Calculates the total progress of the timer in percentage and returns
    only the first number"""

    percentage = str((100 * current_time) // total_time)
    if len(percentage) == 3:
        return int(percentage[:2])
    else:
        return int(percentage[:1])

assert get_percentage(100, 100) == 10
assert get_percentage(100, 50) == 5
assert get_percentage(100, 25) == 2
assert get_percentage(100, 99) == 9

def get_seconds(user_input: str) -> Optional[int]:
    """Manages user input to get total amount of seconds"""
    if user_input.isdigit():
        return int(user_input)
    else:
        user_input = user_input.lower()

        if user_input[-1] == 's': #seconds
            return int(user_input[:-1])
        elif user_input[-1] == 'm': #minutes
            return 60*(int(user_input[:-1]))
        elif user_input[-1] == 'h': #hours
            return 3600*(int(user_input[:-1]))

        elif user_input == 'p': # P stands for pomodoro
            return get_seconds(CURRENT_P[1])
        elif user_input == 'b': # B stands for break
            return get_seconds(CURRENT_P[0])

        else:
            print('No proper input given, please try again\n')
            exit()

assert get_seconds('1h') == 3600
assert get_seconds('3m') == 180
assert get_seconds('60s') == 60
assert get_seconds('5') == 5

def format_time(h: int, m: int, s: int, bar: str) -> str:
    """Formats time to be properly displayed"""

    t = f'{h:02}:{m:02}:{s:02}'
    tomato = f"""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣄⠉⢹⣿⣀⣿⠉⣭⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⣁⣤⡆⠉⢛⡉⠀⢠⣉⣙⣻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⠉⠛⠛⠛⠛⠋⣽⣇⣴⡿⠻⢶⣬⣿⣍⠉⠁⠀⠈⠻⣿⣿⣿⣿
⣿⣿⣿⡿⠁⢀⣴⣾⠟⠛⠀⢠⡿⠟⠁⠀⠀⠀⠈⠉⠛⠃⠀⠀⠀⠀⠹⣿⣿⣿
⣿⣿⣿⠁⢠⣿⠏⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿
⣿⣿⡇⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
⣿⣿⡇⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
⣿⣿⡇⠀⠁⠀⠀⠀⠀   {t}⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿
⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿
⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

     {bar}"""


    return tomato

def show_time(s: int, m: int, h: int, bar: tuple) -> None:
    """Takes formatted time to display it to the screen and adds a second of
    delay"""

    for i in range(2):
        formatted_timer = format_time(h, m, s, bar[i])
        clear_screen()
        print(formatted_timer, end="\r")
        sleep(0.5)

def update_val(t: int, suffix: str) -> int:
    """It will calculate the amount of time in terms of the giving suffix"""
    suffix = suffix.lower()
    if suffix == 's':
        return t%60
    elif suffix == 'm':
        return (t//60) % 60
    else:
        return t//3600

assert update_val(70, 's') == 10
assert update_val(360, 'm') == 6
assert update_val(3789, 'h') == 1

raw_time = input('Enter the time along with a suffix (h/m/s):\n')
timer_seconds = get_seconds(raw_time)
total_time = timer_seconds

while timer_seconds >= 0:
    seconds = update_val(timer_seconds, 's')
    minutes = update_val(timer_seconds, 'm')
    hours = update_val(timer_seconds, 'h')

    percentage = get_percentage(total_time, timer_seconds)
    current_bars = (bar[percentage], bar[percentage + 1])

    show_time(seconds, minutes, hours, current_bars)
    timer_seconds -= 1

print(FINAL_MESSAGE)
