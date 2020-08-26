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
    
    # Instantiate the players        
    player_1 = Player("Player 1", "Ari", deck.deck, screen)
    player_2 = Player("Player 2", "Coda", deck.deck, screen)
    player_1.refresh_screen(game_ui.screen_height, screen)
    
    # Draw the player's starting hand from their deck
    player_1.draw_starting_hand()
    player_2.draw_starting_hand()
    
    # Initialize the player's hand
    player_1.show_hand(game_ui.screen_height, screen)
    
    # Initialize get_status method
    player_1.get_status(game_ui.screen_height, screen)
    
    # Initialize the active_card_ix variable
    # This holds the index of the active card.
    # A value of None indicates that no card is active.
    active_card_ix = None
    
    active_player = 1
    
    # Start the main loop for the game 
    while True:
        # handle errors to gracefully quit the pygame app
        try:
            ###############################################################
            ####### Code that magnifies a card if you mouse over it #######
            ###############################################################
            if active_player == 1:
                player_1.expand_card(screen)
                player_1.expand_card_bf(screen)
            elif active_player == 2:
                player_2.expand_card(screen)
                player_2.expand_card_bf(screen)
            
            ###############################################################
            ########## Get mouse and keyboard events for the game #########
            ###############################################################
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
                ################ Code that operates the user's hand #################
                #####################################################################
                # If the user clicks a card in their hand, it prompts them
                # to either play or devote the card
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if active_player == 1:
                        if event.button == 1:
                            player_1.attack()
                            pos = pygame.mouse.get_pos()
                            for index, card in enumerate(player_1.hand):
                                if card.rect.collidepoint(pos):
                                    player_1.refresh_screen(game_ui.screen_height, screen)
                                    game_ui.hand(game_ui.devote, game_ui.devote_rect, card.rect.topleft, screen)
                                    game_ui.hand(game_ui.play, game_ui.play_rect, (game_ui.devote_rect.topleft), screen)
                                    active_card_ix = index
                            # Code for executing the "Devote" button  
                            if game_ui.devote_rect.collidepoint(pos):
                                player_1.devote_card(active_card_ix, game_ui.screen_height, screen)
                            # Code for executing the "Play Card" button
                            elif game_ui.play_rect.collidepoint(pos):
                                player_1.play_card(active_card_ix, game_ui.screen_height, screen)
                                
                        ##########################################################
                        ########### Code for using the extra options #############
                        ##########################################################
                        
                            player_1.extra_draw(game_ui.screen_height, screen)
                            player_1.get_energy(game_ui.screen_height, screen)
                            active_player = player_2.new_turn(game_ui.screen_height, active_player, screen)

                        # If the user right clicks, redraw the screen without the option boxes
                        elif event.button==3:
                            player_1.right_click(game_ui.screen_height, screen)
                        
                    
                    elif active_player == 2:
                        if event.button == 1:
                            player_2.attack()
                            pos = pygame.mouse.get_pos()
                            for index, card in enumerate(player_2.hand):
                                if card.rect.collidepoint(pos):
                                    player_2.refresh_screen(game_ui.screen_height, screen)
                                    game_ui.hand(game_ui.devote, game_ui.devote_rect, card.rect.topleft, screen)
                                    game_ui.hand(game_ui.play, game_ui.play_rect, (game_ui.devote_rect.topleft), screen)
                                    active_card_ix = index
                            # Code for executing the "Devote" button  
                            if game_ui.devote_rect.collidepoint(pos):
                                player_2.devote_card(active_card_ix, game_ui.screen_height, screen)
                            # Code for executing the "Play Card" button
                            elif game_ui.play_rect.collidepoint(pos):
                                player_2.play_card(active_card_ix, game_ui.screen_height, screen)
                                    
                        ##########################################################
                        ########### Code for using the extra options #############
                        ##########################################################
                            
                            player_2.extra_draw(game_ui.screen_height, screen)
                            player_2.get_energy(game_ui.screen_height, screen)
                            active_player = player_1.new_turn(game_ui.screen_height, active_player, screen)
                            # If the user right clicks, redraw the screen without the option boxes
                        elif event.button==3:
                            player_2.right_click(game_ui.screen_height, screen)
                     
            # Flip the display
            pygame.display.flip()
        except Exception as e:
            pygame.quit()
            raise e
run_game()