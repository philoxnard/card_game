"""A sample deck"""


import random
import card_list



# Create an empty list for the deck
aggro_deck = []
deck = []
      
# Fill the deck with cards  
deck.append(card_list.create_ari())
deck.append(card_list.create_ari())
deck.append(card_list.create_ari())
deck.append(card_list.create_ari())
deck.append(card_list.create_song_of_soothing())
deck.append(card_list.create_song_of_soothing())
deck.append(card_list.create_song_of_soothing())
deck.append(card_list.create_song_of_soothing())
deck.append(card_list.create_kuka_ule_cop())
deck.append(card_list.create_kuka_ule_cop())
deck.append(card_list.create_kuka_ule_cop())
deck.append(card_list.create_kuka_ule_cop())
deck.append(card_list.create_magic_snake())
deck.append(card_list.create_magic_snake())
deck.append(card_list.create_magic_snake())
deck.append(card_list.create_magic_snake())
deck.append(card_list.create_regular_man())
deck.append(card_list.create_regular_man())
deck.append(card_list.create_regular_man())
deck.append(card_list.create_regular_man())
deck.append(card_list.create_guns_endicott())
deck.append(card_list.create_guns_endicott())
deck.append(card_list.create_guns_endicott())
deck.append(card_list.create_guns_endicott())
deck.append(card_list.create_jangles())
deck.append(card_list.create_jangles())
deck.append(card_list.create_jangles())
deck.append(card_list.create_jangles())

# Another sample deck for aggressive play
aggro_deck.append(card_list.create_billie_soldier())
aggro_deck.append(card_list.create_billie_soldier())
aggro_deck.append(card_list.create_billie_soldier())
aggro_deck.append(card_list.create_billie_soldier())
aggro_deck.append(card_list.create_blackwater_pirate())
aggro_deck.append(card_list.create_blackwater_pirate())
aggro_deck.append(card_list.create_blackwater_pirate())
aggro_deck.append(card_list.create_blackwater_pirate())
aggro_deck.append(card_list.create_regular_man())
aggro_deck.append(card_list.create_regular_man())
aggro_deck.append(card_list.create_regular_man())
aggro_deck.append(card_list.create_regular_man())
aggro_deck.append(card_list.create_mini_magician())
aggro_deck.append(card_list.create_mini_magician())
aggro_deck.append(card_list.create_mini_magician())
aggro_deck.append(card_list.create_mini_magician())
aggro_deck.append(card_list.create_magic_snake())
aggro_deck.append(card_list.create_magic_snake())
aggro_deck.append(card_list.create_magic_snake())
aggro_deck.append(card_list.create_magic_snake())
aggro_deck.append(card_list.create_fireball())
aggro_deck.append(card_list.create_fireball())
aggro_deck.append(card_list.create_fireball())
aggro_deck.append(card_list.create_fireball())
aggro_deck.append(card_list.create_guns_endicott())
aggro_deck.append(card_list.create_guns_endicott())
aggro_deck.append(card_list.create_guns_endicott())
aggro_deck.append(card_list.create_flame_spike())
aggro_deck.append(card_list.create_flame_spike())
aggro_deck.append(card_list.create_flame_spike())

random.shuffle(deck)
random.shuffle(aggro_deck)