"""Library of functinos that relate to executing all of the extra options for
a player. This includes quitting the game, ending the turn, getting energy, 
and drawing a card"""

import pygame

import game_ui

# Function for ending the turn when the end turn button is clicked
# Ends all current states, resets the player's upkeep, and switches active
# Control from one player to the other
def end_turn(board, player, enemy):
    if board.button == 1:
        pos = pygame.mouse.get_pos()
        if game_ui.next_turn_rect.collidepoint(pos):
            player.active_card_ix = None
            player.attacking_card = None
            player.upkeep = False
            player.active_player = False
            enemy.active_player = True

# Calls the draw card function if the player clicks the draw button and has
# enough devotion            
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
 
# Gives the active player an energy point if they click the energy button
# and have enough devotion
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
                    
# Simple function for adding a card from the player's deck to their hand
# If they already have too many cards in hand, the new card gets burned
def draw_card(board, player):
    draw = player.deck.pop(0)
    if len(player.hand) < player.hand_max:
        player.hand.append(draw)
    else:
        print("Too many cards in hand - discarding card")
        player.graveyard.append(draw)

# If the user hits the exit button or hits the Q key, this function gets called
# to exit out of the game.                                 
def quit_game(board):
    if board.button == "q":
        pygame.quit()