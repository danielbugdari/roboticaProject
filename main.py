#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.iodevices import *
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
        self.ev3 = EV3Brick()
        

        movingSpeed = configuration.movingSpeed
        runTime = configuration.runTime

        # Write your program here.
        # ev3.speaker.beep()
        # self.camera =  I2CDevice(Port.S2, 0x02 >> 1)
        # self.camera.write(0x41, 'B')
        # self.camera =   Ev3devSensor(Port.S3)
        
        self.motorLeft = Motor(Port.C)
        self.motorRight = Motor(Port.A)
        self.motorUpDown = Motor(Port.B)

        self.stopRight = TouchSensor(Port.S1)
        self.stopLeft = TouchSensor(Port.S4)


    def reset_motor_position(self):
    # This funtion moves the arms of the robot to the initial position
        # reset little motor:
        # self.motorUpDown.run(5)
        # while abs(self.motorUpDown.speed()) > 5:
        #     time.sleep(0.001)
        # self.motorUpDown.stop()
        myRobot.ev3.speaker.say('Reset Arms Position')
        self.pen_up()

        # reset two big motors:
        self.motorLeft.run(speed=-configuration.returnHomeSpeed)
        self.motorRight.run(speed=configuration.returnHomeSpeed)
        aPressed = False
        bPressed = False

        while True:
            if self.stopLeft.pressed():
                self.motorLeft.stop()
                aPressed = True
            if self.stopRight.pressed():
                self.motorRight.stop()
                bPressed = True
            if aPressed and bPressed:
                break

        self.pen_down()


    def run_to_postion(self, left_pos, right_pos):
    # This function 
        if not self.stopLeft.pressed() or not self.stopRight.pressed():
            self.motorUpDown.run_time(speed=-700,time=300)
            self.motorLeft.run_time(speed=left_pos[0],time=left_pos[1])
            self.motorRight.run_time(speed=right_pos[0],time=right_pos[1]) 


    def pen_up(self):
        self.motorUpDown.run_time(speed=500, time=350)

    def pen_down(self):
        self.motorUpDown.run_time(speed=-500, time=300)

    def move_two_motors(self):
        roboticValue = DriveBase(left_motor=self.motorLeft, right_motor=self.motorRight, wheel_diameter=1,axle_track=110)
        roboticValue.straight(5)
        roboticValue.turn(5)
        roboticValue.straight(5)
        roboticValue.stop()
        roboticValue.reset()

    def test(self):
        # while True:
        # roboticValue = DriveBase(left_motor=self.motorLeft, right_motor=self.motorRight, wheel_diameter=1, axle_track=1)
        # while True:
        #     roboticValue.turn(5)
        # speed = 300
        # self.pen_up()
        # self.motorLeft.run(speed)
        # # self.motorRight.run(0.5*speed)
        # time.sleep(5)
        # self.motorLeft.stop()
        # self.motorRight.stop()

        # # self.motorLeft.run(-0.5*speed)
        # self.motorRight.run(speed)
        # time.sleep(5)
        # self.motorLeft.stop()
        # self.motorRight.stop()

        # self.motorLeft.run(-speed)
        # # self.motorRight.run(-speed)
        # time.sleep(5)
        # self.motorLeft.stop()
        # self.motorRight.stop()

        # self.motorRight.run(-speed)
        # time.sleep(5)
        # self.motorLeft.stop()
        # self.motorRight.stop()
        # ---
        # pass
        # self.motorLeft.run(100)
        # currentTime = time.time()*1000.0
        # factor=1.0
        # while ((time.time()*1000.0 - currentTime) < 5000 ):
        #     self.motorRight.run(-100*factor)
        #     factor+=0.1
        #     time.sleep(0.2)
        # self.pen_up()
        # self.motorLeft.run(500)
        # self.motorRight.run(-500)
        # time.sleep(5)
        # self.motorRight.stop()
        # self.motorLeft.stop()
        # self.pen_down()
        
        # # Rectangle:
        while True:
            ##
            self.motorLeft.run(-500)
            # self.motorRight.run(+100)
            time.sleep(3)
            self.motorLeft.stop()

            # self.motorLeft.run(-300)
            self.motorRight.run(500)
            self.motorLeft.run(-200)
            time.sleep(3)
            self.motorRight.stop()
            self.motorLeft.stop()

            self.motorLeft.run(+500)
            # self.motorRight.run(-100)
            time.sleep(3)
            self.motorLeft.stop()

            # self.motorLeft.run(+300)
            self.motorRight.run(-500)
            self.motorLeft.run(+200)
            time.sleep(3)
            self.motorRight.stop()
            self.motorLeft.stop()
            ##
        # self.motorRight.run(-500)
        ############# Test boundries #############
        # self.motorLeft.run(+500)
        # time.sleep(8)
        # self.motorLeft.stop()

        # self.motorRight.run(-500)
        # time.sleep(8)
        # self.motorRight.stop()

        # self.motorLeft.run(-500)
        # time.sleep(8)
        # self.motorLeft.stop()

        # self.motorRight.run(+500)
        # time.sleep(8)
        # self.motorRight.stop()

        # self.motorRight.stop()
        # self.motorLeft.stop()
        # self.pen_up()
        
        
    # def camera1(self):
    #     while True:
    #     # self.camera =  I2CDevice(Port.S2, 0x02 >> 1)
    #     # self.camera.write(0x41, 'B')
    #         a = self.camera.read('TRACK')
    #         print(a)
    #         time.sleep(1)


    def print(self, print_order):
        """
        This function prints an object by given dictionary:
        print_order = {
                      object_name: "object",
                      (dictionary)orders = 
                      {'1': {command: 'both/right/left/up/down',
                             command_tupple: both - tuple(rightSpeed, LeftSpeed, sleepTime)
                                             right - tuple(rightSpeed, sleepTime)
                                             left - tuple(leftSpeed, sleepTime)
                                             up - call pen_up function
                                             down - call pen_down function},
                       '2': {command: 'both/right/left/up/down',
                                command_tupple: both - tuple(rightSpeed, LeftSpeed, sleepTime)
                                                right - tuple(rightSpeed, sleepTime)
                                                left - tuple(leftSpeed, sleepTime)
                                                up - call pen_up function
                                                down - call pen_down function},
                        etc...
                        }
        """
        self.ev3.speaker.say(print_order['object_name'])
        keys = list(print_order['orders'].keys())
        for order in range(len(keys)):  # run over all commands
            command = print_order['orders']['{}'.format(order+1)]
            this_command = command['command']
            command_tupple = command['command_tupple']

            if this_command == 'both':
                self.motorRight.run((-1)*command_tupple[0])
                self.motorLeft.run(command_tupple[1])
                time.sleep(command_tupple[2])
            elif this_command == 'right':
                self.motorRight.run((-1)*command_tupple[0])
                time.sleep(command_tupple[1])
            elif this_command == 'left':
                self.motorLeft.run(command_tupple[0])
                time.sleep(command_tupple[1])
            elif this_command == 'up':
                self.pen_up()
            elif this_command == 'down':
                self.pen_down()
            
            self.motorRight.stop()
            self.motorLeft.stop()
        
        
    def clicks_controller(self):
        """
        This function gets input from EV3 touchSensor to decide what command to execute
        """
        # self.stopRight
        def execute(number_of_clicks):
            """
            This function executes printing according to amount of pressing on the touchSensor
            """
            if number_of_clicks == 0:
                return False
            if number_of_clicks == 1:
                self.print(configuration.print_shapes['Line'])
            elif number_of_clicks == 4:
                self.print(configuration.print_shapes['Rectangle'])
            return True

        running = True  # run flag
        clicks = 0  # clicks counter to determine action
        end_timeout_seconds = 5 # seconds
        proccess_time = 2 # seconds
        start_time = time.time()  # time in seconds

        while running:
            if time.time() - start_time > proccess_time:  # make decision after 2 seconds
                execute(clicks)
                clicks = 0  # reset clicks counter every 2 seconds

            if self.stopRight.pressed():
                start_time = time.time()  # time in seconds
                clicks += 1  # add click counter
                while self.stopRight.pressed():  # for case of long pressing
                    pass
                end_time = time.time()
                
                if (end_time - start_time) > end_timeout_seconds:
                    running = False
                    clicks = 0



if __name__ == "__main__":
    print("main")
    myRobot = PrintingRobot()  # init robot class
    myRobot.ev3.speaker.say('Started Printing Robot Program')
    # myRobot.reset_motor_position()  # reset position

    # myRobot.move_two_motors()
    # myRobot.camera1()
    # myRobot.test()
    # myRobot.print(configuration.print_shapes['Triangle'])
    # myRobot.reset_motor_position()  # reset position
    myRobot.clicks_controller()
    # myRobot.print(configuration.print_shapes['Rectangle'])
    #####
    # arrLeft = [[configuration.movingSpeed, configuration.runTime], [200, 1000]]
    # arrRight = [[-configuration.movingSpeed, configuration.runTime], [500, 2000]]
    # for obj in arrLeft:
    #     myRobot.run_to_postion(arrLeft[obj], arrRight[obj])
    
    #####
    myRobot.reset_motor_position()
    myRobot.ev3.speaker.say('Finished Printing Robot Program')

