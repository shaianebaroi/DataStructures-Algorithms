def repitition (source):
    list1 = []
    count = 0
    count2 = 0
   
    
    while (count < len(source)):
        
        list1.append([source[count],1])
        
        while (count < len(source) - 1):
            
            if list1[count2][0] == source[count + 1]:
                
                list1[count2][1] += 1
                
                count += 1
                continue
            else:
                break
        count += 1
        count2 += 1
    
    status = False
    count = 1
    while (count < len(list1)): 
        temp = list1[count][1]
        count2 = count
        while (count < (len(list1))):
            if temp == list1[count2][1]:
                status = True
                
        if status:
            break
    print(status)
    
repitition([4,5,6,6,4,3,6,4])