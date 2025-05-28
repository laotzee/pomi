# Pomi
Pomi is a script that displays a timer with ASCII art of a tomato using the time the user gives as input.

#How to use
The main.py is run from the terminal and will ask the user for the amount of seconds, minutes, or hours to set the timer. As input, the script takes an integer that can be accompanied by a desired prefixed or, if none is given, defaults to seconds. Additionally, "p" or "b" can be used as input as well, standing for "Pomodoro" and "break" respectively setting the timer to the accustomed 25 minutes of work and 5 minutes of break. Such convention can be changed to the long version of a Pomodoro, 50 minutes of work and 10 minutes of rest, by changing the constant CURRENT_P to LONG_P or SHORT_P already defined at the beginning of the script. The following table illustrates the possible input for the script.

| Example | Result |
|----------|----------|
| 10 | 00:00:10 |
| 10s | 00:00:10 |
| 10m | 00:10:00 |
| 10h | 10:00:00 |
| p | 00:25:00 or 00:50:00|
| b | 00:05:00 or 00:10:00|

