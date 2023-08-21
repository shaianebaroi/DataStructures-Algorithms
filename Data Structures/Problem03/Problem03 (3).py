#TASK01

#------------------------------- NODE CLASS --------------------------------
class Node:
    
    def __init__ (self, element = None, next = None, prev = None):
        self.element = element
        self.next = next
        self.prev = prev
        
    def printNode (self):
        print (self.element, "-", self.next)
        
#---------------------------- LINKED LIST CLASS ----------------------------- 

#TASK02 
        
class DoublyList:
    
    #CONSTRUCTORS 
    head = Node (None, None, None)
    
    def __init__ (self, source = None):
        
        #USING ARRAY AS A PARAMETER 
        #CREATING THE DUMMY NODE 
        self.head.next = self.head.prev
        self.head.prev = self.head
           
        
        #ITERATING TO CONVERT ARRAY INTO NODES
        n = self.head.next 
        count = 0
        temp = self.head
        while (count < len(source)):            
            n = Node (source[count], None, None)
            
            n.next = self.head
            n.prev = temp
            temp.next = n
            self.head.prev = n
            temp = temp.next
                
            count += 1
        
    #2 SHOWLIST()
    def showList (self):
        n = self.head.next
        if (n == None):
            print ("Empty List")  
        while (n != self.head):
            n.printNode()
            n = n.next
            
    #4 INSERTING AT A PARTICULAR INDEX
    def insert_index (self, newElement, index):
        node = Node (newElement, None)
        n = self.head.next

        #CHECKING IF THE KEY TO THE NEW NODE ALREADY EXISTS OR NOT
        length = 0
        status = False
        while (n.next != self.head):            
            if (newElement == n.element):
                #print (node.element)
                print ("The key already exists!")
                status = True
                break
            else:            
                n = n.next
            length += 1

        n = self.head.next
        if (status == False):
            if (index == 0):
                index = length + 2
            count = 0
            while (count < index - 1):
                #print (n.next)
                n = n.next
                count += 1
            
            node.next = n.next
            n.next = node
            node.prev = n
        self.showList()
        
    #3 INSERT
    def insert_end (self, newElement):
        n = self.head.next
        
        #LENGTH OF THE ARRAY
        length = 1
        while (n.next != self.head):            
            n = n.next
            length += 1
        #print (length)
            
        self.insert_index(newElement, length)

        
        #self.showList()
    
    #4 INSERTING AT A PARTICULAR INDEX
    def insert_index (self, newElement, index):
        node = Node (newElement, None)
        n = self.head.next

        #CHECKING IF THE KEY TO THE NEW NODE ALREADY EXISTS OR NOT
        length = 0
        status = False
        while (n.next != self.head):            
            if (newElement == n.element):
                #print (node.element)
                print ("The key already exists!")
                status = True
                break
            else:            
                n = n.next
            length += 1

        n = self.head.next
        if (status == False):
            if (index == 0):
                index = length + 2
            count = 0
            while (count < index - 1):
                #print (n.next)
                n = n.next
                count += 1
            
            node.next = n.next
            n.next = node
            node.prev = n
        self.showList()
        
    #5 REMOVING A NODE AT A PARTICULAR INDEX
    def remove_index (self, index):
        n = self.head.next
        
        #LENGTH OF THE ARRAY
        length = 0
        while (n.next != self.head):            
            n = n.next
            length += 1
        #print (length)
        
        if (index == 0):
            index = length  + 1
        #print (index)
        
        n = self.head.next
        count = 0
        while (count < index + 1):
            #print (n.next)
            n = n.next
            count += 1
        
        temp = n
        #print (temp)
        n = self.head.next
        count = 0
        while (count < index - 1):
            #print (n.next)
            n = n.next
            count += 1
        n.next = temp

        self.showList()
        
        #4 INSERTING AT A PARTICULAR INDEX
    def remove_key (self, deleteKey):
        n = self.head.next
        
        #LENGTH OF THE ARRAY
        length = 1
        while (n.next != self.head):            
            n = n.next
            length += 1
        #print (length)
        
        n = self.head.next  
        count = 0
        index = 0 
        while (n.next != self.head):            
            if (n.element == deleteKey):
                index = count
                #print (count)
                break
            else: 
                n = n.next
                count += 1
        #print (count)
        if count == 0:
            index = length + 1
            
        self.remove_index(index)
    
#------------------------------- TESTER CLASS -------------------------------
#INPUTS
list01 = [2, 4, 6, 8, 10]

#INVOKING THE CLASS USING DIFFERENT CONSTRUCTORS
list1 = DoublyList(list01)
list1.showList()
list1.insert_end(12)
list1.insert_index(3, 1)
list1.remove_index(6)
list1.remove_key(3)