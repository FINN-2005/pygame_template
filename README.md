# `pygame_template`  

This is my Pygame wrapper designed to make creative coding easier.  

## Why It's Here  

It's only here to make my own life easier, after years of creative coding in python and pygame, I just kept noticing little modules of practical implementations that I always implemented.  
So I just bundled them together and added some new cool utilities.  
And boy is it useful, I have literally used this to make:  
- rendering pipelines  
- multiplayer / singleplayer games  
- physics simulations  
- even V2 of pygame_template itself! (currently in the works)  

It has made my coding journey into an enjoyable hobby.  
With this, I was able to focus on the actual complex details of the project rather than thinking about how I was going to show stuff on the screen.  

## Installation  

### Install directly with Git.  
```bash
pip install git+https://github.com/FINN-2005/pygame_template.git
```

### Otherwise:  

- Clone the repo or download and extract the zip file  
    ```bash
    git clone https://github.com/FINN-2005/pygame_template.git
    ```
- **Navigate to the Directory:** Step into the newly created folder.  
    ```bash
    cd pygame_template
    ```
- **Install the Package:** Use pip to install the framework. The `.` tells pip to look for the `setup.py` file in the current directory.  
    ```bash
    pip install .
    ```

## Code Examples  

All you need to get started is just import everything and call the main `APP` class.  
```python
from pygame_template import *

APP()
```

That's literally it!  
This gives you a basic window (1280x720) with FPS as the window title,  

To get more, inherit the class APP (i usually name them run)

```python
from pygame_template import *

class run(APP):
    def init(self):
        ...
        
    def setup(self):
        ...

    def draw(self):
        ...

    def update(self):
        ...

    def first_update(self):
        ...

    def event(self, e):
        ...

    def tick(self, dt):
        ...


run()
```
This gives you full control over every feature i abstracted away but still in a not-a-boilerplate sort of fashion.  

### Small summaries of the functions:  
- **init(self)**:  
    It runs before setup, used to initialise things like window width and height, whether to use full screen or not, whether to use the built in tick system or not, setting the tick rate, etc.  
- **setup(self)**:  
    It is exactly as it sounds, it is called automatically once after everything is initialised, use it for code that needs to run once.  

- **draw(self)**:  
    I separated draw and update for personal choices, runs every frame.  (you can completely ignore this and draw from update too!)

- **update(self)**:  
    I separated draw and update for personal choices, runs every frame.  
    
- **first_update(self)**:  
    This also runs once but just before update. (Note: Update is still called after this on the same frame)  

- **event(self, e)**:     
    The event loop, called per new event per frame.  

- **tick(self, dt)**:  
    Works when using the built-in Tick system, get's called every tick (specified by the tick rate), `dt` is delta time since last tick

### Some Useful Class Attributes  

- `self.screen` (main screen surface)  
- `self.dt` (main delta time, set automatically, use whenever, wherever)  

and a lot more very useful class attributes and other global utility functions and classes that I don't have enough time to list them all here at this time.  

---

## Projects Built Using This Framework  

- [Genetic Algorithm Training Environment](https://github.com/FINN-2005/Genetic-Algo-Training-Environment)
- [2D Collisions](https://github.com/FINN-2005/2D-Collisions)
- [Stars](https://github.com/FINN-2005/Stars)
- [Pi Visualization Sim](https://github.com/FINN-2005/Pi-Visualization-Sim)
- [Spring Particle Sim (V2)](https://github.com/FINN-2005/Spring-Particles-Sim-V2)
- [Spring-Particles-Physics-Collision](https://github.com/FINN-2005/Spring-Particles-Physics-Collision)
- [CNC ToolPath Generator](https://github.com/FINN-2005/CNC-Toolpath-Gen)
- [Shorts Brain Rot Cool](https://github.com/FINN-2005/Shorts-Brain-Rot-Cool)
- [Wave Function Collapse (Overlapping)](https://github.com/FINN-2005/Wave-Function-Collapse-Overlapping)
- [Wave Function Collapse (Tiled)](https://github.com/FINN-2005/Wave-Function-Collapse-Tiled)
- [Tic Tac Toe Multiplayer](https://github.com/FINN-2005/Tic-Tac-Toe-Multiplayer)
- [Game of Life (V2)](https://github.com/FINN-2005/Game-Of-Life-V2)
- [Snake Clone](https://github.com/FINN-2005/Snake-Clone)
- [Flappy Bird Clone](https://github.com/FINN-2005/Flappy-Bird-Clone)
- [Software Pixel Renderer](https://github.com/FINN-2005/Software-Pixel-Renderer)
- [CorkBoard Planner](https://github.com/FINN-2005/CorkBoard-Planner)

---

## Further Documentation  
`¯\_(ツ)_/¯` (WIP - Look at Code Examples)  
