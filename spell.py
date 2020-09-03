"""A child class to the parent class Card. The Spell class is used for cards
that do not go to the battlefield after being played. Instead, they activate
an effect and go straight to the graveyard"""

from card import Card

class Spell(Card):
    
    def __init__(self, name, cost, energy_cost, effects, art):
        super().__init__(name, cost, energy_cost, art)
        
        # Card type is used in some functions to decide what to do with a card
        self.type = "spell"
        
        # Different spell effects that spells can have
        # damage_face deals X damage to the enemy's life total
        self.damage_face = None
        # ramp gives the user X empty devotion points
        self.ramp = None
        # draw gives the user X cards
        self.draw = None
        
        # This loop reads the card data to give it the desired effect
        # It reads the number that follows each keyword and executes that number
        for effect in effects:
            if "damage_face" in effect:
                spec = effect.split()
                self.damage_face = int(spec[1])
            if "ramp" in effect:
                spec = effect.split()
                self.ramp = int(spec[1])
            if "draw" in effect:
                spec = effect.split()
                self.draw = int(spec[1])
                
