import time
import random as rnd

ladders={3:51,
         8:27,
         20:70,
         36:55,
         63:95,
         68:98}

snakes={25:5,
        34:1,
        47:19,
        65:52,
        87:57,
        91:61,
        99:6
        }

die=[1,2,3,4,5,6]


print("The rules are simple:\n1. Press W or w to cast your die. Pressing any other key will just skip your chance of casting the die.")
time.sleep(2)
print("2. Wait for the die to cast your number.")
time.sleep(2)
print("3. Don't get angry if you come across any sudden snakes that I might have placed.")
time.sleep(2)
print("4. If you get angry, then don't press any random buttons to reset the game.")
time.sleep(2)
print("5. Have fun.")
time.sleep(2)

#number_of_players will just contain the number of players.

number_of_players=int(input("Enter the number of players: "))
print("So, there are",number_of_players,"players.\n")

#list_of_players is a list of the all the players' current position.
#Since the list starts at 0, players will be assigned as follows.
#Index 0-> Player 1
#Index 1-> Player 2
#Index 2-> Player 3
#Index i-> Player (i+1)


list_of_players=[0 for i in range(number_of_players)]
i=0

#This outer loop is to check if any player reaches 100 first.
#When any of the values in list_of_players reaches 100,
#This outer loop will stop iterating.
while(100 not in list_of_players):
    
    #This inner loop is to iterate through the number of players.
    for i in range(0,number_of_players):
        castDie=input("\nPlayer {}'s turn:  ".format(i+1))
        
        #Checking if the user input is W or w.
        #Pressing only these keys will cast the die
        #Else, the game will stop and will have to again start from the beginning.
        if(castDie=='W' or castDie=='w'):
            
            #Randomly selects a number from the 6 faced die.
            castResult=rnd.choice(die)
            print("Its a {}.".format(castResult))
            
            #checking to see if the next cast would make the player's position more than 100 or not.
            #if the addition result is more than 100, then skip to the next player.
            if(list_of_players[i]+castResult>100):
                continue
            list_of_players[i]+=castResult
            print("Player {} is at position {}".format(i+1, list_of_players[i]))
            
            #In case the player lands on a snake's mouth
            if(list_of_players[i] in snakes.keys()):
                print("A snake devoured Player{} and dropped him at {}"
                                                      .format(i+1,snakes[list_of_players[i]]))
                
                #Assigning the position of the tail of the snake to the player.
                list_of_players[i]=snakes[list_of_players[i]]
                
            #In case the player lands on a ladder.
            if(list_of_players[i] in ladders.keys()):
                print("Player {} climbed a ladder and reached {}\n"
                                                      .format(i+1,ladders[list_of_players[i]]))
                
                #Assigning the position of the top of the ladder to the player.
                list_of_players[i]=ladders[list_of_players[i]]

        if(100 in list_of_players):
            break
    print("\nCurrent scores are {}".format(list_of_players))
         

print("The winner is Player {}.🎉🎉".format(i+1))    
