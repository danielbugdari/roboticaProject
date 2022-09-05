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

class PrintingRobot():
    def __init__(self):
        self.ev3 = EV3Brick()

        # self.camera =  I2CDevice(Port.S2, 0x02 >> 1)
        # self.camera.write(0x41, 'B')
        # self.camera =   Ev3devSensor(Port.S3)
        
        # Outputs
        self.motorLeft = Motor(Port.C)
        self.motorRight = Motor(Port.A)
        self.motorUpDown = Motor(Port.B)

        # Inputs
        self.button = TouchSensor(Port.S2)
        self.stopRight = TouchSensor(Port.S1)
        self.stopLeft = TouchSensor(Port.S4)
        self.camera =   Ev3devSensor(Port.S3)


    def reset_motor_position(self):
    # This funtion moves the arms of the robot to the initial position
        # reset little motor:
        # self.motorUpDown.run(5)
        # while abs(self.motorUpDown.speed()) > 5:
        #     time.sleep(0.001)
        # self.motorUpDown.stop()
        # myRobot.ev3.speaker.say('Reset Arms Position')
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
        self.motorUpDown.run_time(speed=450, time=350)

    def pen_down(self):
        self.motorUpDown.run_time(speed=-450, time=300)

    def move_two_motors(self):
        roboticValue = DriveBase(left_motor=self.motorLeft, right_motor=self.motorRight, wheel_diameter=1,axle_track=110)
        roboticValue.straight(5)
        roboticValue.turn(5)
        roboticValue.straight(5)
        roboticValue.stop()
        roboticValue.reset()
        
        
    def camera_controller(self):
        """
        This function sends print command according to color sample from the camera
        """
        def execute(color):
            """
            This function executes the print command according to given color id
            """
            if color == 1: # red
                print("print red - print Rectangle")
                self.print(configuration.print_shapes['Rectangle'])
            elif color == 2: # blue
                print("print Blue - print Triangle")
                self.print(configuration.print_shapes['Triangle'])
            elif color == 4: # green
                print("print green - print House")
                self.print(configuration.print_shapes['House'])
            self.reset_motor_position()
            

        running = True
        while running:
            if self.button.pressed():
                print("Button was pressed")
                start_time = time.time()
                while self.button.pressed():
                    color = (self.camera.read('TRACK'))[1]  # take only the color argument
                print("color is {}".format(color))
                end_time = time.time()

                if (end_time - start_time) > 5: # Turn off
                    print("Turn off")
                    running = False
                else:  # execute printing
                    print("execute printing by color")
                    execute(color)


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
        # self.ev3.speaker.say(print_order['object_name'])
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
        
    def set_mode(self):
        """
        This function sets the input mode of the robot - Clicks or Color Sensor
        """
        print("inside set_mode")
        def execute(number_of_clicks):
            """
            This function executes printing according to amount of pressing on the touchSensor
            """
            print("inside set_mode -> execute {} clicks".format(number_of_clicks))
            if number_of_clicks == 0:
                return False
            if number_of_clicks == 1:
                print("camera mode")
                self.camera_controller()
            elif number_of_clicks == 2:
                print("click mode")
                self.clicks_controller()
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

            if self.button.pressed():
                start_time = time.time()  # time in seconds
                clicks += 1  # add click counter
                while self.button.pressed():  # for case of long pressing
                    print("button is pressed")
                    pass
                end_time = time.time()
                
                if (end_time - start_time) > end_timeout_seconds:
                    print("turning off")
                    running = False
                    clicks = 0


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
            elif number_of_clicks == 1:
                print("1 clicks - Line")
                self.print(configuration.print_shapes['Line'])
            elif number_of_clicks == 2:
                self.print(configuration.print_shapes['2_Lines'])
                print("2 clicks - 2 Line")
            elif number_of_clicks == 3:
                self.print(configuration.print_shapes['Triangle'])
                print("3 clicks - Triangle")
            elif number_of_clicks == 4:
                self.print(configuration.print_shapes['Rectangle'])
                print("4 clicks - Rectangle")
            elif number_of_clicks == 5:
                self.print(configuration.print_shapes['House'])
                print("5 clicks - House")
            self.reset_motor_position()
            return True

        print("Inside clicks moode")
        running = True  # run flag
        clicks = 0  # clicks counter to determine action
        end_timeout_seconds = 5 # seconds
        proccess_time = 2 # seconds
        start_time = time.time()  # time in seconds

        while running:
            if time.time() - start_time > proccess_time:  # make decision after 2 seconds
                execute(clicks)
                clicks = 0  # reset clicks counter every 2 seconds

            if self.button.pressed():
                print("btn is prsd")
                start_time = time.time()  # time in seconds
                clicks += 1  # add click counter
                while self.button.pressed():  # for case of long pressing
                    print("prsd down")
                    pass
                end_time = time.time()
                
                if (end_time - start_time) > end_timeout_seconds:
                    running = False
                    clicks = 0



if __name__ == "__main__":
    print("main")
    myRobot = PrintingRobot()  # init robot class
    myRobot.reset_motor_position()
    myRobot.set_mode()  # running the functionality of the robot
    # myRobot.camera_controller()
    # myRobot.ev3.speaker.say('Started Printing Robot Program')

    # myRobot.move_two_motors()
    # myRobot.camera1()
    # myRobot.print(configuration.print_shapes['Triangle'])
    # myRobot.reset_motor_position()  # reset position
    # myRobot.clicks_controller()
    #myRobot.print(configuration.print_shapes['House'])
    #####
    # arrLeft = [[configuration.movingSpeed, configuration.runTime], [200, 1000]]
    # arrRight = [[-configuration.movingSpeed, configuration.runTime], [500, 2000]]
    # for obj in arrLeft:
    #     myRobot.run_to_postion(arrLeft[obj], arrRight[obj])
    
    #####
    myRobot.reset_motor_position()
    # myRobot.ev3.speaker.say('Finished Printing Robot Program')
    # myRobot.ev3.speaker.say('Sapir Daniel and Dan Made me')

