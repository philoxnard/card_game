"""A library of functions and information that relate to visual and numerical
elements of gameplay"""

import pygame



# Set width and height for the game screen
screen_width = 1400
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

# Scale factor for the hand menu options
scale_factor = 2.1

# Code to get the graphics and rect for the devote hand menu option
devote_raw_image = pygame.image.load("game_ui\\devote.bmp")
devote_rect = devote_raw_image.get_rect()
wd = int(devote_rect.width/scale_factor)
ht = int(devote_rect.height/scale_factor)
devote = pygame.transform.scale(devote_raw_image, (wd, ht))
devote_rect = devote.get_rect()

# Code to get the graphics and rect for the play card hand menu option
play_raw_image = pygame.image.load("game_ui\\play_card.bmp")
play_rect = play_raw_image.get_rect()
wd = int(play_rect.width/scale_factor)
ht = int(play_rect.height/scale_factor)
play = pygame.transform.scale(play_raw_image, (wd, ht))
play_rect = play.get_rect()

# Code to get the graphics and rect for a life point
life = pygame.image.load("game_ui\\life.bmp")
life_rect = life.get_rect()
opp_l_dest_x = 839
opp_l_dest_y = 170

# Code to get the graphics and rect for a mana point
mana = pygame.image.load("game_ui\\mana.bmp")
mana_rect = mana.get_rect()
opp_d_dest_x = 839
opp_d_dest_y = 197

# Code to get the graphics and rect for an empty mana point
empty_mana = pygame.image.load("game_ui\\empty_mana.bmp")
empty_mana_rect = empty_mana.get_rect()

# Code to get the graphics and rect for the energy option
energy = pygame.image.load("game_ui\\energy.bmp")
energy_rect = energy.get_rect()
energy_cost = 3
energy_rect.x = 1013
energy_rect.y = 561
energy_dest_x = 376
energy_dest_y = 69
opp_e_dest_x = 835
opp_e_dest_y = 234


# Code to get the graphics and rect for the draw card option
draw = pygame.image.load("game_ui\\draw.bmp")
draw_rect = draw.get_rect()
draw_cost = 4
draw_rect.x = 1026
draw_rect.y = 632

# Code to get the graphics and rect for the next turn option
next_turn = pygame.image.load("game_ui\\next_turn.bmp")
next_turn_rect = next_turn.get_rect()
next_turn_rect.x = 1013
next_turn_rect.y = 500

# Code to get the graphics and rect for the attack enemy option
enemy = pygame.image.load("game_ui\\enemy.bmp")
enemy_rect = enemy.get_rect()
enemy_rect.x = 764
enemy_rect.y = 500

# Code to place the player display
player_disp_x = 890
player_disp_y = 369

# Code to get the graphics and rect for the asleep condition
asleep = pygame.image.load("game_ui\\asleep.bmp")
asleep_rect = asleep.get_rect()

# Code to get the graphcis and rect for the attacked condition
attacked = pygame.image.load("game_ui\\attacked.bmp")
attacked_rect = attacked.get_rect()

# Code to get the graphics and rect for the attacking condition
# No longer a border! It overlays over the creature image
attacking = pygame.image.load("game_ui\\attacking_border.bmp")
attacking_rect = attacking.get_rect()

# Code to get the graphcis and rect for the guardian keyword
guardian = pygame.image.load("game_ui\\guardian.bmp")
guardian_rect = guardian.get_rect()

# Code to get the graphcis and rect for the alert keyword
alert = pygame.image.load("game_ui\\alert.bmp")
alert_rect = alert.get_rect()

# Code to get the graphics and rect for the magical keyword
magical = pygame.image.load("game_ui\\magical.bmp")
magical_rect = magical.get_rect()

# Code to get the graphics and rect for the damage effect
damage = pygame.image.load("game_ui\\damage.bmp")
damage_rect = damage.get_rect()

# Code to get the graphics and rect for the ramp effect
ramp = pygame.image.load("game_ui\\ramp.bmp")
ramp_rect = ramp.get_rect()

# Code to get the graphics and rect for the draw effect
spell_draw = pygame.image.load("game_ui\\spell_draw.bmp")
spell_draw_rect = spell_draw.get_rect()
    


