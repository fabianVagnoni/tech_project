import pygame

# List of characters with their names and corresponding image file paths
characters = [
    {"name": "Chef A", "image": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\chef_a.png"},
    {"name": "Chef B", "image": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\chef_b.png"},
    {"name": "Chef C", "image": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\chef_c.png"}
]

def get_character_images():
    # Load and return images for each character
    images = []
    for char in characters:
        try:
            image = pygame.image.load(char["image"])
            images.append(image)
        except pygame.error:
            print(f"Unable to load image for {char['name']}")
            images.append(None)  # Placeholder if image fails to load
    return images
