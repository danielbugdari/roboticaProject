## This Module configures parameters being used in the EV3 printing project

# return arms to initial position settings:
returnHomeSpeed = 500
returnHomeTime = 500

### General Settings: ###
movingSpeed = 300  # while printing
movePositionSpeed = 200  # when not printing - pen up
switchBetweenModesSec = 3  # camera/clicks mode and power off
processTimeBetweenClicks = 2 # proccess time after clicking until robot decides action

## Shape Configuartion Database:
# print_order = {
#             object_name: "object",
#             (dictionary)orders = 
#             {'1': {command: 'both/right/left/up/down',
#                     command_tupple: both - tuple(rightSpeed, LeftSpeed, sleepTime)
#                                     right - tuple(rightSpeed, sleepTime)
#                                     left - tuple(leftSpeed, sleepTime)
#                                     up - call pen_up function
#                                     down - call pen_down function},
#             '2': {command: 'both/right/left/up/down',
#                     command_tupple: both - tuple(rightSpeed, LeftSpeed, sleepTime)
#                                     right - tuple(rightSpeed, sleepTime)
#                                     left - tuple(leftSpeed, sleepTime)
#                                     up - call pen_up function
#                                     down - call pen_down function},
#             etc...
#             }
print_shapes = {'2_Lines': {'object_name': '2_Lines',
                               'orders': {
                                '1': {'command': 'up',
                                    'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (movePositionSpeed, movePositionSpeed, 4)},
                                '3': {'command': 'down',
                                    'command_tupple': (0)},
                                '4': {'command': 'left',
                                    'command_tupple': (movingSpeed, 4)},
                                '5': {'command': 'left',
                                    'command_tupple': (-movingSpeed, 4)},
                                '6': {'command': 'right',
                                    'command_tupple': (movingSpeed, 4)},
                                '7': {'command': 'right',
                                    'command_tupple': (-movingSpeed, 4)},
                                                }},
                'Rectangle': {'object_name': 'Rectangle',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (movePositionSpeed, movePositionSpeed, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (0, movingSpeed, 4)},
                                '5': {'command': 'both',
                                                'command_tupple': (movingSpeed, 0, 4)},
                                '6': {'command': 'both',
                                                'command_tupple': (0, -movingSpeed, 4)},
                                '7': {'command': 'both',
                                                'command_tupple': (-movingSpeed, 0, 4)}
                                                
                                                }},
                'Triangle': {'object_name': 'Triangle',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (movePositionSpeed, movePositionSpeed, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (movingSpeed, movingSpeed, 4)},
                                '5': {'command': 'both',
                                                'command_tupple': (-movingSpeed, 0, 4)},
                                '6': {'command': 'both',
                                                'command_tupple': (0, -movingSpeed, 4)},
                                                
                                                }},
                'Line': {'object_name': 'Line',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (movePositionSpeed, movePositionSpeed, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (movingSpeed, movingSpeed, 4)}
                                                
                                                }},
                'House': {'object_name': 'House',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (movePositionSpeed, movePositionSpeed, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (0, movingSpeed, 4)},
                                '5': {'command': 'both',
                                                'command_tupple': (movingSpeed, 0, 4)},
                                '6': {'command': 'both',
                                                'command_tupple': (int(0.5*movingSpeed), -int(0.5*movingSpeed), 4)},  # make triangle on top of house
                                '7': {'command': 'up',
                                                'command_tupple': (0)},
                                '8': {'command': 'both',
                                                'command_tupple': (-int(0.5*movingSpeed), int(0.5*movingSpeed), 4)},  # make triangle on top of house
                                '9': {'command': 'down',
                                                'command_tupple': (0)},
                                '10': {'command': 'both',
                                                'command_tupple': (0, -movingSpeed, 4)},
                                '11': {'command': 'both',
                                                'command_tupple': (int(0.5*movingSpeed), int(0.5*movingSpeed), 4)}, # make triangle on top of house
                                '12': {'command': 'up',
                                                'command_tupple': (0)},
                                '13': {'command': 'both',
                                                'command_tupple': (-int(0.5*movingSpeed), -int(0.5*movingSpeed), 4)}, # make triangle on top of house
                                '14': {'command': 'down',
                                                'command_tupple': (0)},
                                '15': {'command': 'both',
                                                'command_tupple': (-movingSpeed, 0, 4)}
                                                
                                                }}}