def HappyNewYear(players, sequence, count = 1, serial = 0, left = 0):
    if(serial > len(sequence)-1):
        serial = 0
    if(players <= 1):
        print(left, "is the Winner")
        return 
    if(sequence[serial] == "H"):
        if(sequence[serial+1] == "H"):
            left = count
            HappyNewYear(players, sequence, count+1, serial+2, left)
        else: # T
            HappyNewYear(players-1, sequence, count+1, serial+2, left)
    elif(sequence[serial] == "T"):
        if(sequence[serial+1] == "T"):
            left = count
            HappyNewYear(players, sequence, count+1, serial+2, left)
        else: # H
            HappyNewYear(players-1, sequence, count+1, serial+2, left)

HappyNewYear(3, "HTHH")