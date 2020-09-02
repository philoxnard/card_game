class Player():
    """Class to represent each player"""
    
    # Initializes attributes for the player
    def __init__(self, name, identity, deck_file_name, screen):
        self.name = name
        self.identity = identity
        self.deck = deck_file_name
        self.life_total = 20
        self.starting_hand_size = 4
        self.devotion_total = 0
        self.devotion_pool = 0
        self.hand = []
        self.battlefield = []
        self.devoted_cards = []
        self.screen = screen
        self.devotion_limit = 0
        self.graveyard = []
        self.devotion_max = 10
        self.hand_max = 7
        self.battlefield_max = 7
        self.energy_pool = 0
        self.energy_max = 3
        self.attacking_card = None
        self.active_card_ix = None
        self.active_player = False
        self.upkeep = False
        self.guardian = False
        
    # Draws the player's starting hand
    def draw_starting_hand(self, first_turn = 0):
        for i in range(self.starting_hand_size+first_turn):
            draw = self.deck.pop(0)
            self.hand.append(draw)
           

                

                

     


                


        



        