"""A child class to the parent class Card. The Spell class is used for cards
that do not go to the battlefield after being played. Instead, they activate
an effect and go straight to the graveyard"""

import pygame

    
from card import Card

class Spell(Card):
    
    def __init__(self, name, cost, energy_cost, effects, art):
        super().__init__(name, cost, energy_cost, art)
        
        # Card type is used in some functions to decide what to do with a card
        self.type = "spell"
        
        # Different spell effects that spells can have
        # damage_face deals X damage to the enemy's life total
        self.damage_face = None
        self.face_text = ""
        # ramp gives the user X empty devotion points
        self.ramp = None
        self.ramp_text = ""
        # draw gives the user X cards
        self.draw = None
        self.draw_text = ""
        
        self.effects_list = []
        
        # This loop reads the card data to give it the desired effect
        # It reads the number that follows each keyword and executes that number
        # Also creates a list of strings that are used to print to the zoomed in card
        for effect in effects:
            if "damage_face" in effect:
                spec = effect.split()
                self.damage_face = int(spec[1])
                self.face_text =  f"Deal {spec[1]} damage to the opponent"
                self.effects_list.append(self.face_text)
            if "ramp" in effect:
                spec = effect.split()
                self.ramp = int(spec[1])
                self.ramp_text = f"Add {spec[1]} empty devotion to your total"
                self.effects_list.append(self.ramp_text)
            if "draw" in effect:
                spec = effect.split()
                self.draw = int(spec[1])
                self.draw_text = f"Draw {spec[1]} card"
                self.effects_list.append(self.draw_text)
        

                
