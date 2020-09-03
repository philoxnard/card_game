"""Library of functions that become available to the active player when they
enter the attacking state. That is, when the player clicks on an awake card
in their battlefield, the following functions become available"""

import pygame

import game_ui

# If the user clicks a card in the opponent's battlefield, and if they do not
# have any restrictions because of any guardians in the opponent's battlefield,
# this executes an attack
def execute_attack(board, screen_height, screen, player, enemy):
    if board.button == 1:
        pos = pygame.mouse.get_pos()
        for defending_card in enemy.battlefield:
            if defending_card.rect.collidepoint(pos):
                if enemy.guardian == False:
                    calculate_damage(board, screen, player, enemy, defending_card)
                elif enemy.guardian == True:
                    if "guardian" in defending_card.keywords:
                        calculate_damage(board, screen, player, enemy, defending_card)
                    else:
                        print("Must attack enemy with guardian")

# If an attack is successfully executed, this function will calculate damage.
# Each card will deal its attack to the other, reducing that total from their
# health. Cards who drop to zero or lower are sent to the graveyard
# Will eventually add a keyword "ranged" that will necessitate a new and separate
# damage function
def calculate_damage(board, screen, player, enemy, defending_card):
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
    board.refresh_screen(screen, player, enemy)

# Option to attack the enemy's player life total directly, so long as they
# don't have any characters with guardian    
def attack_player(board, screen_height, screen, player, enemy):
    if board.button == 1:
        pos = pygame.mouse.get_pos()
        if game_ui.enemy_rect.collidepoint(pos):
            if enemy.guardian == False:
                enemy.life_total -= player.attacking_card.attack
                player.attacking_card.attacked = True
                player.attacking_card = None
                player.active_card_ix = None
                board.refresh_screen(screen, player, enemy)
            elif enemy.guardian == True:
                print("Must attack enemy with guardian")

# Gives the current attacking card a visual indicator that it is the attacking
# card 
def animate_card(board, player):
    if player.attacking_card != None:
        if player.attacking_card.attacked == False:
            game_ui.screen.blit(game_ui.attacking, (player.attacking_card.rect.x + 7, player.attacking_card.rect.y + 10))