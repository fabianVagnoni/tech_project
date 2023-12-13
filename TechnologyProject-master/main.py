import pygame
from player import Player
from level import Level
from menus import show_start_menu, show_character_menu, show_recipe_menu, show_cold_ingredients, show_dry_ingredients, load_and_scale_image
import characters
import recipes

# Constants for game states
START_MENU = 'start_menu'
CHARACTER_SELECTION = 'character_selection'
RECIPE_SELECTION = "recipe_selection"
MAIN_GAME = 'main_game'
MAIN_GAME_COOKING = "cooking"


def game_loop(screen):
    recipe_text_font = pygame.font.Font(None, 20)
    clock = pygame.time.Clock()
    running = True
    current_state = START_MENU
    start_button_rect = None  # This will be set by the show_start_menu function
    character_button_rects = []
    button_color = (100, 100, 100)  # Default button color
    kitchen_level = Level(r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\map1.png", scale_factor=3)  # Replace with actual path
    cooking_level = Level(r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\bowl.png" , scale_factor=1.4)
    player_character = None
    character_selected = False
    pygame.mixer.music.load(r"C:\Users\Usuario\Downloads\TechnologyProject-master\music\menu_music.mp3")
    pygame.mixer.music.set_volume(0.5)  # Initial volume
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely
    cold_ingredients_grabbed = False
    dry_ingredients_grabbed = False
    cold_ingredients_left = False
    dry_ingredients_left = False
    wet_ing = False
    mix_wet = False
    dry_ing = False
    mix_dry = False
    first_time = False
    img_rotated = False
    Ing_sprites = pygame.sprite.Group()

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if start_button_rect is not None before using collidepoint
                if current_state == START_MENU and start_button_rect and start_button_rect.collidepoint(event.pos):
                    current_state = CHARACTER_SELECTION
                elif current_state == CHARACTER_SELECTION:
                    for idx, rect in enumerate(character_button_rects):
                        if rect.collidepoint(event.pos):
                            # Use the actual path from the characters list
                            character_image_path = characters.characters[idx]["image"]
                            player_character = Player(250, 250, character_image_path)
                            character_selected = True
                            current_state = RECIPE_SELECTION
                elif current_state == RECIPE_SELECTION:
                    for idx, rect in enumerate(recipe_button_rects):
                        if rect.collidepoint(event.pos):
                            # Use the actual path from the characters list
                            recipe = recipes.recipes[idx]
                            recipe_image_path = recipes.recipes[idx]["image"]
                            recipe_coldIngredients = recipes.recipes[idx]["coldIngredients"]
                            recipe_dryIngredients = recipes.recipes[idx]["dryIngredients"]
                            current_state = MAIN_GAME
                # Check if start_button_rect is not None before using collidepoint
                if current_state == START_MENU and start_button_rect and start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    button_color = (150, 150, 150)  # Lighter gray for hover
                else:
                    button_color = (100, 100, 100)  # Original gray color

        # Update game state
        screen.fill((255, 255, 255))  # Clear screen
        if current_state == START_MENU:
            start_button_rect , volume_slider = show_start_menu(screen, button_color)[0] , show_start_menu(screen, button_color)[1]
                # Check for volume slider interaction
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (
                    volume_slider.x <= mouse_x <= volume_slider.x + volume_slider.width
                    and volume_slider.y <= mouse_y <= volume_slider.y + volume_slider.height
                ):
                    volume_slider.update_value(mouse_x)
        elif current_state == CHARACTER_SELECTION:
            character_button_rects = show_character_menu(screen)
        elif current_state == RECIPE_SELECTION:
            recipe_button_rects = show_recipe_menu(screen=screen)
        elif current_state == MAIN_GAME:
            if character_selected:
                kitchen_level.draw(screen)
                if cold_ingredients_left:
                    show_cold_ingredients(screen , recipe)
                if dry_ingredients_left:
                    show_dry_ingredients(screen , recipe)
                player_character.draw(screen)

                if cold_ingredients_grabbed != True:
                    recipe_text = f"Go to the refrigerator to grab the {recipe_coldIngredients}"
                    recipe_text_surface = recipe_text_font.render(recipe_text, True, (0, 0, 0))  # (0, 0, 0) is black color
                    screen.blit(recipe_text_surface, (30, 550))  # Adjust the coordinates as needed

                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP] and player_character.y > 125:
                    player_character.update('up')
                if keys[pygame.K_DOWN] and player_character.y < 400:
                    player_character.update('down')
                if keys[pygame.K_LEFT] and player_character.x > 125:
                    player_character.update('left')
                if keys[pygame.K_RIGHT] and player_character.x < 420:
                    player_character.update('right')

                if 410 < player_character.x and 220 < player_character.y < 325 and cold_ingredients_grabbed != True:
                    grab_text = "Press <<X>> to grab the ingredients"
                    grab_text_surface = recipe_text_font.render(grab_text, True, (255, 0, 0),(255,255,255))  # (255, 0, 0) is red color
                    screen.blit(grab_text_surface, (10, 40))  # Adjust the coordinates as needed
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_x]:
                        cold_ingredients_grabbed = True
                        print("Ingredients grabbed!")
                        

                if cold_ingredients_grabbed and dry_ingredients_grabbed == False:
                    screen.fill(pygame.Color("white") , rect=pygame.Rect(10, 545 , 1000 , 30))
                    screen.fill((255, 255, 255), (10, 40, grab_text_surface.get_width(), grab_text_surface.get_height()))
                    recipe_text = "Now leave the ingredients in the shelve"
                    recipe_text_surface = recipe_text_font.render(recipe_text, True, (0, 0, 0))  # (0, 0, 0) is black color
                    screen.blit(recipe_text_surface, (30, 550))  # Adjust the coordinates as needed


                if 150 < player_character.x < 255 and 200 < player_character.y < 275 and cold_ingredients_left != True and cold_ingredients_grabbed:
                    leave_text = "Press <<Y>> to leave the ingredients in the shelve"
                    leave_text_surface = recipe_text_font.render(leave_text, True, (255, 0, 0),(255,255,255))  # (255, 0, 0) is red color
                    screen.blit(leave_text_surface, (10, 40))  # Adjust the coordinates as needed
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                        cold_ingredients_left = True
                        print("Ingredients grabbed!")


                if cold_ingredients_left and dry_ingredients_grabbed == False:
                    screen.fill(pygame.Color("white") , rect=pygame.Rect(10, 545 , 1000 , 30))
                    screen.fill((255, 255, 255), (10, 40, grab_text_surface.get_width(), grab_text_surface.get_height()))
                    recipe_text = f"Now go for the {recipe_dryIngredients}"
                    recipe_text_surface = recipe_text_font.render(recipe_text, True, (0, 0, 0))  # (0, 0, 0) is black color
                    screen.blit(recipe_text_surface, (30, 550))  # Adjust the coordinates as needed


                if 300 < player_character.x < 400 and 150 < player_character.y < 250 and dry_ingredients_grabbed != True and cold_ingredients_left:
                    grab_text = "Press <<X>> to grab the ingredients"
                    grab_text_surface = recipe_text_font.render(grab_text, True, (255, 0, 0),(255,255,255))  # (255, 0, 0) is red color
                    screen.blit(grab_text_surface, (10, 40))  # Adjust the coordinates as needed
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_x]:
                        dry_ingredients_grabbed = True
                        print("Ingredients grabbed!")

                if dry_ingredients_grabbed:
                    screen.fill(pygame.Color("white") , rect=pygame.Rect(10, 545 , 1000 , 30))
                    screen.fill((255, 255, 255), (10, 40, grab_text_surface.get_width(), grab_text_surface.get_height()))
                    recipe_text = f"Now leave the ingredients in the shelve"
                    recipe_text_surface = recipe_text_font.render(recipe_text, True, (0, 0, 0))  # (0, 0, 0) is black color
                    screen.blit(recipe_text_surface, (30, 550))  # Adjust the coordinates as needed

                if 150 < player_character.x < 255 and 200 < player_character.y < 275 and dry_ingredients_left != True and dry_ingredients_grabbed:
                    leave_text = "Press <<Y>> to leave the ingredients in the shelve"
                    leave_text_surface = recipe_text_font.render(leave_text, True, (255, 0, 0),(255,255,255))  # (255, 0, 0) is red color
                    screen.blit(leave_text_surface, (10, 40))  # Adjust the coordinates as needed
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_y]:
                        dry_ingredients_left = True
                        print("Ingredients grabbed!")
                        current_state = MAIN_GAME_COOKING

        elif current_state == MAIN_GAME_COOKING:
            if not wet_ing:
                if not first_time:
                    wIng1 = pygame.sprite.Sprite()
                    wIng1.image = load_and_scale_image(recipe["cIng1"], 70, 70)
                    wIng1.rect = wIng1.image.get_rect()
                    wIng1.rect.topleft = (450, 100)
                    Ing_sprites.empty()  # Remove previous sprite
                    Ing_sprites.add(wIng1)
                    first_time = True

                cooking_level.draw(screen)
                Ing_sprites.draw(screen)

                recipe_text = "Click on the ingredient to pour it in the bowl"
                recipe_text_surface = recipe_text_font.render(recipe_text, True, (0, 0, 0))
                screen.blit(recipe_text_surface, (30, 550))

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if wIng1.rect.collidepoint(mouse_x, mouse_y):
                        wIng1.image = pygame.transform.rotate(wIng1.image, +90)
                        wIng1.rect = wIng1.image.get_rect(topleft=wIng1.rect.topleft)
                        img_rotated = True
                elif event.type == pygame.QUIT:
                    running = False
            
            if img_rotated:
                    cooking_level.change_image(r"C:\Users\Usuario\Downloads\TechnologyProject-master\sprites\bowl_2.png" , scale_factor=1.4)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
