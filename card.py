import pygame
pygame.init()


class Card():
    """A class to represent a playing card"""
    
    # Method to initialize each card
    def __init__(self, name, cost, energy_cost, attack, health, art):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.energy_cost = energy_cost
        self.raw_image = pygame.image.load(art)
        self.raw_rect = self.raw_image.get_rect()
        
        scale_factor = 2.5
        ht = int(self.raw_rect.height / scale_factor)
        wd = int(self.raw_rect.width / scale_factor)
        
        self.image = pygame.transform.scale(self.raw_image, (wd, ht))
        self.rect = self.image.get_rect()
        
        self.first_turn = True
        self.attacked = False
        
        self.attack_font = pygame.font.Font("freesansbold.ttf", 16)
        self.attack_display = self.attack_font.render(str(self.attack), True, (0,0,0))
        self.attack_rect = self.attack_display.get_rect()
        
        self.health_font = pygame.font.Font('freesansbold.ttf', 16)
        self.health_display = self.health_font.render(str(self.health), True, (255,0,0))
        self.health_rect = self.health_display.get_rect()
        
    def update_health(self):
        self.health_display = self.health_font.render(str(self.health), True, (255,0,0))
        

        
        