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

# SPECIFIC SCREEN CLASSES

# SCREEN MANAGER CLASS

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