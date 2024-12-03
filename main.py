import pygame
import sys
import random

# CONSTANTS
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TEXT_TO_RECT_SPACING = 10
FPS_SETTINGS_Y = 425
CHANCE_OF_SOUND_PER_FRAME_Y = 500
BUTTON_SELECTION_BORDER_WIDTH = 10

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

# BUTTON CLASS
def __init__(self, text, x, y, font, color, action=None):
    self.text = text
    self.font = font
    self.color = color
    self.action = action
    self.center_x = x
    self.center_y = y
    self.update_text(text)

def update_text(self, new_text):
    self.text = new_text
    self.text_surface = self.font.render(self.text, True, WHITE)
    self.rect = pygame.Rect(
        self.center_x - (self.text_surface.get_width() / 2) - TEXT_TO_RECT_SPACING,
        self.center_y - (self.text_surface.get_height() / 2) - TEXT_TO_RECT_SPACING,
        self.text_surface.get_width() + (TEXT_TO_RECT_SPACING * 2),
        self.text_surface.get_height() + (TEXT_TO_RECT_SPACING * 2)
    )

def draw(self, screen, selected=False):
    if selected:
        pygame.draw.rect(
            screen, WHITE,
            self.rect.inflate(BUTTON_SELECTION_BORDER_WIDTH * 2, BUTTON_SELECTION_BORDER_WIDTH * 2)
        )
    pygame.draw.rect(screen, self.color, self.rect)
    screen.blit(
        self.text_surface,
        (self.rect.x + TEXT_TO_RECT_SPACING, self.rect.y + TEXT_TO_RECT_SPACING)
    )

def check_collision(self, mouse_pos):
    return self.rect.collidepoint(mouse_pos)

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
    manager = ScreenManager()

    manager.add_screen("main_menu", MainMenuScreen(manager))
    manager.add_screen("sound_player", SoundPlayerScreen(manager))

    manager.set_active_screen("main_menu")

    # MAIN LOOP
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        manager.handle_events(events)
        manager.update()
        manager.render(screen)

        pygame.display.flip()
        clock.tick(settings['fps'])

if __name__ == "__main__":
    main()