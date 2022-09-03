# return arms to initial position settings:
returnHomeSpeed = 500
returnHomeTime = 500

### General Settings: ###
movingSpeed = 500
runTime = 2000

## Shape Configuartion Database:
# 'Shape': []
print_shapes = {'Rectangle': {'object_name': 'Rectangle',
                               'orders': {
                                '1': {'command': 'both',
                                                'command_tupple': (-200, 200, 2)},
                                '2': {'command': 'up',
                                    'command_tupple': (0)},
                                '3': {'command': 'down',
                                    'command_tupple': (0)},
                                '4': {'command': 'left',
                                    'command_tupple': (200, 3)},
                                '5': {'command': 'right',
                                    'command_tupple': (-200, 2)},
                                '6': {'command': 'both',
                                    'command_tupple': (-200, 200, 2)}
                                                }},
                'Circle': [],
                'Triangle': []}