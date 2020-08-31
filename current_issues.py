"""A list of issues
        
    Gotta eventually network this bad boy and allow the player to make
        their own deck
        
    Balance of course! And need to update with taxes and identities/kingdoms

Other things that should be tweaked/fixed/changed:
    
    Show how many cards enemy has in hand
    
    Need to actually end the game
    
    Display whose turn it is
    
    Indicate if a creature has attacked
        draw something on the card if card.attacked == True
    
    Indicate if you have devoted yet this turn
        draw something if player.devotion_limit is or isnt 0
    
    Draw stats on zoomed in card
    
    Clean up the Board class code
        lots of game_ui.screen, game_ui.screen_height, parameters that should
        or shouldnt be there... maybe make a method called self.blit
        that just copies the game_ui.screen.blit code, or something
        to simplify the game_ui.screen/height stuff
    
    When a card has summoning sickness, I'd like a visual indicator, maybe
    a Zzz or something similar
        draw something if card.first_turn == True
    
    Draw a card's devotion cost and energy cost straight onto the card
    maybe the energy can stay as boxes, i like them
    
    Also maybe draw the card name on the card? Possibly art too? Text???
    
    Also can draw life total, devotion total, and energy total as ints
    instead of as colored boxes - but tbh I kinda like the boxes
    
    

"""