import pygame

# Code to get the graphics and rect for the Start Game option
start_game = pygame.image.load("main_menu_ui\\start_game_art.bmp")
start_game_rect = start_game.get_rect()
start_game_rect.x = 550
start_game_rect.y = 250

# Code to get the graphics and rect for the How to Play option
how_to_play = pygame.image.load("main_menu_ui\\how_to_play.bmp")
how_to_play_rect = how_to_play.get_rect()
how_to_play_rect.x = 550
how_to_play_rect.y = 400

# Code to get the graphics and rect for the Hot Seat option
hot_seat = pygame.image.load("main_menu_ui\\play_hot_seat.bmp")
hot_seat_rect = hot_seat.get_rect()
hot_seat_rect.x = 550
hot_seat_rect.y = 300

# Code to get the graphics and rect for the Play vs CPU option
play_vs_cpu = pygame.image.load("main_menu_ui\\play_vs_cpu.bmp")
play_vs_cpu_rect = play_vs_cpu.get_rect()
play_vs_cpu_rect.x = 550
play_vs_cpu_rect.y = 200

# Code to get the graphics and rect for the Play Online option
play_online = pygame.image.load("main_menu_ui\\play_online.bmp")
play_online_rect = play_online.get_rect()
play_online_rect.x = 550
play_online_rect.y = 100

# Code to get the graphics and rect for the Rule Descriptions
rule_descriptions = pygame.image.load("main_menu_ui\\rule_descriptions.bmp")
rule_descriptions_rect = rule_descriptions.get_rect()
rule_descriptions_rect.x = 0
rule_descriptions_rect.y = 0

# Code to tget the graphics and rects for the Aggro Deck
aggro_deck = pygame.image.load("main_menu_ui\\aggro_deck.bmp")
aggro_deck_rect = aggro_deck.get_rect()
aggro_deck_rect.x = 200
aggro_deck_rect.y = 100

# Code to get the the graphics and rect for the Ramp Deck
ramp_deck = pygame.image.load("main_menu_ui\\ramp_deck.bmp")
ramp_deck_rect = ramp_deck.get_rect()
ramp_deck_rect.x = 700
ramp_deck_rect.y = 100