from copy import copy


class Player():
    """Class to represent each player"""
    
    # Initializes attributes for the player
    def __init__(self, name, identity, deck_file_name):
        self.name = name
        self.identity = identity
        self.deck = deck_file_name
        self.life_total = 10
        self.hand_size = 5
        self.devotion_total = 0
        self.devotion_pool = 0
        self.hand = []
        self.battlefield = []
        self.devoted_cards = []
        
    # Draws the player's starting hand
    def draw_starting_hand(self):
        for i in range(self.hand_size):
            draw = self.deck.pop(0)
            self.hand.append(draw)

    # Show what the player has in their hand 
    def show_hand(self, screen_height, screen): 
        for index, card in enumerate(self.hand):
            card.rect.x = index*card.rect.width
            card.rect.y = screen_height - (card.rect.height)
            screen.blit(card.image, card.rect)
    
    # Show the player's current status
    # Displays devotion, life, devoted cards, and battlefield
    def get_status(self):
        print()
        print(f"Current devotion: {str(self.devotion_pool)}/{str(self.devotion_total)}")
        print(f"Current life total: {str(self.life_total)}")
        print("Current devoted cards: ")
        for i in self.devoted_cards:
            print("    " + i.name.title())
        print("Current cards on the battlefield: ")
        for i in self.battlefield:
            print("    " + i.name.title())
        print()
        
    # Checks to see if the player's input is valid
    def check_correct(self, action):
        correct = False
        while correct is False:
            print("Input '0' to skip to the next phase")
            self.card_choice = input(f"Which card would you like to {action}? ")
            if self.card_choice.isdigit() == False:
                print("Error: Please input a digit\n")
            elif int(self.card_choice) == 0:
                correct = True
            elif int(self.card_choice) not in range(1, len(self.hand)+1):
                print("Error: Please select a card in your hand\n")
            else:
                correct = True
    
    # Add card to devotion pool
    def devote_card(self):
        Player.check_correct(self, "devote")
        self.card_choice = int(self.card_choice)
        if self.card_choice == 0:
            pass
        else:
            print()
            self.devotion_total += 1
            card = self.hand.pop(self.card_choice-1)
            self.devoted_cards.append(card)
          
    # Add a card from your hand to the battlefield  
    def play_card(self):
        devotion_correct = False
        while devotion_correct == False:
            Player.check_correct(self, "play")
            self.card_choice = int(self.card_choice)
            if self.card_choice == 0:
                devotion_correct = True
            else:
                print()
                self.card = self.hand[self.card_choice-1]
                if self.card.cost <= self.devotion_pool:
                    self.card = self.hand.pop(self.card_choice-1)
                    self.battlefield.append(self.card)
                    self.devotion_pool -= self.card.cost
                    devotion_correct = True
                else:
                    print(f"Error - not enough devotion to play {self.card.name}")
                
    # Check to see if you have enough devotion to play a card
    #def check_devotion(self):
        
    
    # Draw a card
    def draw_card(self):
       draw = self.deck.pop(0)
       self.hand.append(draw) 
       
    def update_devotion(self):
        self.devotion_pool = copy(self.devotion_total)
        
        
    # Layout for a turn
    def take_turn(self):
        print("__________________________")
        Player.draw_card(self)
        Player.show_hand(self)
        Player.update_devotion(self)
        Player.get_status(self)
        Player.devote_card(self)
        Player.update_devotion(self)
        Player.get_status(self)
        Player.show_hand(self)
        Player.play_card(self)
        Player.get_status(self)
        print("__________________________")
        
        


    