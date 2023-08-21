#TASK01

#------------------------------- NODE CLASS --------------------------------
class Node:
    
    def __init__ (self, element = None, next = None):
        self.element = element
        self.next = next
        
    def printNode (self):
        print (self.element, "-", self.next)
        
#---------------------------- LINKED LIST CLASS ----------------------------- 

#TASK02 
        
class MyList:
    
    #CONSTRUCTORS 
    def __init__ (self, source = None):
        
        #1(A) USING NO PARAMETERS           
        if (source == None): 
            self.head = None
        
        #1(B) USING ARRAY AS A PARAMETER 
        elif (type(source) == type(list())):
            self.head = None
            tail = None 
              
            count = 0
            while (count < len(source)):            
                n = Node (source[count], None)
                
                if (self.head == None):
                    self.head = n
                    tail = n                    
                else:
                    tail.next = n
                    tail = n
                    
                count += 1
        
        #1(C) USING ANOTHER LIST AS A PARAMETER 
        elif (type(source) == type(Node())):
            #print ("object")
            self.head = source
            
        elif (type(source) == type(MyList())):
            self.head = source.head
    
    #2 SHOWLIST()
    def showList (self):
        n = self.head
        if (n == None):
            print ("Empty List")  
        while (n != None):
            n.printNode()
            n = n.next
    
    #3 ISEMPTY()       
    def isEmpty (self):
        n = self.head
        if (n == None):
            return True
        else:
            return False 
    
    #4 CLEAR()
    def clear (self):
        self.head = None
            
    #5 INSERT
    def insert_tail (self, newElement):
        node = Node (newElement, None)
        n = self.head
        while (n.next != None):
            #CHECKING IF THE KEY TO THE NEW NODE ALREADY EXISTS OR NOT
            if (n.next == node):
                print ("The key already exists!")
                break
            else:            
                n = n.next
        #print (n.next)
        n.next = node
        
        self.showList()
        
    #6 INSERTING AT A PARTICULAR INDEX
    def special_insert (self, newElement, index):
        node = Node (newElement, None)
        n = self.head
        #print (n)
        
        #CHECKING IF THE KEY TO THE NEW NODE ALREADY EXISTS OR NOT
        status = False
        while (n.next != None):            
            if (newElement == n.element):
                #print (node.element)
                print ("The key already exists!")
                status = True
                break
            else:            
                n = n.next
        
        #IF NODE HAS TO BE INSERTED IN THE VERY FIRST INDEX
        if (index == 0):
            node.next = self.head
            self.head = node            
        
        #INSERTING A NODE ANYTWHERE WITHIN THE LIST
        else:
            n = self.head
            if (status == False):
                count = 0
                while (count < index - 1):
                    #print (n.next)
                    n = n.next
                    count += 1
                node.next = n.next
                n.next = node
        self.showList()
        
    #7 REMOVING A NODE
    def remove (self, deleteKey):
        status = False
        n = self.head
        while (n != None):
            
            if (n.element == deleteKey):
                status = True
                #COPYING THE VALUES OF THE NEXT NODE INTO THIS NODE
                n2 = n
                n = n.next
                n2.element = n.element
                #COPYING THE ADDRESS OF THE NODE AFTER THE DELETED
                n2.next = n.next   
                self.showList()
                return (deleteKey)
                break
            else:
                status = False
                n = n.next
        
        if status == False:
            print ("The key was not found!")
        
        self.showList()

