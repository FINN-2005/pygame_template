import pygame

class Input_manager:

    INPUT_MAP = {
        'up'    : [pygame.K_w, pygame.K_UP],
        'down'  : [pygame.K_s, pygame.K_DOWN],
        'left'  : [pygame.K_a, pygame.K_LEFT],
        'right' : [pygame.K_d, pygame.K_RIGHT],
        'space' : [pygame.K_SPACE],
        'click' : [pygame.BUTTON_LEFT]
    }

    INPUTS = { key: 0 for key in INPUT_MAP.keys() }     # 000 -> clean, 001 -> just released, 010 -> just pressed, 100 -> pressed

    KEYMAP = { key : button for button, keys in INPUT_MAP.items() for key in keys }

    PRESSED = 4         # 100
    JUST_PRESSED = 2    # 010
    JUST_RELEASED = 1   # 001

    def __init__(self, app):
        self.app = app
        self.app.use_input_system = True
        self.app._input_manager = self

    def _event(self, e):
        if e.type in (pygame.KEYDOWN, pygame.KEYUP):
            if (action := self.KEYMAP.get(e.key)) is None: return
            state = self.INPUTS[action]

            if e.type == pygame.KEYDOWN and not (state & self.PRESSED):
                self.INPUTS[action] |= self.PRESSED | self.JUST_PRESSED

            elif e.type == pygame.KEYUP and (state & self.PRESSED):
                self.INPUTS[action] &= ~(self.PRESSED | self.JUST_PRESSED)
                self.INPUTS[action] |= self.JUST_RELEASED

        else:
            if (action := self.KEYMAP.get(e.button)) is None: return
            state = self.INPUTS[action]

            if e.type == pygame.MOUSEBUTTONDOWN and not (state & self.PRESSED):
                self.INPUTS[action] |= self.PRESSED | self.JUST_PRESSED
            
            elif e.type == pygame.MOUSEBUTTONUP and (state & self.PRESSED):
                self.INPUTS[action] &= ~(self.PRESSED | self.JUST_PRESSED)
                self.INPUTS[action] |= self.JUST_RELEASED

    def _update(self):
        for key in self.INPUTS:
            self.INPUTS[key] &= self.PRESSED

    def is_pressed(self, key: int):       return self.INPUTS[key] & self.PRESSED
    def is_just_pressed(self, key: int):  return self.INPUTS[key] & self.JUST_PRESSED
    def is_just_released(self, key: int): return self.INPUTS[key] & self.JUST_RELEASED

    def add_action(self, action: str, keys: int | tuple | list):
        if action in self.INPUT_MAP: self.INPUT_MAP[action] += list(keys) if isinstance(keys, (tuple, list)) else [keys]
        else: self.INPUT_MAP[action] = list(keys) if isinstance(keys, (tuple, list)) else [keys]
        self.INPUTS = { key: 0 for key in self.INPUT_MAP.keys() }
        self.KEYMAP = { key : button for button, keys in self.INPUT_MAP.items() for key in keys }

    def remove_action(self, action: str):
        self.INPUT_MAP.pop(action, None)
        self.INPUTS = {key: 0 for key in self.INPUT_MAP}
        self.KEYMAP = {key: button for button, keys in self.INPUT_MAP.items() for key in keys}

    def update_action(self, action: str, keys: int | tuple | list):
        if action not in self.INPUT_MAP:
            self.add_action(action, keys)
        else:
            self.INPUT_MAP[action] = list(keys) if isinstance(keys, (tuple, list)) else [keys]
            self.INPUTS = {key: 0 for key in self.INPUT_MAP}
            self.KEYMAP = {key: button for button, keys in self.INPUT_MAP.items() for key in keys}

    def update_input_map(self, input_map: dict[str, list[int]]):
        self.INPUT_MAP = input_map
        self.INPUTS = {key: 0 for key in self.INPUT_MAP}
        self.KEYMAP = {key: button for button, keys in self.INPUT_MAP.items() for key in keys}
