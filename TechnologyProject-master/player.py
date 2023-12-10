import pygame


class Player:
    def __init__(self, x, y, character_image_path, size=(128, 128)):
        self.x = x
        self.y = y
        self.image = pygame.image.load(character_image_path)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        original_image = pygame.image.load(character_image_path)
        self.image = pygame.transform.scale(original_image, size)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def update(self, direction):
        if direction == 'up':
            self.y -= 3
        elif direction == 'down':
            self.y += 3
        elif direction == 'left':
            self.x -= 3
        elif direction == 'right':
            self.x += 3
        # Update rect for collision detection
        self.rect.topleft = (self.x, self.y)
