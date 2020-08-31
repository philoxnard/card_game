import pygame
import game_ui
from board import Board

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    board = Board()

    # Draw the player's starting hand from their deck
    # Player 2 gets an extra card for going second
    board.player_1.draw_starting_hand()
    board.player_2.draw_starting_hand(1)
    
    # Set player 1 to be the first active player
    board.player_1.active_player = True
    
    # Highest level logic loop for the game
    
    while True:
        # handle errors to gracefully quit the pygame app
        try:
            if board.player_1.life_total > 0 and board.player_2.life_total > 0:
                board.play_game(game_ui.screen_height, game_ui.screen)
            else:
                game_ui.screen.fill((0,0,0))
                game_ui.quit_game()
            # Flip the display
            pygame.display.flip()
        except Exception as e:
            pygame.quit()
            raise e
run_game()