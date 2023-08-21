def listing_alphabets(letter):
    alphabets = [0] * 36
    count = 10
    count2 = 65
    while (count <= 35 and count2 <= 90):
        alphabets[count] = chr(count2)
        count += 1
        count2 += 1
    #print (alphabets)
    
    #SEARCHING FOR THE LETTER IN THE ARRRAY
    count = 0
    while (count < len(alphabets)):
        if (alphabets[count] == letter):
            #print (count)
            return int(count)
            break
        count += 1
        

def hashtable(source):
    #LOOP FOR ALL THE ELEMENTS IN THE ARRAY
    hashtable = [0] * 11
    count2 = 0
    while (count2 < len(source)):
        string = source[count2]
        #SEPARATING ALPHABETS AND DIGITS
        alphabets = []
        digits = []
        count = 0
        while (count < len(string)):
            try:
                int(string[count])
                digits.append(string[count])
            except:
                alphabets.append(string[count])
            
            count += 1
        #print (alphabets)
        #print (digits)
        
        #FORMULATING THE HASH FUNCTION
        #SUMMATION OF ALPHABETS
        count = 0
        summation = 0
        score = 0
        while (count < len(alphabets)):
            letter = alphabets[count]
            score = listing_alphabets(str(letter))
            summation += score
            count += 1
        print ("summation - ", summation)
        
        #PRODUCT OF THE DIGITS
        count = 0
        product = 1
        while (count < len(digits)):
            product = product * int(digits[count])
            count += 1
        print ("product-", product)
        
        index = (summation - product) % 11
        print ("Index", index)
        
        #COLLISION CONDITION
        if (hashtable[index] == 0):
            hashtable[index] = string
        else:
            #FIND THE NEXT EMPTY SPACE 
            count = index
            while (count >= 0):
                #MAKING THE ARRAY CIRCULAR
                if (count == len(hashtable) - 1):
                    count = 0
                if (hashtable[count] == 0):
                    hashtable[count] = string
                    break
                count += 1
        
        count2 += 1
        
    print (hashtable)
    
#TESTER CLASS
source = []
hashtable(["C11SG2","E2E3A","2H12DE","EFE111","31GHN"])