#TASK03
            
    #1 EVEN NUMBER
    def even_number_finder (self):
        n = self.head
        list01 = []
        while (n != None):            
            if (n.element%2 == 0):
                list01.append(n.element)
            n = n.next
        print (list01)
        
    #2 FINDING IF AN ELEMENT EXISTS IN THE LIST OR NOT 
    def element_finder (self, findElement):
        n = self.head
        status = False
        while (n != None):            
            if (n.element == findElement):
                status = True  
                break            
            n = n.next
        print (status)
        
    #3 REVERSE THE LIST
    def reverse(self):
        #FINDING OUT THE LENGTH OF THE LIST TO BE REVERSED
        length = 0
        n = self.head
        while (n.next != None):
            n = n.next
            length += 1
        
        #REVERSING PROCESS
        count = 0
        while (count <= length): 
            n = self.head
            #ACCESSING VALUES FROM THE END 
            count2 = 0
            while (count2 <= (length - count - 1)):
                n = n.next
                count2 += 1
            count += 1
            
            print (n.element, end = " ")
        print ()
        
    #4 SORTING IN ASCENDING ORDER
    def sort(self):
        #FINDING OUT THE LENGTH OF THE LIST TO BE SORTED
        length = 0
        n = self.head
        while (n.next != None):
            n = n.next
            length += 1
        
        #SORTING PROCESS
        count = 0
        while (count <= length):
            before = None
            n = self.head
            after = n.next
            
            #FINDING THE MAXIMUM
            while (after != None):
                if (n.element > after.element):
                    #MAXIMUM OR NOT CONDITIONS
                    if (before == None):
                        self.head = after
                        n.next = after.next
                        after.next=n
                    else:
                        before.next = after
                        n.next = after.next
                        after.next = n
                        
                #SWAPPING CONDITIONS        
                before = n
                n = after
                after = after.next
                count += 1
                
        #PRINTING CONDIIONS
        n = self.head 
        while (n != None):
            print (n.element, end = " ")
            n = n.next
        print ()
    
    #5 FINDING THE SUM OF ALL THE ELEMENTS IN THE LIST
    def summation (self):
        n = self.head
        summ = 0
        while (n != None):
            summ += n.element
            n = n.next 
        print(summ)
    
    #6 ROTATING THE ELEMENTS OF THE LIST K TIMES
    def rotate_k (self, source, side, k):
        self.source = source
        self.side = side 
        
        #CONDITIONS FOR LEFT-ROTATE BY K TIMES
        if (side == "left"):
            count = 0
            while (count < k):
                n = self.head
                #MOVING THE POINTER TO THE KTH NODE FROM THE END
                while (n.next != None):
                    n = n.next
                
                #MAKING THAT NODE THE HEAD NODE AND THE REST AFTER IT 
                n.next = self.head
                self.head = self.head.next
                n.next.next = None
                count += 1
        
        #CONDITIONS FOR RIGHT-ROTATE BY K TIMES
        elif (side == "right"):
            count = 0
            while (count < k):
                before = None
                n = self.head
                #MOVING THE POINTER TO THE KTH NODE FROM THE END
                while (n.next != None):
                    before = n
                    n = n.next

                #MAKING THAT NODE THE HEAD NODE AND THE REST AFTER IT
                before.next = None
                n.next = self.head
                self.head = n
                
                count += 1
        
        self.showList()

#------------------------------- TESTER CLASS -------------------------------
#INPUTS
list01 = [2, 4, 6, 8, 10]
list02 = [20, 40, 60, 80, 100]
list03 = [1, 2, 5, 3, 8]
list04 = [101, 120, 25, 91, 87, 1]
list05 = [25, 91, 87, 1]

#TASK02

#INVOKING THE CLASS USING DIFFERENT CONSTRUCTORS
list1 = MyList()
list1.showList()
list1 = MyList(list01)
list1.showList()
list2 = MyList(list1.head)
list2.showList()

#INVOKING THE CLASS FOR OTHER SAMPLES
list2 = MyList(list02)
list3 = MyList(list03)
list4 = MyList(list04)
list5 = MyList(list05)

#SUBTASK02
list1.showList()

#SUBTASK03
print(list1.isEmpty())

#SUBTASK04
list1.clear()
list1.showList()
print(list1.isEmpty())

#SUBTASK05
list2.insert_tail(120)

#SUBTASK06
list2.special_insert(90, 4)

#SUBTASK07
print(list2.remove(90))

#TASK03

#SUBTASK01
list3.even_number_finder()
list4.even_number_finder()

#SUBTASK02
list3.element_finder(7)
list5.element_finder(87)

#SUBTASK03
list3.reverse()

#SUBTASK04 
list3.sort()

#SUBTASK05
list3.summation()

#SUBTASK06
list3.rotate_k(list03, 'left', 2)
list3.rotate_k(list03, 'right', 2)