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




# roboticValue = DriveBase(left_motor=motorLeft, right_motor=motorRight, wheel_diameter=1,axle_track=110)
# roboticValue.turn(-30)
# motorLeft.run_target(500,90)
# motorRight.run_target(500,-90)


# motorUpDown.run_time(speed=700,time=300)
# motorLeft.run_time(speed=movingSpeed,time=runTime)
# motorRight.run_time(speed=-movingSpeed,time=runTime)
# motorUpDown.run_time(speed=-700,time=300)
# motorLeft.run_time(speed=500,time=2000)
# motorRight.run_time(speed=-500,time=1000)

# arrLeft = [[500, 1000], [200, 1000]]
# arrRight = [[500, 1000], [500, 2000]]

# run_to_postion(arrLeft[1], arrRight[1])


class PrintingRobot():
    def __init__(self):
        # Create your objects here.
        ev3 = EV3Brick()

        movingSpeed = configuration.movingSpeed
        runTime = configuration.runTime

        # Write your program here.
        # ev3.speaker.beep()

        self.motorLeft = Motor(Port.C)
        self.motorRight = Motor(Port.A)
        self.motorUpDown = Motor(Port.B)

        self.stopRight = TouchSensor(Port.S1)
        self.stopLeft = TouchSensor(Port.S4)


    def reset_motor_position(self):
    # This funtion moves the arms of the robot to the initial position
        # reset little motor:
        # self.motorUpDown.rotate_forever(speed=-50, regulate='off')
        # time.sleep(0.5)
        # while(abs(self.motorUpDown.speed) > 5):
        #     time.sleep(0.001)
        # self.motorUpDown.stop()

        # reset two big motors:
        while True:
            self.motorLeft.run_time(speed=-configuration.returnHomeSpeed,time=configuration.returnHomeTime)
            if self.stopLeft.pressed():
                break

        while True:
            self.motorRight.run_time(speed=configuration.returnHomeSpeed,time=configuration.returnHomeTime)
            if self.stopRight.pressed():
                break

    def run_to_postion(self, left_pos, right_pos):
    # This function 
        if not self.stopLeft.pressed() or not self.stopRight.pressed():
            self.motorUpDown.run_time(speed=-700,time=300)
            self.motorLeft.run_time(speed=left_pos[0],time=left_pos[1])
            self.motorRight.run_time(speed=right_pos[0],time=right_pos[1]) 

    def move_forward_naive(self):
        self.motorLeft.run_time(speed=500,time=2000)
        self.motorRight.run_time(speed=-500,time=2000) 

    def move_two_motors(self):
        roboticValue = DriveBase(left_motor=self.motorLeft, right_motor=self.motorRight, wheel_diameter=1,axle_track=110)
        roboticValue.straight(5)
        roboticValue.turn(5)
        roboticValue.straight(5)
        roboticValue.stop()
        roboticValue.reset()

    def run_by_command():
        print("Enter Angle:")
        angle=int(input())
        print("Enter Time:")
        time=int(input())



if __name__ == "__main__":
    print("main")
    myRobot = PrintingRobot()
    myRobot.reset_motor_position()  # reset position
    myRobot.move_forward_naive()
    myRobot.move_two_motors()
    #####
    # arrLeft = [[configuration.movingSpeed, configuration.runTime], [200, 1000]]
    # arrRight = [[-configuration.movingSpeed, configuration.runTime], [500, 2000]]
    # for obj in arrLeft:
    #     myRobot.run_to_postion(arrLeft[obj], arrRight[obj])
    
    #####
    myRobot.reset_motor_position()

