import pygame

"""Maybe make this a class ClickOption, and make it a sprite subclass"""
scale_factor = 1.8
devote_option_raw_image = pygame.image.load("game_ui\\devote.bmp")
devote_option_rect = devote_option_raw_image.get_rect()
wd = int(devote_option_rect.width/scale_factor)
ht = int(devote_option_rect.height/scale_factor)
devote_option = pygame.transform.scale(devote_option_raw_image, (wd, ht))
devote_option_rect = devote_option.get_rect()

play_card_option_raw_image = pygame.image.load("game_ui\\play_card.bmp")
play_card_option_rect = play_card_option_raw_image.get_rect()
wd = int(play_card_option_rect.width/scale_factor)
ht = int(play_card_option_rect.height/scale_factor)
play_card_option = pygame.transform.scale(play_card_option_raw_image, (wd, ht))
play_card_option_rect = play_card_option.get_rect()

