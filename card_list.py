"""A list of functions for instantiating cards"""

from card import Card


# Make it easier to get filepath for the card art
file = "card_art\\"

# Functions to create an instance of every different card
def create_ari():
    return Card("Ari", 3, 0, 3, 5, "[guardian]", f"{file}ari_art.bmp")

def create_guns_endicott():
    return Card("Guns Endicott", 4, 1, 6, 3, ["alert"], f"{file}guns_art.bmp")

def create_regular_man():
    return Card("Regular Man", 1, 0, 2, 1, "", f"{file}regular_art.bmp")
    
def create_jangles():
    return Card("Nasty Mr. Jangles", 7, 2, 9, 9, ["alert", "guardian"], f"{file}jangles_art.bmp")
