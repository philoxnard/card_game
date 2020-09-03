"""Library of functions that become available to the active player when they
enter the click hand state. That is, when the player clicks on a card in their
hand and needs to be presented with the play or devote options"""

import pygame

import game_ui
import card_info_lib
import extra_options_lib

# Takes the active card out of the player's hand, reducing the player's devotion
# and energy equal to the devotion and energy cost of the card. If the card is
# a Character, it is added to the battlefield (space permitting). If the card
# is a Spell, its effect goes off and it goes straight to the graveyard. This
# function just checks to see if the cost requirements are met, then it passes
# responsibility to the appropriate function depending on what type of card
# the active card is.
def play_card(board, screen_height, screen, player, enemy):
    if board.button == 1:
        pos = pygame.mouse.get_pos()
        if game_ui.play_rect.collidepoint(pos):
            if player.active_card_ix or player.active_card_ix == 0:
                if player.hand[player.active_card_ix].energy_cost <= player.energy_pool:
                    if player.hand[player.active_card_ix].cost <= player.devotion_pool:
                        if player.hand[player.active_card_ix].type == "character":
                            play_character(board, screen, player, enemy)
                        elif player.hand[player.active_card_ix].type == "spell":
                            play_spell(board, screen, player, enemy)
                    else:
                        print(f"Not enough devotion to play {player.hand[player.active_card_ix].name}")
                else:
                    print(f"Not enough energy to play {player.hand[player.active_card_ix].name}")

# Specific function for adding a Character to the player's battlefield.                   
def play_character(board, screen, player, enemy):
    if len(player.battlefield) < player.battlefield_max:
        card = player.hand[player.active_card_ix]
        player.hand.pop(player.active_card_ix)
        player.battlefield.append(card)
        player.energy_pool -= card.energy_cost
        player.devotion_pool -= card.cost
        player.active_card_ix = None
        board.refresh_screen(screen, player, enemy)
    else:
        print("Already too many cards on the battlefield")
        
# Specific function for casting a Spell, activating its effects then discarding
# it.
def play_spell(board, screen, player, enemy):
    spell = player.hand[player.active_card_ix]
    player.hand.pop(player.active_card_ix)
    player.graveyard.append(spell)
    player.devotion_pool -= spell.cost
    player.active_card_ix = None
    if spell.damage_face:
        enemy.life_total -= spell.damage_face
    if spell.ramp:
        player.devotion_total += spell.ramp
    if spell.draw:
        for i in range(spell.draw):
            extra_options_lib.draw_card(board, player)
    for card in player.battlefield:
        if "magical" in card.keywords:
            card.attack += 1
            card.attack_display = card.attack_font.render(str(card.attack), True, (0,0,0))
            card_info_lib.show_card_stats(board, player)
    board.refresh_screen(screen, player, enemy)

# This allows the user to devote a card, which removes it from their hand, 
# adds to to a (yet unused) list of devoted cards, and increases the player's
# devotion total by 1                            
def devote_card(board, screen_height, screen, player, enemy):
    if board.button == 1:
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
                        board.refresh_screen(screen, player, enemy)
                    else:
                        print("Already devoted this turn")
                else:
                    print("Already at max devotion")

# Displays the Play Card and Devote options to the player.
def display_options(board, screen, player):
    game_ui.devote_rect.bottomleft = player.hand[player.active_card_ix].rect.topleft
    game_ui.play_rect.bottomleft = game_ui.devote_rect.topleft
    screen.blit(game_ui.devote, game_ui.devote_rect)
    screen.blit(game_ui.play, game_ui.play_rect)