import pygame

import game_ui

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

def animate_card(board, player):
    if player.attacking_card != None:
        if player.attacking_card.attacked == False:
            game_ui.screen.blit(game_ui.attacking, (player.attacking_card.rect.x + 7, player.attacking_card.rect.y + 10))