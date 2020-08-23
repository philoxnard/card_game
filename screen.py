import pygame
import main
import game_ui

background_color = (0,0,0)

def run_game():
    # Initialize pygame, settings, and screen object
    pygame.init()
    screen = pygame.display.set_mode(
        (main.screen_width, main.screen_height))
    pygame.display.set_caption("Card Game")
    screen.fill(background_color)
    
    # Initialize the player's hand
    main.player_1.show_hand(main.screen_height, screen)
    
    # Start the main loop for the game 
    while True:
        # handle errors to gracefully quit the pygame app
        try:
            # Get mouse and keyboard events for the game
            for event in pygame.event.get():
                # Did the user click the window close button?
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                # Allows the user to quit by hitting "q"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        
                # Cause something to happen if the user clicks on a card in the hand
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                    pos = pygame.mouse.get_pos()
                    for card in main.player_1.hand:
                        if card.rect.collidepoint(pos):
                            screen.fill(background_color)
                            main.player_1.show_hand(main.screen_height, screen)
                            # Display the option to devote the clicked card
                            game_ui.devote_option_rect.bottomleft = card.rect.topleft
                            screen.blit(game_ui.devote_option, game_ui.devote_option_rect)
                            # Display the option to play the clicked card
                            game_ui.play_card_option_rect.bottomleft = game_ui.devote_option_rect.topleft
                            screen.blit(game_ui.play_card_option, game_ui.play_card_option_rect)
                            #If the user right clicks, redraw the screen without the option boxes
                if event.type == pygame.MOUSEBUTTONDOWN and event.button==3:
                    screen.fill(background_color)
                    main.player_1.show_hand(main.screen_height, screen)
                            ##########
                            # Need to make the two options clickable
                            # Need to allow the user to right click to step back - get rid of the two options
                            # Other next step is to visualize all the info from get_status
                            ##########
            # Flip the display
            pygame.display.flip()
        except Exception as e:
            pygame.quit()
            raise e
run_game()