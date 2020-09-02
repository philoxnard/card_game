"""A list of issues or necessary changes

    Gotta write a README to explain the purpose and function
    
    Gotta eventually network this bad boy and allow the player to make
        their own deck
        
    Balance of course! And need to update with taxes and identities/kingdoms
        Really I need an entirely new understanding of what the cards are going
        to be.

    Pretty much everything needs to be documented well. Just take a day and
        go through every file and document everything really nicely
        
    Getting a yaml file of all the cards OR have each card contain a dictionary
        containing name, attack, cost, etc - that might be a more consice way to 
        do it so that each card doesn't eventually have a million parameters
        
    Make some new cards and implement some way for users to make their own 
        decks. That would be sooo cool but would need basically an entire
        new document of code
    
Other things that should be tweaked/fixed/changed:
    
    Show how many cards enemy has in hand
    
    Need to actually end the game
        For now, just need to display a congrats message for winning player,
        or something like Player 1 wins!
    
    Display whose turn it is, make it clear which battlefield is which
    
    Indicate if you have devoted yet this turn
        draw something if player.devotion_limit is or isnt 0
    
    Draw stats on zoomed in card
        zoomed in card will also have special card text
        Gonna wait on this until I have a better idea of what the cards will
        look like
    
    Clean up the Board class code
        lots of game_ui.screen, game_ui.screen_height, parameters that should
        or shouldnt be there... maybe make a method called self.blit
        that just copies the game_ui.screen.blit code, or something
        to simplify the game_ui.screen/height stuff
    
    Decide on final layout for the card so you can finialize the drawing of stats
        Also could be nice to move all the card stat display drawing to a new
        file, or at least class so its a little bit cleaner. This feels like
        a low priority fix, it would have to come after figuring out more
        about what I want the cards to actually look like. Function stuff first.
        
    Draw the card art in the same way that you currently have card stats/keywords
        drawn. In other words, dont put it straight on the card, but display it
        relative to the card's current position
    
    Also can draw life total, devotion total, and energy total as ints
    instead of as colored boxes - but tbh I kinda like the boxes.
    Doing this in a pretty way may involve redrawing the entire UI
        IN WHICH CASE, I would like to have everything relate the percentages
        of the screen size rather than static numbers
        ALSO this would go hand in hand with redrawing the game board, which
        I think makes most sense if I actually network. Therefore, this is
        a low priority fix.
    
    

"""