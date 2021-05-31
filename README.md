# Snakes-And-Ladders
This is a basic console input based snakes and ladders game, without any GUI.
We input the number of players we want. 
The length of the list "list_of_players" is equal to the number of players. In this list, each index number corresponds to a particular player.
Eg,
Index 0-> Player 1
Index 1-> Player 2
Index 2-> Player 3
Index i-> Player (i+1)

There are two dictionaries, snakes and ladders. If the position that a player lands on is a key in either of these dictionaries, then the player is shifted to the value of that particular key. 

Everytime a player moves backward or forward, the correspoding index of the "list_of_players" is updated to the position of the player.
The die is cast using the random library, which chooses a random number from the list [1,2,3,4,5,6]. This number is added to the previous position, ie, value at the corresponding index of "list_of_players" to get the new position of the player.

There is a for loop inside a while loop.
The while loop keeps iterating on until one value of the "list_of_players" list becomes equal to 100. In that case, the while loop ends and the player corresponding to the index number of the value 100 is the winner.

The for loop iterates for each player to cast his die, update his position and print out the current position of all the players. The user is required to input either W or w to cast his die. Pressing any other button will skip his chance of playing and move on to the next player.

If the player lands on a ladder or a snake's mouth, he will be warned of it.
