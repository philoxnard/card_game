import pygame

pygame.init()


class Card():
    """A class to represent a playing card"""
    
    # Method to initialize each card
    def __init__(self, name, cost, energy_cost, art):
        self.name = name
        self.cost = cost
        self.energy_cost = energy_cost
        self.raw_image = pygame.image.load("card_art\\card_template.bmp")
        self.raw_rect = self.raw_image.get_rect()
        
        self.raw_card_art = pygame.image.load(art)
        self.raw_card_art_rect = self.raw_card_art.get_rect()
        
        scale_factor = 2.5
        ht = int(self.raw_rect.height / scale_factor)
        wd = int(self.raw_rect.width / scale_factor)
        
        art_ht = int(self.raw_card_art_rect.height / scale_factor)
        art_wd = int(self.raw_card_art_rect.width / scale_factor)
        
        self.card_art = pygame.transform.scale(self.raw_card_art, (art_wd, art_ht))
        self.card_art_rect = self.card_art.get_rect()
        
        self.image = pygame.transform.scale(self.raw_image, (wd, ht))
        self.rect = self.image.get_rect()
                
        self.cost_font = pygame.font.Font("freesansbold.ttf", 12)
        self.cost_display = self.cost_font.render(str(self.cost), True, (0,0,255))
        self.cost_rect = self.cost_display.get_rect()
        
        self.energy_font = pygame.font.Font("freesansbold.ttf", 12)
        self.energy_display = self.energy_font.render(str(self.energy_cost), True, (180,0,180))
        self.energy_rect = self.energy_display.get_rect()
        
        self.name_font = pygame.font.Font("freesansbold.ttf", 10)
        self.name_display = self.name_font.render(str(self.name), True, (0,0,0))
        self.name_rect = self.name_display.get_rect()
        
        self.zoom_cost = pygame.transform.scale2x(self.cost_display)
        self.zoom_energy = pygame.transform.scale2x(self.energy_display)
        self.zoom_name = pygame.transform.scale2x(self.name_display)
        
        

        

        
        