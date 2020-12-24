#!/usr/bin/python3

import os
import sys

try:
    date = sys.argv[1]
    time = sys.argv[2]
except IndexError:
    print("You must past date (format: mm/dd/yy) and time (hh:mm:ss) on that order.")
else:
    dateArray = date.split('/')
    timeArray = time.split(':')
    instructions = f"""
    sudo date -s {dateArray[0]}/{dateArray[1]}/{dateArray[2]};
    sudo date -s {timeArray[0]}:{timeArray[1]}:{timeArray[2]};
    """
    os.system(instructions)
