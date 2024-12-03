import pygame
import sys
import random

# CONSTANTS
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# PYGAME INITIALIZATIONS
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# VARIABLE INITALIZATIONS
settings = {
    'fps': 60,
    'one_in_chance_of_sound_per_frame': 60,
}

# HELPER FUNCTION
def mouse_in_rect(mouse_pos, rect):
    rect_x, rect_y, rect_width, rect_height = rect
    mouse_x, mouse_y = mouse_pos
    if ((rect_x + rect_width >= mouse_x >= rect_x) and
        (rect_y + rect_height >= mouse_y >= rect_y)):
        return True
    return False

# BASE SCREEN CLASS
class Screen:
    def __init__(self, screen_manager):
        self.manager = screen_manager

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

# SPECIFIC SCREEN CLASSES
class MainMenuScreen(Screen):
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        pass

    def handle_events(self, events):
        pass

    def render(self, screen):
        pass

    def exit_to_sound_player(self):
        pass

class SoundPlayerScreen(Screen):
    def __init__(self, screen_manager):
        super().__init__(screen_manager)
        pass
    
    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

    def exit_to_main_menu(self):
        pass

# SCREEN MANAGER CLASS
class ScreenManager:
    def __init__(self):
        self.screens = {}
        self.active_screen = None

    def add_screen(self, name, screen):
        self.screens[name] = screen

    def set_active_screen(self, name):
        self.active_screen = self.screens[name]

    def handle_events(self, events):
        if self.active_screen:
            self.active_screen.handle_events(events)

    def update(self):
        if self.active_screen:
            self.active_screen.update()

    def render(self, screen):
        if self.active_screen:
            self.active_screen.render(screen)

# MAIN FUNCTION
def main():

    # MAIN LOOP
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(settings['fps'])

if __name__ == "__main__":
    main()