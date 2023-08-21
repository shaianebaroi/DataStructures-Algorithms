#TASK01
#FUNCTION CODE
import random
def input_players():
    list_of_players = []
    count = 0
    while (count < 3): 
        list_of_players.append(input("Please enter the name of the player: "))
        count += 1
    return (list_of_players)
    print ("The music is playing...")
    
def playing (source, k = 1):
    #GENERATING A RANDOM NUMBER
    number = random.randint(0, 3)
    
    while (len(source) != 1):
        #GENERATING A RANDOM NUMBER
        number = random.randint(0, 3)
        
        if (number == 1):
            input ("The music has stopped. Press enter to know which players remain! ")
            limit = int(len(source) / 2)
            source[limit] = None
            #print (source)
            
            #PLAYERS-REMAINING
            print ("Players remaining: ")
            count = 0
            players_remaining = []
            while (count < len(source)):
                if (source[count] != None):
                    players_remaining.append(source[count])
                count += 1
            count2 = 0
            while (count2 < len(players_remaining)):
                print (players_remaining[count2])
                count2 += 1 
            source = players_remaining

        #RIGHT-ROTATING
        #STORING THE LAST K VALUES
        temp = [0] * k
        count = len(source) - k
        count2 = 0
        while (count < len(source)):
            temp[count2] = source[count]
            count += 1
            count2 += 1
        
        #print (temp)
        
        #SHIFTING
        count = len(source) - 1
        while (count > 0):
            source[count] = source[count-k]
            count -= 1
        
        #REPLACING FIRST VALUE WITH LAST VALUE
        
        count2 = 0
        while (count < len(temp)):
            source[count] = temp[count]
            count += 1
        print (source)
    
    if (len(source) == 1):
        print ("The winner is : " + source[0])

#MAIN CODE
players = input_players()
playing(players)