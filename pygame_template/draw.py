from pygame import Vector2 as V2
import pygame
import random
from pygame_template.utils import Rect



class Drawer:
    class RECTANGLE:
        def __init__(self):
            self.active = False
            self.rects = []
            self.colors = []
            self.border_colors = []

        def update(self):
            mdown = pygame.mouse.get_pressed()[0]
            mpos = pygame.mouse.get_pos()
            if not self.active:
                if mdown:
                    self.active = True
                    self.pos1 = V2(mpos)
                    self.pos2 = V2(mpos)
                    self.current_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 50)
                    self.current_border_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 100)
            else:
                self.pos2 = V2(mpos)
                if not mdown: 
                    self.active = False
                    l = min(self.pos1.x, self.pos2.x)
                    t = min(self.pos1.y, self.pos2.y)
                    w = abs(self.pos2.x - self.pos1.x)
                    h = abs(self.pos2.y - self.pos1.y)
                    self.rects.append(pygame.Rect(l, t, w, h))
                    self.colors.append(self.current_color)
                    self.border_colors.append(self.current_border_color)
                    self.pos1 = V2()
                    self.pos2 = V2()

        def draw(self, screen):
            for i, rect in enumerate(self.rects):
                pygame.draw.rect(screen, self.colors[i], rect)
                pygame.draw.rect(screen, self.border_colors[i], rect, 2)
            if self.active:
                l = min(self.pos1.x, self.pos2.x)
                t = min(self.pos1.y, self.pos2.y)
                w = abs(self.pos2.x - self.pos1.x)
                h = abs(self.pos2.y - self.pos1.y)
                temp_rect = pygame.Rect(l, t, w, h)
                pygame.draw.rect(screen, self.current_color, temp_rect)
                pygame.draw.rect(screen, self.current_border_color, temp_rect, 2)

    class TRIANGLE:
        def __init__(self):
            self.active = False
            self.triangles = []
            self.colors = []
            self.border_colors = []

        def update(self):
            mdown = pygame.mouse.get_pressed()[0]
            mpos = pygame.mouse.get_pos()

            if not self.active:
                if mdown:
                    self.active = True
                    self.pos1 = V2(mpos)
                    self.pos2 = V2(mpos)
                    self.current_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 50)
                    self.current_border_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 100)
            else:
                self.pos2 = V2(mpos)
                if not mdown: 
                    self.active = False
                    l = min(self.pos1.x, self.pos2.x)
                    t = min(self.pos1.y, self.pos2.y)
                    w = abs(self.pos2.x - self.pos1.x)
                    h = abs(self.pos2.y - self.pos1.y)
                    if self.pos2.y < self.pos1.y: self.triangles.append([(l, t+h), (l+w/2, t), (l+w, t+h)])
                    else: self.triangles.append([(l, t), (l + w, t), (l + w / 2, t + h)])
                    self.colors.append(self.current_color)
                    self.border_colors.append(self.current_border_color)
                    self.pos1 = V2()
                    self.pos2 = V2()

        def draw(self, screen):
            for i, triangle in enumerate(self.triangles):
                pygame.draw.polygon(screen, self.colors[i], triangle)
                pygame.draw.polygon(screen, self.border_colors[i], triangle, 2)
            if self.active:
                l = min(self.pos1.x, self.pos2.x)
                t = min(self.pos1.y, self.pos2.y)
                w = abs(self.pos2.x - self.pos1.x)
                h = abs(self.pos2.y - self.pos1.y)
                if self.pos2.y < self.pos1.y: temp_triangle = [(l, t+h), (l+w/2, t), (l+w, t+h)]
                else: temp_triangle = [(l, t), (l+w, t), (l+w / 2, t+h)]
                pygame.draw.polygon(screen, self.current_color, temp_triangle)
                pygame.draw.polygon(screen, self.current_border_color, temp_triangle, 2)

    class ELLIPSE:
        def __init__(self):
            self.active = False
            self.ellipses = []
            self.colors = []
            self.border_colors = []

        def update(self):
            mdown = pygame.mouse.get_pressed()[0]
            mpos = pygame.mouse.get_pos()

            if not self.active:
                if mdown:
                    self.active = True
                    self.pos1 = V2(mpos)
                    self.pos2 = V2(mpos)
                    self.current_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 50)
                    self.current_border_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255), 100)
            else:
                self.pos2 = V2(mpos)
                if not mdown: 
                    self.active = False
                    l = min(self.pos1.x, self.pos2.x)
                    t = min(self.pos1.y, self.pos2.y)
                    w = abs(self.pos2.x - self.pos1.x)
                    h = abs(self.pos2.y - self.pos1.y)
                    self.ellipses.append(pygame.Rect(l, t, w, h))
                    self.colors.append(self.current_color)
                    self.border_colors.append(self.current_border_color)
                    self.pos1 = V2()
                    self.pos2 = V2()

        def draw(self, screen):
            for i, ellipse in enumerate(self.ellipses):
                pygame.draw.ellipse(screen, self.colors[i], ellipse)
                pygame.draw.ellipse(screen, self.border_colors[i], ellipse, 2)
            if self.active:
                l = min(self.pos1.x, self.pos2.x)
                t = min(self.pos1.y, self.pos2.y)
                w = abs(self.pos2.x - self.pos1.x)
                h = abs(self.pos2.y - self.pos1.y)
                temp_ellipse = pygame.Rect(l, t, w, h)
                pygame.draw.ellipse(screen, self.current_color, temp_ellipse)
                pygame.draw.ellipse(screen, self.current_border_color, temp_ellipse, 2)

    SHAPES = ('rect', 'ellipse', 'triangle')

    def __init__(self):
        '''
        A drawing utility class that handles shape creation and management.

        Usage:
        1. Initialize the drawer instance
        2. Add desired shapes using add_shape()
        3. Optionally set active shape with set_current_drawer()
        4. Call update() and draw() in the main loop

        Available Shapes:
        - rect: Rectangle
        - ellipse: Ellipse
        - triangle: Triangle
        '''
        self.shape_drawers = {}
        self.current_drawer = None
        self.draw_enabled = True

    def add_shape(self, shape_name: str, change_current_drawer_to_given=True):
        '''
        Add a shape drawer to the available shapes.
        
        Args:
            shape_name (str): Shape type to add ('rect', 'ellipse', 'triangle')
            change_current_drawer_to_given (bool): Set as active shape if True
        '''
        if shape_name == "rect": self.shape_drawers["rect"] = self.RECTANGLE()
        elif shape_name == "ellipse": self.shape_drawers["ellipse"] = self.ELLIPSE()
        elif shape_name == "triangle": self.shape_drawers["triangle"] = self.TRIANGLE()
        if change_current_drawer_to_given: self.current_drawer = shape_name

    def set_current_drawer(self, shape_name: str):
        '''
        Set the active shape for drawing.

        Args:
            shape_name (str): Shape type to activate
        
        Returns:
            bool: True if shape was activated, False if shape not found
        '''
        if shape_name in self.shape_drawers:
            self.current_drawer = shape_name
            return True
        return False

    def toggle_draw(self):
        '''
        Toggle drawing functionality on/off.
        Does not clear existing shapes from screen.

        Returns:
            bool: New drawing state
        '''
        self.draw_enabled = not self.draw_enabled
        return self.draw_enabled

    def update(self):
        if self.draw_enabled and self.current_drawer:
            drawer = self.shape_drawers[self.current_drawer]
            drawer.update()

    def draw(self, screen):
        for drawer in self.shape_drawers.values():
            drawer.draw(screen)


