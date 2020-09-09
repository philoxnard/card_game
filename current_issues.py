"""A list of issues or necessary changes

    CURRENT PROJECT
    During deck select, display to the user who is picking their deck. aka, 
        draw something like "PLAYER ONE SELECT YOUR DECK"    
        Also, add a third deck that's like, tempo or swarm or something
        
    Make the decks a lil more concise by using for loops;
        for i in range 4:
            deck.append(card)
        
    Easy fix to make shit shorter - import game_ui and main_menu_ui as shorter
        variables so everything isn't so fucking massive. AND make every blit
        like how it is in the main menu stuff - define all the rect Xs and Ys
        in the game_ui rather than in the main functions
        
    Do a general sweep of the code and make it prettier
        The design choices in the menu code are soooo much easier to read and
        understand than in the main body - fixing that could be nice. Also I 
        think a lot of the comments are probably not super good.
    
    Make a spell effect for dealing X damage to a character
        Also a spell effect for dealing X to any target
        
    Eventually make a new library for Spell effects

    Gotta eventually network this bad boy and allow the player to make
        their own deck
        
    Make a play vs CPU option... gonna be hard lol
        
    Update game with identities, factions, and taxes. This will make things more
        interesting I think, but also will necessitate a LOT more cards
        
    Create another card type that's like an enchantment or artifact

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

    
    

"""