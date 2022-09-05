## This Module configures parameters being used in the EV3 printing project

# return arms to initial position settings:
returnHomeSpeed = 500
returnHomeTime = 500

### General Settings: ###
movingSpeed = 500
runTime = 2000

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
print_shapes = {'Circle': {'object_name': '2 Lines',
                               'orders': {
                                '1': {'command': 'both',
                                                'command_tupple': (200, 200, 2)},
                                '2': {'command': 'up',
                                    'command_tupple': (0)},
                                '3': {'command': 'down',
                                    'command_tupple': (0)},
                                '4': {'command': 'left',
                                    'command_tupple': (200, 3)},
                                '5': {'command': 'left',
                                    'command_tupple': (-200, 3)},
                                '6': {'command': 'right',
                                    'command_tupple': (200, 3)},
                                '7': {'command': 'right',
                                    'command_tupple': (-200, 3)},
                                                }},
                'Rectangle': {'object_name': 'Rectangle',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (200, 200, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (0, 300, 4)},
                                '5': {'command': 'both',
                                                'command_tupple': (300, 0, 4)},
                                '6': {'command': 'both',
                                                'command_tupple': (0, -300, 4)},
                                '7': {'command': 'both',
                                                'command_tupple': (-300, 0, 4)}
                                                
                                                }},
                'Triangle': {'object_name': 'Triangle',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (200, 200, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (300, 300, 4)},
                                '5': {'command': 'both',
                                                'command_tupple': (-300, 0, 4)},
                                '6': {'command': 'both',
                                                'command_tupple': (0, -300, 4)},
                                                
                                                }},
                'Line': {'object_name': 'Line',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (200, 200, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (300, 300, 4)}
                                                
                                                }},
                'House': {'object_name': 'House',
                               'orders': {
                                '1': {'command': 'up',
                                                'command_tupple': (0)},
                                '2': {'command': 'both',
                                                'command_tupple': (200, 200, 4)},
                                '3': {'command': 'down',
                                                'command_tupple': (0)},
                                '4': {'command': 'both',
                                                'command_tupple': (0, 300, 4)},
                                '5': {'command': 'both',
                                                'command_tupple': (300, 0, 4)},
                                '6': {'command': 'both',
                                                'command_tupple': (150, -150, 4)},  # make triangle on top of house
                                '7': {'command': 'both',
                                                'command_tupple': (-150, 150, 4)},  # make triangle on top of house
                                '8': {'command': 'both',
                                                'command_tupple': (0, -300, 4)},
                                '9': {'command': 'both',
                                                'command_tupple': (150, 150, 4)}, # make triangle on top of house
                                '10': {'command': 'both',
                                                'command_tupple': (-150, -150, 4)}, # make triangle on top of house
                                '11': {'command': 'both',
                                                'command_tupple': (-300, 0, 4)}
                                                
                                                }}}