class SelectionBox:
    def __init__(self):
        self.spr = None
        self.col = (255, 255, 255, 50)
        self.position = (0, 0)
        self.pos1 = V2()
        self.pos2 = V2()
        self.active = False

    def update(self, rects=[]):
        mdown = pygame.mouse.get_pressed()[0]
        mpos = pygame.mouse.get_pos()
        if not self.active:
            if mdown:
                self.active = True
                self.pos1 = V2(mpos)
                self.pos2 = V2(mpos)
        else:
            self.pos2 = V2(mpos)
            if not mdown: self.active = False
        l = min(self.pos1.x, self.pos2.x)
        t = min(self.pos1.y, self.pos2.y)
        w = abs(self.pos2.x - self.pos1.x)
        h = abs(self.pos2.y - self.pos1.y)
        self.spr = pygame.Surface((w, h), pygame.SRCALPHA)
        self.position = (l, t)
        if rects:
            selection_rect = pygame.Rect(self.position, (w, h))
            if (type(rects[0]) == pygame.Rect) or (type(rects[0]) == pygame.FRect):
                colliding_rects = [rect for rect in rects if selection_rect.colliderect(rect)]
                return colliding_rects
            elif isinstance(rects[0], Rect):
                colliding_rects = [rect for rect in rects if selection_rect.colliderect(rect.rect)]
                return colliding_rects
        return list()

    def draw(self, screen):
        if self.active:
            self.spr.fill(self.col)
            pygame.draw.rect(self.spr, (255, 255, 255, 100), (0, 0, *self.spr.get_size()), 2)
            screen.blit(self.spr, self.position)

