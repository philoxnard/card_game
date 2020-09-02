import game_ui

def enemy_stats(board, enemy):
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
def enemy_battlefield(board, screen_height, enemy):
    for index, card in enumerate(enemy.battlefield):
        card.rect.x = index*card.rect.width + 665
        card.rect.y = 8
        game_ui.screen.blit(card.image, card.rect)

def show_enemy_stats(board, screen, enemy):
    for card in enemy.battlefield:
        screen.blit(card.card_art, (card.rect.x+8, card.rect.y+18))
        screen.blit(card.health_display, (card.rect.x+card.rect.width-18, card.rect.y+card.rect.height-22))
        screen.blit(card.attack_display, (card.rect.x+card.rect.width-90, card.rect.y+card.rect.height-22))
        screen.blit(card.name_display, (card.rect.x+12, card.rect.y+4))
        if "guardian" in card.keywords:
            screen.blit(game_ui.guardian, (card.rect.x+card.rect.width-30, card.rect.y+card.rect.height-60))