import pygame
import main

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Cooking Game")

    main.game_loop(screen)

if __name__ == '__main__':
    run_game()