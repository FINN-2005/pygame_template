import random
from pygame import color





class Color:
    salmon = '#ffc8b3'
    dark_purple = '#4a0046'

    @classmethod
    def random(cls):
        r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        return [r,g,b,255]

    @classmethod
    def add_pygame_colors(cls):
        for color_name in color.THECOLORS:
            setattr(cls, color_name, color.THECOLORS[color_name])

Color.add_pygame_colors()
            
