# Author: Yujin Nie
# Date: 22/9/25
# Description: Create the Python program file to let the Robot move

from microbit import display, Image
import tinybit

display.show(Image.ARROW_S) # Display the forward arrow on the microbit dot matrix
tinybit.car_run(150) # Drive the tinybit car to move forward
