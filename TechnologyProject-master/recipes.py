import pygame

# List of characters with their names and corresponding image file paths
recipes = [
    {"name": "Recipe A", "image": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\recipe_1.png" ,
     "coldIngredients" : "Eggs, Butter & Milk" , "dryIngredients" : "Flour, Baking Powder, Salta & Sugar or Sweetner",
     "cIng1" : r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_1.webp", 
     "cIng2": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_2.webp", 
     "cIng3" : r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_3.webp"},

    {"name": "Recipe B", "image": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\recipe_2.png",
     "coldIngredients" : "Eggs, Butter & Milk" , "dryIngredients" : "Flour, Baking Powder, Salta & Sugar or Sweetner",
     "cIng1" : r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_1.webp", 
     "cIng2": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_2.webp", 
     "cIng3" : r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_3.webp"},

    {"name": "Recipe C", "image": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\recipe_3.png",
     "coldIngredients" : "Eggs, Butter & Milk" , "dryIngredients" : "Flour, Baking Powder, Salta & Sugar or Sweetner",
     "cIng1" : r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_1.webp", 
     "cIng2": r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_2.webp", 
     "cIng3" : r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\cold_ing_3.webp"}
]

def get_recipe_images():
    # Load and return images for each character
    images = []
    for r in recipes:
        try:
            image = pygame.image.load(r["image"])
            images.append(image)
        except pygame.error:
            print(f"Unable to load image for {r['name']}")
            images.append(None)  # Placeholder if image fails to load
    return images