from player import Player
import deck

# Set width and height for the game screen
screen_width = 1200
screen_height = 700

# Instantiate the first player        
player_1 = Player("Player 1", "Ari", deck.deck)

# Draw the player's starting hand from their deck
player_1.draw_starting_hand()

