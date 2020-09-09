"""
A library of functions that operate the very highest menu of the game
"""

import main_menu_ui


# Activates the button that moves from the top menu to the next menu
def start_game_button(menu):
    if menu.button == 1:
        if main_menu_ui.start_game_rect.collidepoint(menu.pos):
            menu.top_menu = False
            menu.button = 0
            menu.main_menu = True
            
# Draws a blank black background for the top menu    
def draw_background(menu, screen):
    screen.fill((0,0,0))

# Draws the Start Game option for the top menu
def draw_options(menu, screen):
    screen.blit(main_menu_ui.start_game, main_menu_ui.start_game_rect)