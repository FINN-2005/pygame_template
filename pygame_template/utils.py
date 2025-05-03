import pygame
import random
from typing import Union
from pygame import Vector2 as V2
from pygame import Vector3 as V3


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
    def __init__(self, *sprites):
        super().__init__(*sprites)
        
        self.screen = pygame.display.get_surface()

    def draw(self):
        for spr in self.sprites():
            if hasattr(spr, 'draw') and callable(getattr(spr, 'draw')): spr.draw(self.screen)
            else: self.screen.blit(spr.image, spr.rect)
        
    def __getattr__(self, name):
        def forwarder(*args, **kwargs):
            return_values = []
            for spr in self.sprites():
                method = getattr(spr, name, None)
                if callable(method):
                    return_values.append(method(*args, **kwargs))
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
            