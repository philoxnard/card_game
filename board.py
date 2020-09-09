"""The highest level class in the game. the Board class is responsible for 
instantiating the players, guiding the active player's turn, drawing the active
and inactive player's relevant information, and doing pretty much everything.

The functionality that the Board class has is spread between a volume of 
smaller, more specific libraries for handling specific things"""

import pygame
from copy import copy
import random

from player import Player
import deck
import game_ui
import click_hand_state
import attacking_state
import extra_options_lib
import draw_enemy_lib
import draw_player_lib
import card_info_lib


class Board():
    
    # Method to initialize the gameboard and the players
    def __init__(self):
        self.game_board = pygame.image.load("background.bmp")
        self.game_board_rect = self.game_board.get_rect()
        self.button = None
        self.start_game_attr = False
        game_ui.screen.blit(self.game_board, (0,0))
        pygame.display.set_caption("Card Game")
     
    # Highest level method in the Board class
    # Checks to see who is the active player and who is the enemy
    def play_game(self, screen_height, screen):
        self.start_game()
        self.draw_extra_options(screen)
        for index, player in enumerate(self.players):
            if player.active_player:
                enemy = self.players[int(not bool(index))]
                self.player_turn(screen, player, enemy)
    
    # High level method that defines the active player's turn
    def player_turn(self, screen, player, enemy):
        self.start_turn(screen, player, enemy)
        self.draw_player(player)
        self.draw_enemy(screen, enemy)
        card_info_lib.show_card_stats(self, screen, player)
        card_info_lib.expand_card(self, screen, player, enemy)
        self.check_guardian(enemy)
        self.button = self.get_event_button()
        self.right_click(game_ui.screen_height, game_ui.screen, player, enemy)
        self.click_hand(screen, player, enemy)
        if player.active_card_ix or player.active_card_ix == 0:
            click_hand_state.display_options(self, screen, player)
            click_hand_state.play_card(self, game_ui.screen_height, screen, player, enemy)
            click_hand_state.devote_card(self, game_ui.screen_height, screen, player, enemy)
        self.start_attack(game_ui.screen_height, game_ui.screen, player)
        if player.attacking_card:
            attacking_state.execute_attack(self, game_ui.screen_height, screen, player, enemy)
            attacking_state.attack_player(self, game_ui.screen_height, screen, player, enemy)
            attacking_state.animate_card(self, player)
        extra_options_lib.end_turn(self, player, enemy)
        extra_options_lib.extra_draw(self, screen, player, enemy)
        extra_options_lib.get_energy(self, screen, player, enemy)
        extra_options_lib.quit_game(self)
        self.end_game()
        
    # Function that only runs once at the beginning of the game
    def start_game(self):
        if self.start_game_attr == False:
            self.players = []
            self.player_1 = Player("Player 1", "Ari", deck.player_1_deck, game_ui.screen)
            self.player_2 = Player("Player 2", "Coda", deck.player_2_deck, game_ui.screen)
            random.shuffle(self.player_1.deck)
            random.shuffle(self.player_2.deck)
            self.players.append(self.player_1)
            self.players.append(self.player_2)
            self.player_1.draw_starting_hand()
            self.player_2.draw_starting_hand(1)
            self.player_1.active_player = True
            self.start_game_attr = True

    # Collection of functions from the draw_player_lib responsible for drawing
    # the visual aspects of the player
    def draw_player(self, player):
        draw_player_lib.player_hand(self, game_ui.screen_height, player)
        draw_player_lib.player_battlefield(self, game_ui.screen_height, player)
        draw_player_lib.player_stats(self, player)
    
    # Collection of functions from the draw_enemy_lib responsible for drawing
    # the visual aspects of the enemy
    def draw_enemy(self, screen, enemy):
        draw_enemy_lib.enemy_battlefield(self, game_ui.screen_height, enemy)
        draw_enemy_lib.enemy_stats(self, enemy)
        draw_enemy_lib.show_enemy_stats(self, screen, enemy)
    
    # Draws all of the extra options for the player
    # Includes get energy, draw a card, end the turn, and attack enemy directly
    def draw_extra_options(self, screen):
        screen.blit(game_ui.energy, game_ui.energy_rect)
        screen.blit(game_ui.draw, game_ui.draw_rect)
        screen.blit(game_ui.next_turn, game_ui.next_turn_rect)
        screen.blit(game_ui.enemy, game_ui.enemy_rect)
    
    # A VERY important function that gets called very frequently to redraw
    # pretty much everything on screen. Any time anything on the board changes,
    # this function must be called        
    def refresh_screen(self, screen, player, enemy):
        game_ui.screen.blit(self.game_board, (0,0))
        self.draw_extra_options(screen)
        self.draw_player(player)
        self.draw_enemy(screen, enemy)
        card_info_lib.show_card_stats(self, screen, player)
            
    # A function for maintaining a player's upkeep when they start a new turn.
    # Draws them a card, refreshes their devotion pool, removes their limit
    # on devoting cards, wakes up any of their sleeping cards
    def start_turn(self, screen, player, enemy):
        if player.upkeep == False:
            player.devotion_pool = copy(player.devotion_total)  
            extra_options_lib.draw_card(self, player)
            player.devotion_limit = 0
            for card in player.battlefield:
                if card.first_turn:
                    card.first_turn = False
                if card.attacked:
                    card.attacked = False
            player.upkeep = True
            self.refresh_screen(screen, player, enemy)
 
    # Checks to see if the enemy has any guardian Characters in their battlefield.
    # If they do, it limits the options that the active player has in terms
    # of attacking
    def check_guardian(self, enemy):
        if enemy.battlefield == []:
            enemy.guardian = False
        else:
            for card in enemy.battlefield:
                if "guardian" in card.keywords:
                    enemy.guardian = True
                elif "guardian" not in card.keywords:
                    enemy.guardian = False

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
    
    # Right clicks are like state refreshers. If any state is active on a 
    # player's turn, it cancels out those states and removes the click hand
    # options.                        
    def right_click(self, screen_height, screen, player, enemy):
        if self.button == 3:
            player.attacking_card = None
            player.active_card_ix = None
            screen.blit(game_ui.devote, (-300,-300))
            screen.blit(game_ui.play, (-300, -300))
            self.refresh_screen(screen, player, enemy)

    # If a card in your hand is clicked, this enters the click hand state            
    def click_hand(self, screen, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            for index, card in enumerate(player.hand):
                if card.rect.collidepoint(pos):
                    self.refresh_screen(screen, player, enemy)
                    player.active_card_ix = index

    # If a card on the battlefield is clicked, if that card is awake, enters
    # the attacking state
    def start_attack(self, screen_height, screen, player):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            for card in player.battlefield:
                if card.rect.collidepoint(pos):
                    if card.attacked == False:                        
                        if card.first_turn == False:
                            print("attack")
                            player.attacking_card = card
                        else:
                            print("summoning sickness")
                    else:
                        print(f"{card.name} has already attacked this turn")

    # Function that ends the game. This is called when a player's health
    # is reduced to zero.                                                                     
    def end_game(self):
        if self.player_1.life_total <= 0 or self.player_2.life_total <= 0:
            game_ui.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
        
    
                
