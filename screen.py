import pygame
import game_ui
from player import Player
import deck

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    screen = pygame.display.set_mode(
        (game_ui.screen_width, game_ui.screen_height))
    pygame.display.set_caption("Card Game")
    screen.blit(game_ui.background, (0,0))
    
    # Instantiate the first player        
    player_1 = Player("Player 1", "Ari", deck.deck, screen)
    
    # Draw the player's starting hand from their deck
    player_1.draw_starting_hand()
    
    # Initialize the player's hand
    player_1.show_hand(game_ui.screen_height, screen)
    
    # Initialize get_status method
    player_1.get_status(game_ui.screen_height, screen)
    
    # Initialize the active_card_ix variable
    # This holds the index of the active card.
    # A value of None indicates that no card is active.
    active_card_ix = None
    active_card = None
    
    # Start the main loop for the game 
    while True:
        # handle errors to gracefully quit the pygame app
        try:
            ######################################################################
            #### Code that magnifies a card in your hand if you mouse over it ####
            ######################################################################
            pos = pygame.mouse.get_pos()
            for index, card in enumerate(player_1.hand):
                if card.rect.collidepoint(pos):
                    active_card = player_1.hand[index]
                    x = game_ui.screen_width - active_card.raw_rect.width
                    y = game_ui.screen_height - active_card.raw_rect.height
                    screen.blit(active_card.raw_image, (x, y))   

            #############################################################################
            #### Code that magnifies a card in your battlefield if you mouse over it ####
            #############################################################################
            pos = pygame.mouse.get_pos()
            for index, card in enumerate(player_1.battlefield):
                if card.rect.collidepoint(pos):
                    active_card = player_1.battlefield[index]
                    x = game_ui.screen_width - active_card.raw_rect.width
                    y = game_ui.screen_height - active_card.raw_rect.height
                    screen.blit(active_card.raw_image, (x, y))

            # Get mouse and keyboard events for the game
            for event in pygame.event.get():
                #####################################################################
                ########### Code that allows the user to quit the game ##############
                #####################################################################
                # Did the user click the window close button?
                if event.type == pygame.QUIT:
                    pygame.quit()    
                # Allows the user to quit by hitting "q"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                #####################################################################
                ########### Code that allows the user to end their turn #############
                #####################################################################
                    elif event.key == pygame.K_SPACE:
                        player_1.new_turn(game_ui.screen_height, screen)
                                            
                #####################################################################        
                ################ Code that operates the user's hand #################
                #####################################################################
                # If the user clicks a card in their hand, it prompts them
                # to either play or devote the card
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        active_card_ix = player_1.click_hand(game_ui.screen_height, screen)
                        print(f"index outside of click_hand method is {active_card_ix}")
                    if game_ui.devote_rect.collidepoint(pos):
                        player_1.devote_card(active_card_ix, game_ui.screen_height, screen)
                    elif game_ui.play_rect.collidepoint(pos):
                        player_1.play_card(active_card_ix, game_ui.screen_height, screen)
                    # If the user right clicks, redraw the screen without the option boxes
                    elif event.button==3:
                        active_card_ix = player_1.right_click(game_ui.screen_height, screen)
                    ##########################################################
                    ######### Code for using cards in the battlefield ########
                    ##########################################################
                    # Allows you to attack with a card on the battlefield
                    # Can only be done if a card has been active for a turn
                    if event.button == 1:
                        player_1.attack()
            # Flip the display
            pygame.display.flip()
        except IndexError:
            pass
        except Exception as e:
            pygame.quit()
            raise e
run_game()