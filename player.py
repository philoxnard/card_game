from copy import copy
import pygame

import game_ui


class Player():
    """Class to represent each player"""
    
    # Initializes attributes for the player
    def __init__(self, name, identity, deck_file_name, screen):
        self.name = name
        self.identity = identity
        self.deck = deck_file_name
        self.life_total = 20
        self.hand_size = 6
        self.devotion_total = 0
        self.devotion_pool = 0
        self.hand = []
        self.battlefield = []
        self.devoted_cards = []
        self.screen = screen
        self.devotion_limit = 0
        self.graveyard = []
        self.devotion_max = 10
        self.hand_max = 7
        self.battlefield_max = 7
        
    # Draws the player's starting hand
    def draw_starting_hand(self):
        for i in range(self.hand_size):
            draw = self.deck.pop(0)
            self.hand.append(draw)

    # Show what the player has in their hand 
    def show_hand(self, screen_height, screen): 
        for index, card in enumerate(self.hand):
            card.rect.x = index*card.rect.width
            card.rect.y = screen_height - (card.rect.height)
            screen.blit(card.image, card.rect)
            
        # Show what is on the player's battlefield
    def show_battlefield(self, screen_height, screen):
        for index, card in enumerate(self.battlefield):
            card.rect.x = index*card.rect.width
            card.rect.y = screen_height - 2.8*(card.rect.height)
            screen.blit(card.image, card.rect)
    
    # Show the player's current status
    # Displays devotion, life, devoted cards, and battlefield
    def get_status(self, screen_height, screen):
        # Display a green square for each life point
        for i in range(self.life_total):
            next_image = i*game_ui.life_rect.width
            screen.blit(game_ui.life, (next_image, 0))
        # Display a blue square for each devotion point
        for i in range(self.devotion_pool):
            next_image = i*game_ui.mana_rect.width
            screen.blit(game_ui.mana, (next_image, game_ui.life_rect.height))
        # Display a blue square for each empty devotion point
        for i in range(self.devotion_total-self.devotion_pool):
            next_image = i*game_ui.empty_mana_rect.width
            empty_starting_point = self.devotion_pool*game_ui.mana_rect.width
            screen.blit(game_ui.empty_mana, (empty_starting_point+next_image, game_ui.life_rect.height))
        self.show_battlefield(screen_height, screen)
    
            
    # Add card to devotion pool
    # Removes the selected card from your hand
    # Adds the card to the devoted_cards list
    # Sets the player's devotion_limit to 1, preventing them from devoting again
    ### Must display some sort of error if user devotes while at devotion limit
    def devote_card(self, active_card_ix, screen_height, screen):
        if self.devotion_total < self.devotion_max:
            if self.devotion_limit == 0:
                print("devote")
                self.devotion_total += 1
                self.devotion_pool += 1
                card = self.hand.pop(active_card_ix)
                self.devoted_cards.append(card)
                self.refresh_screen(screen_height, screen)
                self.get_status(screen_height, screen)
                self.devotion_limit = 1
                active_card_ix = None
            else:
                print("Already devoted this turn")
        else:
            print("Already at max devotion")

          
    # Add a card from your hand to the battlefield  
    ### Must display some sort of error if user doesn't have enough devotion
    def play_card(self, active_card_ix, screen_height, screen):
        if len(self.battlefield) < self.battlefield_max:
            if self.hand[active_card_ix].cost <= self.devotion_pool:
                card = self.hand[active_card_ix]
                self.hand.pop(active_card_ix)
                self.battlefield.append(card)
                self.devotion_pool -= card.cost
                self.refresh_screen(screen_height, screen)
                self.get_status(screen_height, screen)
                print("play")
            else:
                print(f"Not enough devotion to play {self.hand[active_card_ix].name}")
        else:
            print("Already too many cards on the battlefield")


    # Draw a card
    ### Must do something if there are no more cards in deck
    def draw_card(self):
        draw = self.deck.pop(0)
        if len(self.hand) < self.hand_max:
            self.hand.append(draw)
        else:
            print("Too many cards in hand - discarding card")
            self.graveyard.append(draw)
       
    def refresh_devotion(self):
        self.devotion_pool = copy(self.devotion_total)
        
    def new_turn(self, screen_height, screen):
        self.devotion_limit = 0
        self.draw_card()
        self.refresh_devotion()
        self.refresh_screen(screen_height, screen)
        self.get_status(screen_height, screen)
        for card in self.battlefield:
            if card.first_turn == True:
                card.first_turn = False
            
    def refresh_screen(self, screen_height, screen):
        screen.blit(game_ui.background, (0,0))
        #self.screen.fill(game_ui.background_color)
        self.show_hand(game_ui.screen_height, self.screen)
        self.get_status(screen_height, screen)
        
    def right_click(self, screen_height, screen):
        self.refresh_screen(game_ui.screen_height, screen)
        game_ui.hand(game_ui.devote, game_ui.devote_rect, (0, -game_ui.devote_rect.height), screen)
        game_ui.hand(game_ui.play, game_ui.play_rect, (game_ui.devote_rect.topleft), screen)
        return None

    def attack(self):
        pos = pygame.mouse.get_pos()
        for card in self.battlefield:
            if card.rect.collidepoint(pos):
                if card.first_turn == False:
                    print("attack")
                else:
                    print("summoning sickness")
                    
    def click_hand(self, screen_height, screen):
        for index, card in enumerate(self.hand):
            pos = pygame.mouse.get_pos()
            if card.rect.collidepoint(pos):
                # Refresh the display
                self.refresh_screen(game_ui.screen_height, screen)
                # Display the option to devote the clicked card
                game_ui.hand(game_ui.devote, game_ui.devote_rect, card.rect.topleft, screen)
                # Display the option to play the clicked card
                game_ui.hand(game_ui.play, game_ui.play_rect, (game_ui.devote_rect.topleft), screen)
                print(f"index being returned in click_hand method is {index}")
                return index



    