import pygame


import game_ui
from board import Board
from menu import Menu

def run_game():
    # Initialize pygame, board, and menu
    pygame.init()
    board = Board()
    menu = Menu()
    
    # Highest level logic loop for the game
    while True:
        # handle errors to gracefully quit the pygame app
        try:
            if menu.start_game == False:
                menu.run(game_ui.screen)
            else:
                board.play_game(game_ui.screen_height, game_ui.screen)
            # Flip the display
            pygame.display.flip()
        except Exception as e:
            pygame.quit()
            raise e
run_game()