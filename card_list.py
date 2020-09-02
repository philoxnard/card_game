"""A list of functions for instantiating cards"""

from card import Card


# Make it easier to get filepath for the card art
file = "card_art\\"

# Cards follow the following structure:
    # Name, Cost, Energy, Attack, Health, Keywords, Art

# Functions to create an instance of every different card
def create_ari():
    return Card("Ari", 3, 0, 3, 3, ["guardian"], f"{file}ari_art.bmp")

def create_guns_endicott():
    return Card("Guns Endicott", 2, 1, 6, 3, ["alert"], f"{file}guns_art.bmp")

def create_regular_man():
    return Card("Regular Man", 1, 0, 2, 1, "", f"{file}regular_art.bmp")
    
def create_jangles():
    return Card("Jangles", 4, 2, 9, 9, ["alert", "guardian"], f"{file}jangles_art.bmp")

def create_billie_soldier():
    return Card("Billie Soldier", 1, 0, 1, 1, ["alert"], f"{file}billie_art.bmp")

def create_blackwater_pirate():
    return Card ("Blackwater Pirate", 3, 0, 3, 1, ["alert"], f"{file}pirate_art.bmp")
