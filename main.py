from time import sleep
import os

LONG_P = ("10m", "50m")

SHORT_P = ("5m", "25m")

CURRENT_P = SHORT_P

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# string -> int
def get_seconds(user_input):
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

# int -> string
def format_time(h, m, s):
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
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"""

    return tomato

# string -> None
def show_time(t):
    """Takes formatted time to display it to the screen and adds a second of
    delay"""
    clear_screen()
    print(t, end='\r')
    sleep(1)

# int, string -> int
def update_val(t, suffix='s'):
    """time is int, and suffix is either 's', 'm' or 'h'.
    It will calculate the amount of time in terms of the giving suffix"""
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
assert update_val(325) == 25


raw_time = input('Enter the time along with a suffix (h/m/s):\n')
timer_seconds = get_seconds(raw_time)
message = "Time's up"

while timer_seconds >= 0:
    seconds = update_val(timer_seconds)
    minutes = update_val(timer_seconds, 'm')
    hours = update_val(timer_seconds, 'h')
    timer = format_time(hours, minutes, seconds)
    show_time(timer)
    timer_seconds -= 1

print(message)
