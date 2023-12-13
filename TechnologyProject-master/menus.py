import pygame

import pygame
import characters
import recipes


# Slider class for volume adjustment
class Slider:
    def __init__(self, x, y, width, height, min_value, max_value, initial_value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value

    def draw(self, surface):
        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        pygame.draw.rect(surface, white, (self.x, self.y, self.width, self.height))
        percentage = (self.value - self.min_value) / (self.max_value - self.min_value)
        slider_x = int(self.x + percentage * self.width)
        pygame.draw.rect(surface, red, (slider_x - 5, self.y, 10, self.height))

    def update_value(self, new_x):
        percentage = (new_x - self.x) / self.width
        self.value = self.min_value + percentage * (self.max_value - self.min_value)
        pygame.mixer.music.set_volume(self.value)


def draw_button(screen, text, font, button_color, text_color, x, y, width, height):
    # Draw button rectangle
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, button_color, button_rect)

    # Render the text
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=button_rect.center)

    # Blit the text onto the screen
    screen.blit(text_surface, text_rect)

    return button_rect


def show_start_menu(screen, button_color):
    # Define colors
    button_color = (100, 100, 100)  # Gray color for button
    text_color = (255, 255, 255)    # White color for text
    background_color = (0, 0, 0)     # Black color for background

    # Fill background
    screen.fill(background_color)

    # Set up font
    font = pygame.font.Font(None, 49)  # You can replace None with a font file path

    # Define button properties
    button_width = 200
    button_height = 50
    button_x = 300#(screen.get_width() - button_width) / 2
    button_y = 200#(screen.get_height() - button_height) / 2

    # Draw the button and get its rect
    button_rect = draw_button(screen, "Start Game", font, button_color, text_color, button_x, button_y, button_width, button_height)

    volume_slider = Slider(300, 350, 200, 20, 0, 1, pygame.mixer.music.get_volume())
    volume_slider.draw(screen)
    volume_button = draw_button(screen, "Volume", font, button_color, text_color, 300, 300, 200, 50)
    return button_rect, volume_slider, volume_button


def draw_text_centered(screen, text, font, color, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(screen.get_width() / 2, y))
    screen.blit(text_surface, text_rect)


def load_and_scale_image(image_path, width, height):
    try:
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (width, height))
        return image
    except pygame.error as e:
        print(f"Error loading image {image_path}: {e}")
        return None


def show_character_menu(screen):
    font = pygame.font.SysFont(None, 55)
    color_black = (0, 0, 0)
    draw_text_centered(screen, 'Choose Character', font, color_black, 50)

    char_images = [load_and_scale_image(char["image"], 100, 100) for char in characters.characters]
    button_rects = []

    for i, img in enumerate(char_images):
        if img is not None:
            x = 200 + i * (100 + 10)  # 100px image width + 10px padding
            y = 200  # Fixed y position for all character images
            screen.blit(img, (x, y))
            rect = pygame.Rect(x, y, 100, 100)  # Assuming images are scaled to 100x100
            button_rects.append(rect)
        else:
            # Handle the case when the image is None
            print(f"Image for character {characters.characters[i]['name']} is not available.")

    return button_rects


def show_recipe_menu(screen):
    font = pygame.font.SysFont(None, 55)
    color_black = (0, 0, 0)
    draw_text_centered(screen, 'Choose Recipe', font, color_black, 50)

    recipe_images = [load_and_scale_image(recipe["image"], 100, 100) for recipe in recipes.recipes]
    button_rects = []

    for i, img in enumerate(recipe_images):
        if img is not None:
            x = 200 + i * (100 + 10)  # 100px image width + 10px padding
            y = 200  # Fixed y position for all recipe images
            screen.blit(img, (x, y))
            rect = pygame.Rect(x, y, 100, 100)  # Assuming images are scaled to 100x100
            button_rects.append(rect)
        else:
            # Handle the case when the image is None
            print(f"Image for recipe {recipes.recipes[i]['name']} is not available.")

    return button_rects



def show_cold_ingredients(screen , choosen_recipe):
    cIngImages = []
    for r in recipes.recipes:
        if r == choosen_recipe:
            cIngImages.append(load_and_scale_image(r["cIng1"], 35, 35))
            cIngImages.append(load_and_scale_image(r["cIng2"], 35, 35))
            cIngImages.append(load_and_scale_image(r["cIng3"], 35, 35))

    for i, img in enumerate(cIngImages):
        if img is not None:
            x = 300 + i * (10)  # 100px image width + 10px padding
            y = 230  # Fixed y position for all recipe images
            screen.blit(img, (x, y))
        else:
            # Handle the case when the image is None
            print(f"Image for recipe {recipes.recipes[i]['name']} is not available.")


def show_dry_ingredients(screen , choosen_recipe):
    dIngImages = []
    for r in recipes.recipes:
        if r == choosen_recipe:
            dIngImages.append(load_and_scale_image(r["dIng1"], 35, 35))
            dIngImages.append(load_and_scale_image(r["dIng2"], 35, 35))
            dIngImages.append(load_and_scale_image(r["dIng3"], 35, 35))

    for i, img in enumerate(dIngImages):
        if img is not None:
            x = 300 + i * (10)  # 100px image width + 10px padding
            y = 230  # Fixed y position for all recipe images
            screen.blit(img, (x, y))
        else:
            # Handle the case when the image is None
            print(f"Image for recipe {recipes.recipes[i]['name']} is not available.")




