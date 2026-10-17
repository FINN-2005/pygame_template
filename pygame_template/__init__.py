

import pygame
import random
import math
import time
import numpy as np
import re
from pathlib import Path

pygame.init()

from pygame_template.utils import Group, Sprite, Rect, get_Font, get_2d_input_dir, get_3d_input_dir, get_random_screen_pos, lerp, perlin_noise
from pygame_template.animation import Animation_player, Timer
from pygame_template.inputs import Input_manager
from pygame_template.colors import Color
from pygame_template.draw import Drawer, SelectionBox
from pygame_template.main import APP

from pygame import Vector2 as V2
from pygame import Vector3 as V3

from os.path import join
