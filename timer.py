import sys
import time
from simple_timer import Timer



minutes = (float(input("Minutes: "))*60)
break_minutes = (float(input("Break: "))*60)
seconds = minutes/60
timer = Timer()
while timer.duration < minutes:
    sys.stdout.write("\r")
    sys.stdout.write(time.strftime('Timer: %M:%S', time.gmtime(minutes - timer.duration)))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\n")

break_timer = Timer()
while break_timer.duration < break_minutes:
    sys.stdout.write("\r")
    sys.stdout.write(time.strftime('Break Timer:%M:%S', time.gmtime(minutes - break_timer.duration)))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\n")

sys.stdout.write("\rComplete!            \n")