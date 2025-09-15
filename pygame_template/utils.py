import pygame
import random
from typing import Union
from pygame import Vector2 as V2
from pygame import Vector3 as V3
from numpy import cos, sin, pi


def get_Font(size=32, font='Arial', bold=False, italic=False):
    return pygame.font.SysFont(font, size, bold, italic)

def get_2d_input_dir() -> V2:
    keys = pygame.key.get_pressed()
    direction = V2(
        (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT]),
        (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])
    )
    if direction.magnitude_squared(): return direction.normalize()
    return direction

def get_3d_input_dir() -> V3:
    keys = pygame.key.get_pressed()
    direction = V3(
        (keys[pygame.K_d]) - (keys[pygame.K_a]),
        (keys[pygame.K_SPACE] ) - (keys[pygame.K_LSHIFT]),
        (keys[pygame.K_s]) - (keys[pygame.K_w])
    )
    if direction.magnitude_squared(): return direction.normalize()
    return direction



class Group(pygame.sprite.Group):
    def __init__(self, *sprites, screen=None):
        super().__init__(*sprites)
        
        self.screen = pygame.display.get_surface() if screen==None else screen

    def draw(self):
        for spr in self.sprites():
            if hasattr(spr, 'draw') and callable(getattr(spr, 'draw')): spr.draw(self.screen)
            else: self.screen.blit(spr.image, spr.rect)
    
    def draw_on_top(self, spr):
        if spr in self.sprites():
            self.remove(spr)
            self.add(spr)

    def __getattr__(self, name):
        def forwarder(*args, **kwargs):
            return_values = []
            for spr in self.sprites():
                method = getattr(spr, name, None)
                if callable(method): return_values.append(method(*args, **kwargs))
            return return_values
        return forwarder

class Sprite(pygame.sprite.Sprite):
    ...


class Rect:
    def __init__(self, l=100, t=100, w=100, h=100, col='white', draw_border=False, border_col='white', border_size=3, border_radius=0,):
        self.rect = pygame.Rect(l,t,w,h)
        
        self.col = col
        self.border_col = border_col
        self.border_size = border_size
        self.border_radius = border_radius
        self.draw_border = draw_border
        self.highlighted = False
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.col, self.rect, 0, self.border_radius)
        if self.draw_border:
            pygame.draw.rect(screen, self.border_col, self.rect, self.border_size, self.border_radius)
        if self.highlighted:
            overlay = pygame.Surface((self.rect.w + 20, self.rect.h + 20), pygame.SRCALPHA)
            overlay.fill((255, 255, 255, 100))
            screen.blit(overlay, (self.rect.x - 10, self.rect.y - 10))
        
    def collide(self, other: Union["Rect", list, tuple, V2]):
        if type(other) == Rect: return self.rect.colliderect(other.rect)
        elif (type(other) == tuple) or (type(other) == list) or (type(other) == V2): return self.rect.collidepoint(other)
        else: return False
        
    @classmethod
    def random(cls, W=800, H=600):
        l = random.randint(0, W-100)
        t = random.randint(0, H-100)
        w = random.randint(20,100)
        h = random.randint(20,100)
        return Rect(l,t,w,h)
            

def lerp(val, xmin, xmax, ymin, ymax):
    if xmax - xmin == 0: return ymin
    return ymin + (val - xmin) * (ymax - ymin) / (xmax - xmin)


def perlin_noise(given: V2, grid_scale = 10, seed=12345) -> float:
    def get_gradient(x, y):
        random.seed((x * seed**2 + y * seed + seed))
        angle = random.uniform(0, 2*pi)
        return V2(cos(angle), sin(angle))
    
    t_fade = lambda t: (t**3) * (t * (6 * t - 15) + 10)  # Smooth fade function

    # noramlise (sorta) the given (aka make it a float)
    if isinstance(grid_scale, V2): given = V2(given.x/grid_scale.x, given.y/grid_scale.y)
    else: given /= grid_scale
    
    # Grid cell corners
    bl = V2(int(given.x), int(given.y))
    br = bl + V2(1, 0)
    tl = bl + V2(0, 1)
    tr = bl + V2(1, 1)

    # Gradients at each corner
    grads_bl = get_gradient(bl.x, bl.y)
    grads_br = get_gradient(br.x, br.y)
    grads_tl = get_gradient(tl.x, tl.y)
    grads_tr = get_gradient(tr.x, tr.y)
    
    # Displacement vectors
    disp_bl = given - bl
    disp_br = given - br
    disp_tl = given - tl
    disp_tr = given - tr

    # Dot products
    dot_bl = grads_bl.dot(disp_bl)
    dot_br = grads_br.dot(disp_br)
    dot_tl = grads_tl.dot(disp_tl)
    dot_tr = grads_tr.dot(disp_tr)
    
    # Fade values
    tx = (given.x - bl.x) / (br.x - bl.x)
    if (tr.y == tl.y): ty = (given.y - bl.y)    
    else: ty = ((given.y - tl.y) / (tr.y - tl.y))
    
    tx = t_fade(tx)
    ty = t_fade(ty)
    
    # Interpolation
    inter_x1 = (1 - tx) * dot_bl + tx * dot_br
    inter_x2 = (1 - tx) * dot_tl + tx * dot_tr
    final_val = (1 - ty) * inter_x1 + ty * inter_x2
    
    return (final_val + 1) / 2
