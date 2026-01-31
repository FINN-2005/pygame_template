import pygame
from pygame_template.colors import Color
from pygame import Vector2 as V2
from pygame import Vector3 as V3


import ctypes
ctypes.windll.user32.SetProcessDPIAware()

class APP:
    W,H = 1280,720
    HW, HH = W//2, H//2
    FPS = 120
    INSTANCE = None
    def __init__(self):
        
        self.limit_fps = False
        self.no_clear = False
        self.FPS = APP.FPS
        self.WIDTH = APP.W
        self.HEIGHT = APP.H
        self.FULLSCREEN = False
        self.bg_col = Color.gray18
        self.window_title = 'fps'
        self.dt_speed_factor = 100
        APP.INSTANCE = self

        # ========== T I C K   S Y S T E M ==========
        self.use_tick_system = False
        self.prev_time_ticks = pygame.time.get_ticks()
        self.TICK_RATE = 40

        self.init()

        self.TICK_EVENT = pygame.USEREVENT + 1
        self.TICK_TIME = int(1000 / self.TICK_RATE)
        pygame.time.set_timer(self.TICK_EVENT, self.TICK_TIME)
        
        self.HW = self.WIDTH / 2
        self.HH = self.HEIGHT / 2
        APP.HW, APP.HH = self.HW, self.HH
        APP.W, APP.H = self.WIDTH, self.HEIGHT
        self.RES = self.WIDTH, self.HEIGHT
        
        if self.FULLSCREEN: self.screen = pygame.display.set_mode(self.RES, pygame.SRCALPHA | pygame.FULLSCREEN)
        else: self.screen = pygame.display.set_mode(self.RES, pygame.SRCALPHA)
        self.clock = pygame.Clock()
        
        self.setup()
        self._first = True
        if self.use_tick_system: self.dt_speed_factor = 1
        self._run()
        
    def init(self):
        ...
                
    def setup(self):
        ...
        
    def event(self, e):
        ...
        
    def draw(self):
        ...

    def first_update(self):
        ...

    def tick(self, dt):
        ...

    def update(self):
        ...

    def _run(self):
        self.running = True
        while self.running:
            
            if self.limit_fps: self.dt = self.dt_speed_factor*self.clock.tick(self.FPS)/1000
            else: self.dt = self.dt_speed_factor*self.clock.tick()/1000
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
                if self.use_tick_system and (event.type == self.TICK_EVENT):
                    dt = (self.TICK_TIME / 1000) * self.dt_speed_factor
                    self.prev_time_ticks = pygame.time.get_ticks()
                    self.tick(dt)
                self.event(event)
                    
            if self._first:
                self.prev_time_ticks = pygame.time.get_ticks()
                # self.screen.fill(self.bg_col)
                self.first_update()
                self._first = False
            if not self.no_clear:
                self.screen.fill(self.bg_col)
            
            now = pygame.time.get_ticks()
            self.tick_alpha = min((now - self.prev_time_ticks) / self.TICK_TIME, 1)

            self.update()
            self.draw()
            if self.window_title == 'fps': 
                pygame.display.set_caption(f'FPS: {self.clock.get_fps()//1}')
            else:
                pygame.display.set_caption(self.window_title)
            
            pygame.display.flip()
            

