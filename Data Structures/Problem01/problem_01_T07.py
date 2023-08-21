#TASK07
#FUNCTION CODE

def bunch (source):
    
    #TAKING ONE ELEMENT AND COMPARING IT WITH OTHER TO FIND COMMONS
    count = 0
    max_bunch = 0
    count2 = 0
    while (count < len(source) - 1):
        
        
        bunch = 1
        while (count2 < len(source) - 1):           
        
            if (source[count2] == source[count2 + 1]):
                bunch += 1
                count2 += 1
                
            else:
                count2 += 1
                break
                            
        if bunch > max_bunch:
            max_bunch = bunch
        
        count += 1
        
    print (max_bunch)
            
            
#MAIN CODE
bunch ([1, 2, 2, 2, 2, 2, 3, 4, 4, 4, 4])
