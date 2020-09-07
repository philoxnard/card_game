"""

This is a currently unnamed digital card game in the same vein as digital card
games like Heathstone and ShadowVerse. Each player has their own life total and
access to various characters (other games call them minions, creatures, etc) and
and spells that they can use to dwindle their opponent's life total to zero. 
Whoever loses all 20 of their starting life points first loses.

Three key differences in play set this game apart from other card games, whether
virtual or real. Firstly, unlike Hearthstone and ShadowVerse, a player's mana
total (called Devotion in this game) does not increment every turn automatically.
Instead, a player must choose a card in their hand to Devote - Devoting a card
will discard it from your hand, making it unplayable, but adding one point to 
your devotion total/pool. This is similar to Magic: The Gathering's use of lands
to increase your mana pool. However, unlike in MtG, a player will never be 
"mana screwed" or "mana flooded", two unfortunate conditions that render a game
very un-fun and un-interactive. In this card game, every single card in your hand
is a potential "land", which means: 1) You will never draw too few "lands", 
2) You will never have too many lands and not enough "non-land" cards, and 
3) Players have more decisions to make on their turn - do they want to devote
the high cost card in their hand in favor of playing a low cost card this turn, 
or do they want to devote the low cost card in hopes of surviving for a few 
more turns so they can drop their high cost bomb? More decisions generally means
a more fun and interesting game - this design principle is the key driver
behind the devotion mechanic.

In the same vein, players have yet another option available to them that is not
available in most card games: The option to gain an "Energy Point" at the cost
of 3 devotion points. Energy is a special kind of resource that, unlike, devotion,
does not refresh to your total at the start of each new turn. Energy Points are
one time use resources. For example, if you play a card that costs 3 Devotion
and 2 Energy, and you currently havec 6 Devotion and 2 Energy in your resource
pool, you will start your next turn with 6 Devotion and 0 Energy. The Devotion
refreshes and refills, but the Energy is gone and must be purchased again. The
intent behind Energy is similar to the intent behind the Devotion mechanic: to
give players more meaningful choices. Do they play a 3-cost character this turn,
or do they leave their board empty and buy an Energy Point so they can play a 
stronger character next turn? Energy is meant to fill a similar role as Vespein
Gas does in StarCraft - it is necessary to play some of the stronger characters
in the game, but harvesting it will leave you weaker in the early phases of
the game. Aggro decks may forgo including any cards with an Energy cost, while
control decks may have a large number of them.

Lastly, also in the same vein, players have the option of drawing a new card
to their hand at the steep cost of 4 Devotion. Having no cards in hand isn't
terribly fun, but the ability to draw cards on a whim is potentially very, very
strong. This option seeks to remedy the boredom and luck that comes from top
decking every turn and hoping to draw the nuts, while at the same time trying
to not give too much power to lategame decks that will have the Devotion to draw
whenever they want.

Many other mechanics in the game are shared with Hearthstone or MtG. Characters
cannot attack on the first turn they are played unless they have the "alert"
keyword, spells are one-time use cards that have various different effects, etc.
Structurally and functionally, the game plays nearly identical to Hearthstone.
No sense in reinventing the wheel here, as non traditional TCGs tend not to
fair too well. Further editions of the game will include factions and identities
similar to Android: NetRunner, but implementation of this is a decent ways 
down the pipeline. Another set of features that will be implemented later are
online multiplayer and playing against AI. Currently, the game can only be played
on one machine with the two players alternating seats at the computer, much
like a game of Hot Seat in Civilization. 

"""