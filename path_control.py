# Author: Yujin Nie
# Date: 22/9/25
# Description: Create path_control.py to let the Robot move following user-defined path

from microbit import sleep, display, Image, button_a, button_b
import tinybit

display.show(Image.HAPPY)
show_vertical_line = Image("00900:00900:00900:00900:00900")  # Dot matrix display of '|'
show_horizontal_line = Image("00000:00000:99999:00000:00000")  # Display of '-'
show_O = Image("09990:90009:90009:90009:09990")  # Dot matrix display of the 'O'
show_triangle = Image("00900:09090:99999:00000:00000")  # Dot matrix display of triangle

a = 0  # Variable a is used to display that path
b = 0  # Variable b is used to determine whether to start the car's movement

speed_run = 100  # The speed values of the trolley's operation
speed_spin = 110  # The speed values of the trolley's rotation

# Run along the trajectory of the letter '|'
def run_vertical_line():
    display.show(show_vertical_line)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_stop()
        global b
        b = 0

# Run along the trajectory of the '-'
def run_horizontal_line():
    display.show(show_horizontal_line)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_spinleft(160)
        sleep(400)
        tinybit.car_run(80)
        sleep(1500)
        tinybit.car_stop()
        global b
        b = 0

# Run along the trajectory of 'O'
def run_O():
    display.show(show_O)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_spinright(120)
        sleep(400)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_spinright(120)
        sleep(400)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_spinright(120)
        sleep(400)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_stop()
        global b
        b = 0

# Run along the trajectory of triangle
def run_triangle():
    display.show(show_triangle)
    global b
    if b == 1:
        sleep(1000)
        tinybit.car_spinright(60)
        sleep(400)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_spinright(60)
        sleep(500)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_spinright(220)
        sleep(500)
        tinybit.car_run(80)
        sleep(1000)
        tinybit.car_stop()
        global b
        b = 0


while True:
    # 'A' controls the route switching of the trolley
    if button_a.was_pressed():
        a = a + 1
        if a >= 5:
            a = 1
    # 'B' controls the trolley to run along the route
    if button_b.was_pressed():
        b = 1
    if a == 1:
        run_vertical_line()
    elif a == 2:
        run_horizontal_line()
    elif a == 3:
        run_O()
    elif a == 4:
        run_triangle()
