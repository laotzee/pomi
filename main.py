import time as t

# string -> int
def get_seconds(time): 
    """Manages user string to get total amount of seconds"""
    if time.isdigit():
        return int(time)
    else:
        time = time.lower()
        if time[-1] == 's': #seconds
            return int(time[:-1])
        elif time[-1] == 'm': #minutes
            return 60*(int(time[:-1]))
        elif time[-1] == 'h': #hours
            return 3600*(int(time[:-1]))
        elif time == 'p': # P stands for pomodoro (50 minutes)
            return 3000
        elif time == 'b': # B stands for break (10 minutes)
            return 600
        else:
            print('No proper input given, please try again\n')
            exit()

assert get_seconds('1h') == 3600
assert get_seconds('3m') == 180
assert get_seconds('60s') == 60
assert get_seconds('5') == 5

# int -> string
def format_time(hours, minutes, seconds):
    """Formats time to be properly displayed"""

    timer = f'{hours:02}:{minutes:02}:{seconds:02}'
    return timer

assert format_time(0,0,20) == f'00:00:20'
assert format_time(30,5,20) == f'30:05:20'

# string -> None
def show_time(timer):
    """Takes formatted time to display it to the screen and adds a second of
    delay"""

    print(timer, end='\r')
    t.sleep(1)

# int, string -> int
def update_val(time, suffix='s'):
    """time is int, and suffix is either 's', 'm' or 'h'.
    It will calculate the amount of time in terms of the giving suffix"""
    
    suffix = suffix.lower()
    if suffix == 's':
        return time%60
    elif suffix == 'm':
        return (time//60) % 60
    else: 
        return time//3600

assert update_val(70, 's') == 10
assert update_val(360, 'm') == 6
assert update_val(3789, 'h') == 1
assert update_val(325) == 25


raw_time = input('Enter the time along with a suffix (h/m/s):\n')
time = get_seconds(raw_time)
message = "Time's up"

while time != 0:
    seconds = update_val(time)
    minutes = update_val(time, 'm')
    hours = update_val(time, 'h')
    timer = format_time(hours, minutes, seconds)
    show_time(timer)
    time -= 1

print(message)
