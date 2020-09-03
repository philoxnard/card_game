"""A list of functions for instantiating cards
This currently contains every card in the game, but as the number of cards
grows, this should be split into smaller, more manageable libraries"""

from character import Character
from spell import Spell


# Make it easier to get filepath for the card art
file = "card_art\\"

# Characters follow the following structure:
    # Name, Cost, Energy, Attack, Health, Keywords, Art
    
# Spells follow the following structure:
    # Name, Cost, Energy, Effects, Art

# Functions to create an instance of every different card
def create_ari():
    return Character("Ari", 4, 0, 4, 3, ["guardian"], "Human Hero", f"{file}ari_art.bmp")

def create_kuka_ule_cop():
    return Character("Kuka Ule Cop", 1, 0, 1, 3, ["guardian"], "Human Cop", f"{file}kuka_ule_cop_art.bmp")

def create_guns_endicott():
    return Character("Guns Endicott", 2, 1, 6, 3, ["alert"], "Human Hero", f"{file}guns_art.bmp")

def create_regular_man():
    return Character("Regular Man", 1, 0, 2, 1, "", "Human", f"{file}regular_art.bmp")
    
def create_jangles():
    return Character("Jangles", 6, 2, 10, 10, ["alert", "guardian"], "Nightmare", f"{file}jangles_art.bmp")

def create_billie_soldier():
    return Character("Billie Soldier", 1, 0, 1, 1, ["alert"], "Billie Soldier", f"{file}billie_art.bmp")

def create_blackwater_pirate():
    return Character("Blackwater Pirate", 3, 0, 3, 1, ["alert"], "Human Pirate", f"{file}pirate_art.bmp")

def create_mini_magician():
    return Character("Mini Magician", 1, 0, 1, 3, ["magical"], "Lowling Wizard", f"{file}mini_magician_art.bmp")

def create_fireball():
    return Spell("Fireball", 1, 0, ["damage_face 3"], f"{file}fireball_art.bmp")

def create_song_of_soothing():
    return Spell("Song of Soothing", 3, 0, ["ramp 2", "draw 1"], f"{file}song_of_soothing_art.bmp")

def create_flame_spike():
    return Spell("Flame Spike", 4, 0, ["damage_face 7"], f"{file}flame_spike_art.bmp")

def create_magic_snake():
    return Spell("Magic Snake", 2, 0, ["damage_face 2", "ramp 1"], f"{file}magic_snake_art.bmp")