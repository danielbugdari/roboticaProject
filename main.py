#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()
# motorLeft = ev3.OUTPUT_C #mymotor(OUTPUT_C)
# motorLeft.run(5)
motorLeft = Motor(Port.C)
motorRight = Motor(Port.A)
# motorLeft.run_target(500,90)
# motorRight.run_target(500,-90)
motorLeft.run_time(speed=500,time=1000)
motorRight.run_time(speed=-500,time=1000)
