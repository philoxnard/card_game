"""A library of functions that represent the main menu"""

import main_menu_ui

# Draws a blank black background for the top menu    
def draw_background(menu, screen):
    screen.fill((0,0,0))

# Draws the Start Game option for the top menu
def draw_options(menu, screen):
    screen.blit(main_menu_ui.how_to_play, main_menu_ui.how_to_play_rect)
    screen.blit(main_menu_ui.play_vs_cpu, main_menu_ui.play_vs_cpu_rect)
    screen.blit(main_menu_ui.hot_seat, main_menu_ui.hot_seat_rect)
    screen.blit(main_menu_ui.play_online, main_menu_ui.play_online_rect)
    
def rule_descriptions(menu, screen):
    screen.fill((0,0,0))
    screen.blit(main_menu_ui.rule_descriptions, main_menu_ui.rule_descriptions_rect)
    if menu.button == 1:
        menu.main_menu = True
        menu.button = 0
        menu.how_to_play = False
       
def how_to_play_button(menu):
    if menu.button == 1:
        if main_menu_ui.how_to_play_rect.collidepoint(menu.pos):
            menu.main_menu = False
            menu.button = 0
            menu.how_to_play = True
    
def hot_seat_button(menu):
    if menu.button == 1:
        if main_menu_ui.hot_seat_rect.collidepoint(menu.pos):
            menu.main_menu = False
            menu.button = 0
            menu.deck_select = True