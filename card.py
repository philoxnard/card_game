import pygame

class Card():
    """A class to represent a playing card"""
    
    # Method to initialize each card
    def __init__(self, name="", cost="", attack="", health="", art=""):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.raw_image = pygame.image.load(art)
        self.raw_rect = self.raw_image.get_rect()
        
        scale_factor = 2.5
        ht = int(self.raw_rect.height / scale_factor)
        wd = int(self.raw_rect.width / scale_factor)
        
        self.image = pygame.transform.scale(self.raw_image, (wd, ht))
        self.rect = self.image.get_rect()
        
        self.first_turn = True