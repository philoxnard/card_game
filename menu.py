"""
A collection of code that represents the top menus that the player can navigate
through before the actual card game begins.
"""

import pygame

import top_menu
import main_menu
import deck_select

class Menu():
    
    # Initialize the main menu statuses
    def __init__(self):
        self.button = None
        self.start_game = False
        self.top_menu = True
        self.main_menu = False
        self.how_to_play = False
        self.deck_select = False
        self.player_select = 1
    
    # Highest level logic for how the main menu screens operate
    def run(self, screen):
        self.get_user_input()
        if self.top_menu:
            self.run_top_menu(screen)
        if self.main_menu:
            self.run_main_menu(screen)
        if self.how_to_play:
            main_menu.rule_descriptions(self, screen)
        if self.deck_select:
            self.run_deck_select(screen)
    
    # First chunk of code that runs when the game is initiated
    def run_top_menu(self, screen):
        top_menu.start_game_button(self)
        top_menu.draw_background(self, screen)
        top_menu.draw_options(self, screen)
    
    # Chunk of code that runs when the player is in the main menu
    def run_main_menu(self, screen):
        main_menu.draw_background(self, screen)
        main_menu.draw_options(self, screen)
        main_menu.hot_seat_button(self)
        main_menu.how_to_play_button(self)
        
    # Chunk of code that runs when the player is selecting their deck
    def run_deck_select(self, screen):
        deck_select.draw_background(self, screen)
        deck_select.draw_deck_options(self, screen)
        deck_select.select_aggro_deck(self)
        deck_select.select_ramp_deck(self)
        
    # Functions that constantly run to check the player's input and allow the
    # user to quit
    def get_user_input(self):
        self.button = self.get_event_button()
        self.quit_game(self.button)
        self.get_mouse_pos()
    
    # Gets the mouse position during the menu screens
    def get_mouse_pos(self):
        self.pos = pygame.mouse.get_pos()
        
    # Checks for mouse clicks and keyboard presses
    def get_event_button(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return 1
                elif event.button == 3:
                    return 3
            if event.type == pygame.QUIT:
                return "q"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return "q"
                
    # Quits the game on a Q press or a system exit
    def quit_game(self, button):
        if button == "q":
            pygame.quit()

    