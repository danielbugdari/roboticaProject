#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
import configuration
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


def run_to_postion(left_pos, right_pos):
    if not stopLeft.pressed() or not stopRight.pressed():
        motorUpDown.run_time(speed=-700,time=300)
        motorLeft.run_time(speed=left_pos[0],time=left_pos[1])
        motorRight.run_time(speed=right_pos[0],time=right_pos[1]) 


# Create your objects here.
ev3 = EV3Brick()

movingSpeed = configuration.movingSpeed
runTime = configuration.runTime
# Write your program here.
# ev3.speaker.beep()
# motorLeft = ev3.OUTPUT_C #mymotor(OUTPUT_C)
# motorLeft.run(5)
motorLeft = Motor(Port.C)
motorRight = Motor(Port.A)
motorUpDown = Motor(Port.B)

# stopLeft = TouchSensor(Port.S3)
# stopRight = TouchSensor(Port.S2)
# motorLeft.run_target(500,90)
# motorRight.run_target(500,-90)

# motorLeft.run_time(speed=-500,time=500)
# motorRight.run_time(speed=-500,time=1000)

# motorUpDown.run_time(speed=700,time=300)
motorLeft.run_time(speed=movingSpeed,time=runTime)
motorRight.run_time(speed=-movingSpeed,time=runTime)
# motorUpDown.run_time(speed=-700,time=300)
# motorLeft.run_time(speed=500,time=2000)
# motorRight.run_time(speed=-500,time=1000)

# arrLeft = [[500, 1000], [200, 1000]]
# arrRight = [[500, 1000], [500, 2000]]

# run_to_postion(arrLeft[1], arrRight[1])
