"""A child class to the parent class Card. The Character class is used for 
cards that go to the battlefield upon being played. They have an attack and
health value and are sent to the graveyard if their health hits zero"""

import pygame

from card import Card

class Character(Card):
    
    def __init__(self, name, cost, energy_cost, attack, health, keywords, identity, art):
        super().__init__(name, cost, energy_cost, art)
        self.attack = attack
        self.health = health
        self.keywords = keywords
        self.identity = identity
        
        # Card type is used in some functions to decide what to do with a card
        self.type = "character"
        
        # first_turn is used to determine if the character is asleep (after being
        # played) or awake if it's been on the field for a turn
        self.first_turn = True
        # attacked is used to determine if a character has attacked this turn.
        # This will have to be turned into a number if I implement a keyword
        # for doublestrike/windfury
        self.attacked = False
        
        # the alert keyword allows a character to attack on their first turn out
        if "alert" in self.keywords:
            self.first_turn = False
        
        # Creates the display properties for a character's attack
        self.attack_font = pygame.font.Font("freesansbold.ttf", 16)
        self.attack_display = self.attack_font.render(str(self.attack), True, (0,0,0))
        self.attack_rect = self.attack_display.get_rect()
        
        # Creates the display properties for a character's health
        self.health_font = pygame.font.Font('freesansbold.ttf', 16)
        self.health_display = self.health_font.render(str(self.health), True, (255,0,0))
        self.health_rect = self.health_display.get_rect()
        
    # Quick function for updating a character's health
    def update_health(self):
        self.health_display = self.health_font.render(str(self.health), True, (255,0,0))