import pygame


class Level:
    def __init__(self, map_image_path, scale_factor=2):
        original_image = pygame.image.load(map_image_path)
        original_size = original_image.get_size()
        scaled_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        self.map_image = pygame.transform.scale(original_image, scaled_size)

    def draw(self, screen):
        screen.blit(self.map_image, (60, 0))  # Drawing the map at the origin
