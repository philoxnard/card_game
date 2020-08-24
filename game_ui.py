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

# Code to get the graphics and rect for a mana point
mana = pygame.image.load("game_ui\\mana.bmp")
mana_rect = mana.get_rect()

# Code to get the graphics and rect for an empty mana point
empty_mana = pygame.image.load("game_ui\\empty_mana.bmp")
empty_mana_rect = empty_mana.get_rect()

# Function for instantiating the images/rects
# for the options a player has when they select a card
def hand(option_image, option_rect, anchor, screen):
    option_rect.bottomleft = anchor
    screen.blit(option_image, option_rect)
    

    


