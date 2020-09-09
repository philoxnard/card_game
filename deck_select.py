import deck
import main_menu_ui as mmu

def draw_background(menu, screen):
    screen.fill((0,0,0))

def draw_deck_options(menu, screen):
    screen.blit(mmu.aggro_deck, mmu.aggro_deck_rect)
    screen.blit(mmu.ramp_deck, mmu.ramp_deck_rect)
    
def select_aggro_deck(menu):
    if menu.button == 1:
        if mmu.aggro_deck_rect.collidepoint(menu.pos):
            if menu.player_select == 1:
                deck.player_1_deck = deck.aggro_deck
                menu.button = 0
                menu.player_select = 2
            elif menu.player_select == 2:
                deck.player_2_deck = deck.aggro_deck
                menu.button = 0
                menu.deck_select = False
                menu.start_game = True
                
def select_ramp_deck(menu):
    if menu.button == 1:
        if mmu.ramp_deck_rect.collidepoint(menu.pos):
            if menu.player_select == 1:
                deck.player_1_deck = deck.ramp_deck
                menu.button = 0
                menu.player_select = 2
            elif menu.player_select == 2:
                deck.player_2_deck = deck.ramp_deck
                menu.button = 0
                menu.deck_select = False
                menu.start_game = True
            
    
