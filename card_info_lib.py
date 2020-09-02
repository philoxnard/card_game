import pygame

import game_ui

# Could fix this to have the functions pass screen rather than importing from game_ui

def show_card_stats(board, player):
    for card in player.hand:
        game_ui.screen.blit(card.card_art, (card.rect.x+8, card.rect.y+18))
        game_ui.screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
        game_ui.screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
        game_ui.screen.blit(card.cost_display, (card.rect.x+card.rect.width-13, card.rect.y+6))
        game_ui.screen.blit(card.energy_display, (card.rect.x+7, card.rect.y+6))
        game_ui.screen.blit(card.name_display, (card.rect.x+18, card.rect.y+6))
        if "alert" in card.keywords:
            game_ui.screen.blit(game_ui.alert, (card.rect.x+card.rect.width-95, card.rect.y+card.rect.height-60))
        if "guardian" in card.keywords:
            game_ui.screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
    for card in player.battlefield:
        game_ui.screen.blit(card.card_art, (card.rect.x+8, card.rect.y+18))
        game_ui.screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
        game_ui.screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
        game_ui.screen.blit(card.name_display, (card.rect.x+18, card.rect.y+6))
        if "guardian" in card.keywords:
            game_ui.screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
        if card.first_turn:
            game_ui.screen.blit(game_ui.asleep, (card.rect.x+card.rect.width-95, card.rect.y+card.rect.height-60))
        if card.attacked:
            game_ui.screen.blit(game_ui.attacked, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-60))
        
def expand_card(board, player, enemy):
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