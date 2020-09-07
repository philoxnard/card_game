"""Library of functions that relate directly to displaying information for 
cards"""

import pygame

import game_ui

# Could fix this to have the functions pass screen rather than importing from game_ui

# Big function for displaying the different stats for a card 
# Displays cost, energy, art, and name for every card
# Displays health and attack for Characters cards
# Displays keyword icons for Character cards
# This function should be broken up into many many different functions
# One each for hand/battlefield, one each for Character/Spell
def show_card_stats(board, screen, player):
    for card in player.hand:
        screen.blit(card.card_art, (card.rect.x+8, card.rect.y+18))
        screen.blit(card.cost_display, (card.rect.x+card.rect.width-13, card.rect.y+6))
        screen.blit(card.energy_display, (card.rect.x+7, card.rect.y+6))
        screen.blit(card.name_display, (card.rect.x+18, card.rect.y+6))
        if card.type == "character":
            screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
            screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
            if "alert" in card.keywords:
                screen.blit(game_ui.alert, (card.rect.x+card.rect.width-95, card.rect.y+card.rect.height-60))
            if "guardian" in card.keywords:
                screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
            if "magical" in card.keywords:
                screen.blit(game_ui.magical, (card.rect.x+card.rect.width-60, card.rect.y+card.rect.height-60))
        if card.type == "spell":
            if card.damage_face:
                screen.blit(game_ui.damage, (card.rect.x+card.rect.width-95, card.rect.y+card.rect.height-60))
            if card.ramp:
                screen.blit(game_ui.ramp, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
            if card.draw:
                screen.blit(game_ui.spell_draw, (card.rect.x+card.rect.width-60, card.rect.y+card.rect.height-60))
    for card in player.battlefield:
        screen.blit(card.card_art, (card.rect.x+8, card.rect.y+18))
        screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
        screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
        screen.blit(card.name_display, (card.rect.x+18, card.rect.y+6))
        if "guardian" in card.keywords:
            screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))
        if "magical" in card.keywords:
            screen.blit(game_ui.magical, (card.rect.x+card.rect.width-60, card.rect.y+card.rect.height-60))
        if card.first_turn:
            screen.blit(game_ui.asleep, (card.rect.x+card.rect.width-95, card.rect.y+card.rect.height-60))
        if card.attacked:
            screen.blit(game_ui.attacked, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-60))

# Big function for zooming in on a card if you mouse over it
# Should be split into three smaller functions
# One each for hand/battlefield/opponent battlefield        
def expand_card(board, screen, player, enemy):
    pos = pygame.mouse.get_pos()
    for index, card in enumerate(player.hand):
        if card.rect.collidepoint(pos):
            active_card = player.hand[index]
            expanded_card_details(board, screen, player, enemy, active_card)        
    for index, card in enumerate(player.battlefield):
        if card.rect.collidepoint(pos):
            active_card = player.battlefield[index]
            expanded_card_details(board, screen, player, enemy, active_card)
    for index, card in enumerate(enemy.battlefield):
        if card.rect.collidepoint(pos):
            active_card = enemy.battlefield[index]
            expanded_card_details(board, screen, player, enemy, active_card)

# Big function for drawing all the detail to the zoomed in card            
def expanded_card_details(board, screen, player, enemy, active_card):
    x = game_ui.screen_width - active_card.raw_rect.width
    y = game_ui.screen_height - active_card.raw_rect.height
    screen.blit(active_card.raw_image, (x, y))
    screen.blit(active_card.zoom_cost, (x+200, y+13))
    screen.blit(active_card.zoom_energy, (x+13, y+13))
    screen.blit(active_card.zoom_name, (x+30, y+13))
    screen.blit(active_card.raw_card_art, (x+19, y+45))
    if active_card.type == "character":
        screen.blit(active_card.zoom_attack, (x+13, y+310))
        screen.blit(active_card.zoom_health, (x+200, y+310))
        for index, keyword in enumerate(active_card.keywords):
            keyword_font = pygame.font.Font("freesansbold.ttf", 12)
            keyword_display = keyword_font.render(keyword, True, (0,0,0))
            next_display = index*30
            screen.blit(keyword_display, (x+30, y+210+next_display))
    if active_card.type == "spell":
        for index, effect in enumerate(active_card.effects_list):
            effect_font = pygame.font.Font("freesansbold.ttf", 12)
            effect_display = effect_font.render(effect, True, (0,0,0))
            next_display = index*30
            screen.blit(effect_display, (x+30, y+210+next_display))
        
