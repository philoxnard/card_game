import pygame

# A list of settings for the general UI

# Set the background the screen
background = pygame.image.load("background.bmp")
background_rect = background.get_rect()

# Set width and height for the game screen
screen_width = 1400
screen_height = 700

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


# Function for instantiating the images/rects
# for the options a player has when they select a card
def hand(option_image, option_rect, anchor, screen):
    option_rect.bottomleft = anchor
    screen.blit(option_image, option_rect)
    

    

    


