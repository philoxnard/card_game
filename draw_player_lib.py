"""Library of functions that relate to drawing the active player and all of the
information relevant information and cards"""

import game_ui

# Gets the display information for the active player's hand
def player_hand(board, screen_height, player):
    for index, card in enumerate(player.hand):
        card.rect.x = index*card.rect.width
        card.rect.y = screen_height - (card.rect.height)
        game_ui.screen.blit(card.image, card.rect)

# Gets the display information for the active player's battlefield
def player_battlefield(board, screen_height, player):
    for index, card in enumerate(player.battlefield):
        card.rect.x = index*card.rect.width
        card.rect.y = screen_height - 2.8*(card.rect.height)
        game_ui.screen.blit(card.image, card.rect)

# Gets the display information for the player's health, devotion, and energy
def player_stats(board, player):
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