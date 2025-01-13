# BotPokeMMO
A bot made in python to play PokeMMO game to automatize repetitive tasks like shiny capture, pokemon training, pokemon capture for perfect IV, and so on.

## Functions ready:

1. Shiny hunt and capture (Magikarp)
2. Pokemon capture for perfect IV (Magikarp)
3. Berry planting, watering, and harvesting.

The two first functions were made for Magikarp, but the system is generalizable for any pokemon, it only needs the registration of the target pokemon in the system, and the path to the character arrives at the spot area that the pokemon is related, which needs to be programmed.

## Next Steps:

### Pokemon capture for perfect IV  
* Test the system if it is capturing the target pokémon and ignoring others (unless it is shiny), when there are more than one pokemon in the spot area.

### Shiny hunt and capture
* Develop routine for going to the center at the end of the battle if the pokémon is low HP.
* Develop routine for when our attacking pokémon faints (Put other, except the false swipe pokemon, and use the right attack)
* Develop routine for when our false swipe pokémon faints (Put other and just tries to capture, if there is only one wild pokémon)

### New function: EV training
* Develop function for EV training on the selected spot (If it appears a shiny, capture it)

### New function: Levelling up grinding
* Develop function for grinding XP on the selected spot (If it appears a shiny, capture it).
