#!/usr/bin/env pybricks-micropython
"""
made by:
Dan Averin 204358394
Daniel Bugdari 315846501
Sapir Naugauker 206542375
"""


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.iodevices import *
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog

import time
import configuration

class PrintingRobot():
    """
    This is the main class of the roubot and the גefinition of all the actions he can perform
    """
    def __init__(self):
        self.ev3 = EV3Brick()

        # Outputs
        self.motorLeft = Motor(Port.C)
        self.motorRight = Motor(Port.A)
        self.motorUpDown = Motor(Port.B)

        # Inputs
        self.button = TouchSensor(Port.S2)
        self.stopRight = TouchSensor(Port.S1)
        self.stopLeft = TouchSensor(Port.S4)
        self.camera =   Ev3devSensor(Port.S3)

    def pen_up(self):
        """
        This function press on the arms to pick up the pen from the paper
        """
        self.motorUpDown.run_time(speed=450, time=350)


    def pen_down(self):
        """
        This function free the arms to put down the pen on the paper
        """
        self.motorUpDown.run_time(speed=-450, time=300)
        

    def reset_motor_position(self):
        """
        This funtion moves the arms of the robot to the initial position
        """
        self.pen_up()

        # reset two big motors:
        self.motorLeft.run(speed=-configuration.returnHomeSpeed)
        self.motorRight.run(speed=configuration.returnHomeSpeed)
        leftPressed =  rightPressed = False

        while True:
            if self.stopLeft.pressed():
                self.motorLeft.stop()
                leftPressed = True
            if self.stopRight.pressed():
                self.motorRight.stop()
                rightPressed = True
            if leftPressed and rightPressed:
                break

        self.pen_down()


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


    def camera_controller(self):
        """
        This function sends print command according to color sample from the camera
        """
        
        def execute(color):
            """
            This function executes the print command according to given color id
            """
            if color == 1: # red
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "Red - Rectangle")
                self.print(configuration.print_shapes['Rectangle'])
            elif color == 2: # blue
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "Blue - Triangle")
                self.print(configuration.print_shapes['Triangle'])
            elif color == 4: # green
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "Green - House")
                self.print(configuration.print_shapes['House'])
            self.reset_motor_position()


        running = True
        while running:
            if self.button.pressed():
                start_time = time.time()
                while self.button.pressed():
                    color = (self.camera.read('TRACK'))[1]  # take only the color argument
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "Color: {}".format(color))
                end_time = time.time()

                if (end_time - start_time) > 5: # Turn off
                    running = False
                else:  # execute printing
                    execute(color)


    def clicks_controller(self):
        """
        This function gets input from EV3 touchSensor to decide what command to execute
        """

        def execute(number_of_clicks):
            """
            This function executes printing according to amount of pressing on the touchSensor
            """
            if number_of_clicks == 0:
                return False
            elif number_of_clicks == 1:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "1 clicks - Line")
                self.print(configuration.print_shapes['Line'])
            elif number_of_clicks == 2:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "2 clicks - 2 Line")
                self.print(configuration.print_shapes['2_Lines'])
            elif number_of_clicks == 3:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "3 clicks - Triangle")
                self.print(configuration.print_shapes['Triangle'])
            elif number_of_clicks == 4:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "4 clicks - Rectangle")
                self.print(configuration.print_shapes['Rectangle'])
            elif number_of_clicks == 5:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "5 clicks - House")
                self.print(configuration.print_shapes['House'])
            self.reset_motor_position()
            return True
        
        running = True  # run flag
        clicks = 0  # clicks counter to determine action
        end_timeout_seconds = configuration.switchBetweenModesSec # seconds
        proccess_time = configuration.processTimeBetweenClicks # seconds
        start_time = time.time()  # time in seconds

        while running:
            if time.time() - start_time > proccess_time:  # make decision after 2 seconds
                execute(clicks)
                clicks = 0  # reset clicks counter every 2 seconds

            if self.button.pressed():
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "Clicks Mode")
                start_time = time.time()  # time in seconds
                clicks += 1  # add click counter
                while self.button.pressed(): # for case of long pressing
                    self.ev3.screen.clear()
                    self.ev3.screen.draw_text(40, 50, "{} Clicks".format(clicks))
                
                end_time = time.time()
                
                if (end_time - start_time) > end_timeout_seconds:
                    running = False
                    clicks = 0


    def set_mode(self):
        """
        This function sets the input mode of the robot - Clicks or Color Sensor
        """
        
        def execute(number_of_clicks):
            """
            This function executes printing according to amount of pressing on the touchSensor
            """
            if number_of_clicks == 0:
                return False
            if number_of_clicks == 1:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "Camera Mode")
                self.camera_controller()
            elif number_of_clicks == 2:
                self.ev3.screen.clear()
                self.ev3.screen.draw_text(40, 50, "Click Mode")
                self.clicks_controller()
            return True

        running = True  # run flag
        clicks = 0  # clicks counter to determine action
        end_timeout_seconds = configuration.switchBetweenModesSec # seconds
        proccess_time = configuration.processTimeBetweenClicks # seconds
        start_time = time.time()  # time in seconds

        while running:
            if time.time() - start_time > proccess_time:  # make decision after 2 seconds
                execute(clicks)
                clicks = 0  # reset clicks counter every 2 seconds

            if self.button.pressed():
                start_time = time.time()  # time in seconds
                clicks += 1  # add click counter
                while self.button.pressed():  # for case of long pressing
                    self.ev3.screen.clear()
                    self.ev3.screen.draw_text(40, 50, "{} Clicks".format(clicks))
                    pass
                end_time = time.time()
                
                if (end_time - start_time) > end_timeout_seconds:
                    self.ev3.screen.clear()
                    self.ev3.screen.draw_text(40, 50, "Close Program")
                    running = False
                    clicks = 0



if __name__ == "__main__":
    # init robot class
    myRobot = PrintingRobot()

    #reset the robot arm to start position before start run
    myRobot.reset_motor_position()
    
    # running the functionality of the robot
    myRobot.set_mode()

    #reset the robot arm to start position before shudown
    myRobot.reset_motor_position()
