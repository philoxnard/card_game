import pygame

import game_ui

def end_turn(board, player, enemy):
    if board.button == 1:
        pos = pygame.mouse.get_pos()
        if game_ui.next_turn_rect.collidepoint(pos):
            player.active_card_ix = None
            player.attacking_card = None
            player.upkeep = False
            player.active_player = False
            enemy.active_player = True
            
def extra_draw(board, screen, player, enemy):
    if board.button == 1:
        pos = pygame.mouse.get_pos()
        if game_ui.draw_rect.collidepoint(pos):
            if player.devotion_pool >= game_ui.draw_cost:
                player.devotion_pool -= game_ui.draw_cost
                board.draw_card(player)
                board.refresh_screen(screen, player, enemy)
            else:
                print("Not enough devotion")
                
def get_energy(board, screen, player, enemy):
    if board.button == 1:
        pos = pygame.mouse.get_pos()
        if game_ui.energy_rect.collidepoint(pos):
            if player.energy_pool == player.energy_max:
                print("Already at max energy")
            else:
                if player.devotion_pool >= game_ui.energy_cost:
                    player.energy_pool += 1
                    player.devotion_pool -= game_ui.energy_cost
                    board.refresh_screen(screen, player, enemy)
                else:
                    print("Not enough devotion")
                                 
def quit_game(board):
    if board.button == "q":
        pygame.quit()