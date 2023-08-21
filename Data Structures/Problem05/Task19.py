#================================ NODE CLASS =================================
class Node:
    def __init__ (self, element, next):
        self.element = element
        self.next = next
        
    def printNode (self):
        print (self.element, "-", self.next)
        
#============================ LINKED LIST CLASS ==============================
class MyList():
    def __init__ (self, source):
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
    
    def counting (self):
        count = 0
        n = self.head
        while (n != None):
            count += 1
            n = n.next
        return count
    
    def showList (self):
        n = self.head
        if (n == None):
            print ("Empty List")  
        while (n != None):
            n.printNode()
            n = n.next

    def insert_begin(self, element, index = None):
        node = Node(element, None)
        node.next = self.head
        self.head = node
        #self.showList()
        
    def insert_end(self, element, index = None):
        node = Node(element, None)
        n = self.head
        while (n.next != None):
            n = n.next
        n.next = node                                                                                                              
        #self.showList()
    
    def insert_anywhere (self, element, index):
        node = Node (element, None)
        n = self.head          
        count = 0
        while (count < index - 1):
            n = n.next
            count += 1
        node.next = n.next
        n.next = node
        #self.showList()
        
    def insert (self, element, index):
        count = self.counting()
        if (index == 0):
            self.insert_begin (element)
        elif (index == count - 1):
            self.insert_end (element)
        else:
            self.insert_anywhere (element, index)
        self.showList()

#=============================== TESTER CLASS ================================
list1 = [20, 40, 60, 80, 100]

list01 = MyList(list1)
list01.insert(120,4)
