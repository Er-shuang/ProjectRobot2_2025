# Author: Yujin Nie
# Date: 22/9/25
# Description: Create the speed_control.py to let the Robot move with user-define speeds

from microbit import display, Image, sleep
import tinybit

display.show(Image.HAPPY)


while True:
    # The motor on the left runs at a speed of 0, the right runs at a speed of 50
    tinybit.car_run(0, 50)
    sleep(1000)
    # The motor on the left runs at a speed of 50, the right runs at a speed of 0
    tinybit.car_run(50, 0)
    sleep(1000)
    # The motor on the left runs at a speed of 100, the right runs at a speed of 100
    tinybit.car_run(100, 100)
    sleep(1000)
