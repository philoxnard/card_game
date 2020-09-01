import pygame
from copy import copy

from player import Player
import deck
import game_ui


class Board():
    
    # Method to initialize the gameboard and the players
    def __init__(self):
        self.game_board = pygame.image.load("background.bmp")
        self.game_board_rect = self.game_board.get_rect()
        self.players = []
        self.player_1 = Player("Player 1", "Ari", deck.deck, game_ui.screen)
        self.player_2 = Player("Player 2", "Coda", deck.aggro_deck, game_ui.screen)
        self.players.append(self.player_1)
        self.players.append(self.player_2)
        self.button = None
        game_ui.screen.blit(self.game_board, (0,0))
        pygame.display.set_caption("Card Game")
     
    # Highest level method in the Board class
    # Checks to see the active player, then draws their battlefield
    # Draws enemy stats for the inactive player
    def play_game(self, screen_height, screen):
        self.extra_options(game_ui.screen)
        for index, player in enumerate(self.players):
            if player.active_player:
                enemy = self.players[int(not bool(index))]
                self.player_turn(player, enemy)
                
    def extra_options(self, screen):
        screen.blit(game_ui.energy, game_ui.energy_rect)
        screen.blit(game_ui.draw, game_ui.draw_rect)
        screen.blit(game_ui.next_turn, game_ui.next_turn_rect)
        screen.blit(game_ui.enemy, game_ui.enemy_rect)
    
    # High level method that defines the active player's turn
    # Draws their hand, battlefield, and their stats
    def player_turn(self, player, enemy):
        self.start_turn(player, enemy)
        self.draw_player(player)
        self.draw_enemy(enemy)
        self.check_guardian(enemy)
        self.show_card_stats(player)
        self.expand_card(player, enemy)
        self.button = self.get_event_button()
        self.right_click(game_ui.screen_height, game_ui.screen, player, enemy)
        self.click_hand(player, enemy)
        if player.active_card_ix or player.active_card_ix == 0:
            self.display_options(game_ui.screen, player)
            self.play_card(game_ui.screen_height, game_ui.screen, player, enemy)
            self.devote_card(game_ui.screen_height, game_ui.screen, player, enemy)
        self.start_attack(game_ui.screen_height, game_ui.screen, player)
        if player.attacking_card:
            self.execute_attack(game_ui.screen_height, game_ui.screen, player, enemy)
            self.attack_player(game_ui.screen_height, game_ui.screen, player, enemy)
            self.animate_card(player)
        self.end_turn(player, enemy)
        self.extra_draw(player, enemy)
        self.get_energy(player, enemy)
        self.quit_game()
    
    def draw_player(self, player):
        self.player_hand(game_ui.screen_height, player)
        self.player_battlefield(game_ui.screen_height, player)
        self.player_stats(player)
            
    def refresh_screen(self, player, enemy):
        game_ui.screen.blit(self.game_board, (0,0))
        self.extra_options(game_ui.screen)
        self.draw_player(player)
        self.draw_enemy(enemy)
        self.show_card_stats(player)
            
    def start_turn(self, player, enemy):
        if player.upkeep == False:
            player.devotion_pool = copy(player.devotion_total)  
            self.draw_card(player)
            player.devotion_limit = 0
            for card in player.battlefield:
                if card.first_turn:
                    card.first_turn = False
                if card.attacked:
                    card.attacked = False
            player.upkeep = True
            self.refresh_screen(player, enemy)

    def draw_card(self, player):
        draw = player.deck.pop(0)
        if len(player.hand) < player.hand_max:
            player.hand.append(draw)
        else:
            print("Too many cards in hand - discarding card")
            player.graveyard.append(draw)

    # Draws the active player's hand       
    def player_hand(self, screen_height, player):
        for index, card in enumerate(player.hand):
            card.rect.x = index*card.rect.width
            card.rect.y = screen_height - (card.rect.height)
            game_ui.screen.blit(card.image, card.rect)
    
    # Draws the active player's battlefield
    def player_battlefield(self, screen_height, player):
        for index, card in enumerate(player.battlefield):
            card.rect.x = index*card.rect.width
            card.rect.y = screen_height - 2.8*(card.rect.height)
            game_ui.screen.blit(card.image, card.rect)
    
    # Draws the active player's stats
    def player_stats(self, player):
        for i in range(player.life_total):
            next_image = i*game_ui.life_rect.width
            game_ui.screen.blit(game_ui.life, (next_image, 0))
        for i in range(player.devotion_pool):
            next_image = i*game_ui.mana_rect.width
            game_ui.screen.blit(game_ui.mana, (next_image, game_ui.life_rect.height))
        for i in range(player.devotion_total-player.devotion_pool):
            next_image = i*game_ui.empty_mana_rect.width
            empty_starting_point = player.devotion_pool*game_ui.mana_rect.width
            game_ui.screen.blit(game_ui.empty_mana, (empty_starting_point+next_image, game_ui.life_rect.height))
        for i in range(player.energy_pool):
            next_image = i*game_ui.energy_rect.width
            game_ui.screen.blit(game_ui.energy, (game_ui.energy_dest_x+next_image, game_ui.energy_dest_y))
            
    def show_card_stats(self, player):
        for card in player.hand:
            game_ui.screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
            game_ui.screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
            game_ui.screen.blit(card.cost_display, (card.rect.x+card.rect.width-12, card.rect.y+4))
            game_ui.screen.blit(card.energy_display, (card.rect.x+6, card.rect.y+4))
            game_ui.screen.blit(card.name_display, (card.rect.x+12, card.rect.y+4))
            if "guardian" in card.keywords:
                game_ui.screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
        for card in player.battlefield:
            game_ui.screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
            game_ui.screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
            game_ui.screen.blit(card.name_display, (card.rect.x+12, card.rect.y+4))
            if "guardian" in card.keywords:
                game_ui.screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
            if card.first_turn:
                game_ui.screen.blit(game_ui.asleep, (card.rect.x+card.rect.width-95, card.rect.y+card.rect.height-60))
            if card.attacked:
                game_ui.screen.blit(game_ui.attacked, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-60))
            
    def expand_card(self, player, enemy):
        pos = pygame.mouse.get_pos()
        for index, card in enumerate(player.hand):
            if card.rect.collidepoint(pos):
                active_card = player.hand[index]
                x = game_ui.screen_width - active_card.raw_rect.width
                y = game_ui.screen_height - active_card.raw_rect.height
                game_ui.screen.blit(active_card.raw_image, (x, y))
        for index, card in enumerate(player.battlefield):
            if card.rect.collidepoint(pos):
                active_card = player.battlefield[index]
                x = game_ui.screen_width - active_card.raw_rect.width
                y = game_ui.screen_height - active_card.raw_rect.height
                game_ui.screen.blit(active_card.raw_image, (x, y))
        for index, card in enumerate(enemy.battlefield):
            if card.rect.collidepoint(pos):
                active_card = enemy.battlefield[index]
                x = game_ui.screen_width - active_card.raw_rect.width
                y = game_ui.screen_height - active_card.raw_rect.height
                game_ui.screen.blit(active_card.raw_image, (x, y))
            
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
                        
    def right_click(self, screen_height, screen, player, enemy):
        if self.button == 3:
            player.attacking_card = None
            player.active_card_ix = None
            screen.blit(game_ui.devote, (-300,-300))
            screen.blit(game_ui.play, (-300, -300))
            self.refresh_screen(player, enemy)
            
    def click_hand(self, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            for index, card in enumerate(player.hand):
                if card.rect.collidepoint(pos):
                    self.refresh_screen(player, enemy)
                    player.active_card_ix = index

    def display_options(self, screen, player):
        game_ui.devote_rect.bottomleft = player.hand[player.active_card_ix].rect.topleft
        game_ui.play_rect.bottomleft = game_ui.devote_rect.topleft
        screen.blit(game_ui.devote, game_ui.devote_rect)
        screen.blit(game_ui.play, game_ui.play_rect)

    def play_card(self, screen_height, screen, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            if game_ui.play_rect.collidepoint(pos):
                if player.active_card_ix or player.active_card_ix == 0:
                    if player.hand[player.active_card_ix].energy_cost <= player.energy_pool:
                        if len(player.battlefield) < player.battlefield_max:
                            if player.hand[player.active_card_ix].cost <= player.devotion_pool:
                                card = player.hand[player.active_card_ix]
                                player.hand.pop(player.active_card_ix)
                                player.battlefield.append(card)
                                player.energy_pool -= card.energy_cost
                                player.devotion_pool -= card.cost
                                player.active_card_ix = None
                                self.refresh_screen(player, enemy)
                            else:
                                print(f"Not enough devotion to play {player.hand[self.active_card_ix].name}")
                        else:
                            print("Already too many cards on the battlefield")
                    else:
                        print(f"Not enough energy to play {player.hand[self.active_card_ix].name}")
                                
    def devote_card(self, screen_height, screen, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            if game_ui.devote_rect.collidepoint(pos):
                if player.active_card_ix or player.active_card_ix == 0:
                    if player.devotion_total < player.devotion_max:
                        if player.devotion_limit == 0:
                            print("devote")
                            player.devotion_total += 1
                            player.devotion_pool += 1
                            card = player.hand.pop(player.active_card_ix)
                            player.devoted_cards.append(card)
                            player.devotion_limit = 1
                            player.active_card_ix = None
                            self.refresh_screen(player, enemy)
                        else:
                            print("Already devoted this turn")
                    else:
                        print("Already at max devotion")
                                
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
                        
    def execute_attack(self, screen_height, screen, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            for defending_card in enemy.battlefield:
                if defending_card.rect.collidepoint(pos):
                    if enemy.guardian == False:
                        self.calculate_damage(player, enemy, defending_card)
                    elif enemy.guardian == True:
                        if "guardian" in defending_card.keywords:
                            self.calculate_damage(player, enemy, defending_card)
                        else:
                            print("Must attack enemy with guardian")
    
    def calculate_damage(self, player, enemy, defending_card):
        player.attacking_card.health -= defending_card.attack
        defending_card.health -= player.attacking_card.attack
        defending_card.update_health()
        player.attacking_card.update_health()
        if player.attacking_card.health <= 0:
            player.battlefield.remove(player.attacking_card)
            player.graveyard.append(player.attacking_card)
        if defending_card.health <= 0:
            enemy.battlefield.remove(defending_card)
            enemy.graveyard.append(defending_card)
        player.attacking_card.attacked = True
        player.attacking_card = None
        player.active_card_ix = None
        self.refresh_screen(player, enemy)
                    
    def check_guardian(self, enemy):
        for card in enemy.battlefield:
            if "guardian" in card.keywords:
                enemy.guardian = True
            else:
                enemy.guardian = False
                    
    def attack_player(self, screen_height, screen, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            if game_ui.enemy_rect.collidepoint(pos):
                if enemy.guardian == False:
                    enemy.life_total -= player.attacking_card.attack
                    player.attacking_card.attacked = True
                    player.attacking_card = None
                    player.active_card_ix = None
                    self.refresh_screen(player, enemy)
                elif enemy.guardian == True:
                    print("Must attack enemy with guardian")
    
    def animate_card(self, player):
        if player.attacking_card != None:
            if player.attacking_card.attacked == False:
                game_ui.screen.blit(game_ui.attacking, (player.attacking_card.rect.x + 7, player.attacking_card.rect.y + 10))
    
    # High level method that draws the enemy's board
    # Draws their battlefield and their stats
    def draw_enemy(self, enemy):
        self.enemy_battlefield(game_ui.screen_height, enemy)
        self.enemy_stats(enemy)
        self.show_enemy_stats(enemy)
    
    # Draws the current enemy's stats
    def enemy_stats(self, enemy):
        for i in range(enemy.life_total):
            next_image = i*game_ui.life_rect.width
            game_ui.screen.blit(game_ui.life, (next_image + game_ui.opp_l_dest_x, game_ui.opp_l_dest_y))
        for i in range(enemy.devotion_total):
            next_image = i*game_ui.mana_rect.width
            game_ui.screen.blit(game_ui.mana, (next_image+game_ui.opp_d_dest_x, game_ui.opp_d_dest_y))
        for i in range(enemy.energy_pool):
            next_image = i*game_ui.energy_rect.width
            game_ui.screen.blit(game_ui.energy, (game_ui.opp_e_dest_x+next_image, game_ui.opp_e_dest_y))
        
    # Draws the current enemy's battlefield        
    def enemy_battlefield(self, screen_height, enemy):
        for index, card in enumerate(enemy.battlefield):
            card.rect.x = index*card.rect.width + 665
            card.rect.y = 8
            game_ui.screen.blit(card.image, card.rect)

    def show_enemy_stats(self, enemy):
        for card in enemy.battlefield:
            game_ui.screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
            game_ui.screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
            game_ui.screen.blit(card.name_display, (card.rect.x+12, card.rect.y+4))
            if "guardian" in card.keywords:
                game_ui.screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
            
    # End any current states                
    def end_turn(self, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            if game_ui.next_turn_rect.collidepoint(pos):
                player.active_card_ix = None
                player.attacking_card = None
                player.upkeep = False
                player.active_player = False
                enemy.active_player = True
                
    def extra_draw(self, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            if game_ui.draw_rect.collidepoint(pos):
                if player.devotion_pool >= game_ui.draw_cost:
                    player.devotion_pool -= game_ui.draw_cost
                    self.draw_card(player)
                    self.refresh_screen(player, enemy)
                else:
                    print("Not enough devotion")
                    
    def get_energy(self, player, enemy):
        if self.button == 1:
            pos = pygame.mouse.get_pos()
            if game_ui.energy_rect.collidepoint(pos):
                if player.energy_pool == player.energy_max:
                    print("Already at max energy")
                else:
                    if player.devotion_pool >= game_ui.energy_cost:
                        player.energy_pool += 1
                        player.devotion_pool -= game_ui.energy_cost
                        self.refresh_screen(player, enemy)
                    else:
                        print("Not enough devotion")
                                     
    def quit_game(self):
        if self.button == "q":
            pygame.quit()
            
    def end_game(self):
        game_ui.screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
    

            
