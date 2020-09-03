"""A list of issues or necessary changes

    THIS IS TOP PRIORITY
    The zoomed in card is pointless if it doesn't display info!!
    Draw stats on zoomed in card
        zoomed in card will also have special card text
        Gonna wait on this until I have a better idea of what the cards will
        look like
        
    Eventually make a new library for Spell effects

    Gotta write a README to explain the purpose and function
        Also gotta do an overhaul on documentation
    
    Gotta eventually network this bad boy and allow the player to make
        their own deck
        
    Balance of course! And need to update with taxes and identities/kingdoms
        Really I need an entirely new understanding of what the cards are going
        to be.

    Pretty much everything needs to be documented well. Just take a day and
        go through every file and document everything really nicely
        
    Make some preconstructed decks and a main menu that allows players to pick
        their decks
        
    There are a lot of things that are told to the player via text in the 
        console - they must be changed to be made visible somehow - 
        possibly even add sound??
    
Other things that should be tweaked/fixed/changed:

    Find a more concise way to draw all of the icons on cards
    Literally everything that gets drawn to cards is SO messy in terms of how
        its done. Gotta fix it.
    
    Show how many cards enemy has in hand
    
    Need to actually end the game
        For now, just need to display a congrats message for winning player,
        or something like Player 1 wins!
    
    Display whose turn it is, make it clear which battlefield is which
    
    Indicate if you have devoted yet this turn
        draw something if player.devotion_limit is or isnt 0
    
    Clean up the Board class code
        lots of game_ui.screen, game_ui.screen_height, parameters that should
        or shouldnt be there... maybe make a method called self.blit
        that just copies the game_ui.screen.blit code, or something
        to simplify the game_ui.screen/height stuff
    
    Also can draw life total, devotion total, and energy total as ints
    instead of as colored boxes - but tbh I kinda like the boxes.
    Doing this in a pretty way may involve redrawing the entire UI
        IN WHICH CASE, I would like to have everything relate the percentages
        of the screen size rather than static numbers
        ALSO this would go hand in hand with redrawing the game board, which
        I think makes most sense if I actually network. Therefore, this is
        a low priority fix.
    
    

"""