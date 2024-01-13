#import beepy
import time

def display_count_down(total_seconds):
    for x in range(total_seconds, 0, -1):
        seconds = x % 60
        minutes = (x // 60) % 60
        hours = (x //3600)
        print(f"{hours}:{minutes:02}:{seconds:02}", end="\r")
        time.sleep(1)

def time_transformation(desired_time):
    if desired_time[-1] == "m":
        total_seconds = int(desired_time[:-1])*60
    elif desired_time[-1] == "h":
        total_seconds = int(desired_time[:-1])*3600
    elif desired_time[-1] == "s":
        total_seconds = int(desired_time[:-1])
    elif desired_time.lower() == "p": #p stands for pomodoro technique (25m)
        total_seconds  = 1500
    elif desired_time.lower() == "b": #b stands for break (5m)
        total_seconds  = 300
    else:
        try:
            total_seconds = int(desired_time)
        except:
            print("Invalid Input")
            exit()
    return total_seconds

desired_time = input("Introduce time using prefixes (s/m/h)\n")
total_seconds = time_transformation(desired_time)
display_count_down(total_seconds)
print("Time's up")
#beepy.beep(sound=3) #takes values 1 to 7
