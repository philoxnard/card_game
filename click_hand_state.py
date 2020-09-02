import pygame

import game_ui


def play_card(board, screen_height, screen, player, enemy):
    if board.button == 1:
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
                            board.refresh_screen(screen, player, enemy)
                        else:
                            print(f"Not enough devotion to play {player.hand[player.active_card_ix].name}")
                    else:
                        print("Already too many cards on the battlefield")
                else:
                    print(f"Not enough energy to play {player.hand[player.active_card_ix].name}")
                            
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
                    
def display_options(board, screen, player):
    game_ui.devote_rect.bottomleft = player.hand[player.active_card_ix].rect.topleft
    game_ui.play_rect.bottomleft = game_ui.devote_rect.topleft
    screen.blit(game_ui.devote, game_ui.devote_rect)
    screen.blit(game_ui.play, game_ui.play_rect)