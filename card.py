import pygame

pygame.init()


class Card():
    """A class to represent a playing card"""
    
    # Method to initialize each card
    def __init__(self, name, cost, energy_cost, attack, health, keywords, art):
        self.name = name
        self.cost = cost
        self.attack = attack
        self.health = health
        self.energy_cost = energy_cost
        self.raw_image = pygame.image.load(art)
        self.raw_rect = self.raw_image.get_rect()
        self.keywords = keywords
        
        scale_factor = 2.5
        ht = int(self.raw_rect.height / scale_factor)
        wd = int(self.raw_rect.width / scale_factor)
        
        self.image = pygame.transform.scale(self.raw_image, (wd, ht))
        self.rect = self.image.get_rect()
        
        self.first_turn = True
        self.attacked = False
        
        if "alert" in self.keywords:
            self.first_turn = False
        
        self.attack_font = pygame.font.Font("freesansbold.ttf", 16)
        self.attack_display = self.attack_font.render(str(self.attack), True, (0,0,0))
        self.attack_rect = self.attack_display.get_rect()
        
        self.health_font = pygame.font.Font('freesansbold.ttf', 16)
        self.health_display = self.health_font.render(str(self.health), True, (255,0,0))
        self.health_rect = self.health_display.get_rect()
        
        self.cost_font = pygame.font.Font("freesansbold.ttf", 16)
        self.cost_display = self.cost_font.render(str(self.cost), True, (0,0,255))
        self.cost_rect = self.cost_display.get_rect()
        
        self.energy_font = pygame.font.Font("freesansbold.ttf", 16)
        self.energy_display = self.energy_font.render(str(self.energy_cost), True, (180,0,180))
        self.energy_rect = self.energy_display.get_rect()
        
        self.name_font = pygame.font.Font("freesansbold.ttf", 10)
        self.name_display = self.name_font.render(str(self.name), True, (0,0,0))
        self.name_rect = self.name_display.get_rect()
        
    def update_health(self):
        self.health_display = self.health_font.render(str(self.health), True, (255,0,0))
        

        
        