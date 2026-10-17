
import pygame
from pygame import Vector2 as V2
import re
from pathlib import Path

def natural_key(path: Path): return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", path.name)]


class Timer:
    def __init__(self, duration: float, repeat: bool):
        '''duration in seconds'''
        self.start_time = 0
        self.duration = duration * 1000
        self.repeat = repeat
        self.active = False

    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def update(self) -> bool:
        if self.active:
            if pygame.time.get_ticks() - self.start_time >= self.duration:
                if self.repeat:
                    self.start_time += self.duration
                else:
                    self.active = False
                return True
        return False

    

class Animation_player:

    @classmethod
    def load_frames_atlas_grid(cls, path: str, grid_width: int, grid_height: int) -> list[pygame.Surface]:
        '''load frames from grid atlas, only suitable if entire image only contains ordered sprites for one single animation. only png, jpg/jpeg, webp. grid size is '''
        base_image = pygame.image.load(path).convert_alpha()
        cell_size = V2(base_image.width // grid_width, base_image.height // grid_height)
        return [ base_image.subsurface(pygame.Rect(x*cell_size.x, y*cell_size.y, cell_size.x, cell_size.y)).copy() for y in range(grid_height) for x in range(grid_width) ]

    @classmethod
    def load_frames(cls, path: str) -> list[pygame.Surface]:
        '''load frames from individual images in a folder'''
        folder = Path(path)
        files = sorted((file for file in folder.iterdir() if file.is_file() and file.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'}), key=natural_key)
        return [ pygame.image.load(str(file)).convert_alpha() for file in files ]

    def __init__(self, fps: int, total_frames: int, loop: bool, reverse = False):
        self.index = 0
        self.total_frames = total_frames
        self.timer = Timer(1 / fps, loop)
        self.iter = -1 if reverse else 1

    def start(self):
        self.timer.start()

    def update(self) -> bool :
        '''True -> animation active, False -> animation inactive'''
        if self.timer.update():
            if self.timer.active or self.timer.repeat:
                self.index = (self.index + self.iter + self.total_frames) % self.total_frames
        return self.timer.active
