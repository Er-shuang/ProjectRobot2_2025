# Author: Yujin Nie
# Date: 22/9/25
# Description: Create the robot_move.py to let the Robot move in multiple directions.

from microbit import display, Image, sleep
import tinybit


while True:
    tinybit.car_run(150)  # moving forward at a speed of 150
    display.show(Image.ARROW_S)  # The arrow pointing forward
    sleep(1000)
    tinybit.car_back(150)  # moving backward
    display.show(Image.ARROW_N)  # The arrow pointing backward
    sleep(1000)
    tinybit.car_left(150)  # moving left
    display.show(Image.ARROW_E)  # left arrow
    sleep(1000)
    tinybit.car_right(150)  # right move
    display.show(Image.ARROW_W)  # right arror
    sleep(1000)
    tinybit.car_spinleft(150)  # car rotates to the left
    display.show(Image.ARROW_E)
    sleep(1000)
    tinybit.car_spinright(150)  # car rotates to the right
    display.show(Image.ARROW_W)
    sleep(1000)
    tinybit.car_stop()  # car stop move
    display.clear()
    sleep(1000)
