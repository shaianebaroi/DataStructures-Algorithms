#THEORY_ASSIGNMENT_01

#----------------------- NODE CLASS ------------------------------
class Node:
    
    def __init__ (self, element = None, next = None):
        self.element = element
        self.next = next
        
    def printNode (self):
        print (self.element, "-", self.next)


# ------------------DOUBLY LINKED NODE CLASS ---------------------
class Node2:

    def __init__(self, element=None, next=None, prev=None):
        self.element = element
        self.next = next
        self.prev = prev

    def printNode(self):
        print(self.element, "-", self.next, "-", self.prev)
        
#--------------------- LINKED LIST CLASS ------------------=------ 

class MyList:
    def __init__ (self, source=None):
        
        self.head = None
        
        #USING ARRAY AS A PARAMETER 
        if (type(source) == type(list())):
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
    
        #USING ANOTHER LIST AS A PARAMETER 
        elif (type(source) == type(Node())):
            self.head = source
            
        elif (type(source) == type(MyList())):
            self.head = source.head
    
    #SHOWLIST()
    def showList (self):
        n = self.head
        if (n == None):
            print ("Empty List")  
        while (n != None):
            n.printNode()
            n = n.next

#SHOWLIST2()
def showList2 (head):
    n = head
    if (n == None):
        print ("Empty List")
    while (n != None):
        n.printNode()
        n = n.next

#--------------------------- TASKS -------------------------
#TASK03
def printDuplicate(head):
    head1 = head
    status = False
    #FIRST TRAVERSAL
    while (head1 != None):
        n = head1.next
        #SECOND TRAVERSAL WITHIN THE FIRST TRAVERSAL
        while (n != None):
            if head1.element == n.element:
                status = True
                break
            else:
                n = n.next
        if status:
            break
        head1 = head1.next
    if status:
        print(head1.element)

#TASK04
def remove_multiple_of_five (head):
    head1 = head
    prev = None
    while True:
        if head1 == None:
            break
        if (head1.element % 5 == 0):
            if (head1 == head):
                head = head1.next
            else:
                prev.next = head1.next
                head1 = head1.next
                continue
        prev = head1
        head1 = head1.next
    return head

#TASK05
def summation (list1, list2):
    #CONVERTING THE FIRST LIST FROM NODE TO STRING
    integer1 = ""
    list1 = list1.next
    while (list1 != None):
        integer1 += str(list1.element)
        list1 = list1.next
    number1 = int(integer1)

    #CONVERTING THE FIRST LIST FROM NODE TO STRING
    integer2 = ""
    list2 = list2.next
    while (list2 != None):
        integer2 += str(list2.element)
        list2 = list2.next
    number2 = int(integer2)

    #SUMMING THE TWO NUMBERS
    number = number1 + number2

    #CONVERTING THE SUMMED VALUE TO STRING
    string = str(number)

    # CONVERTING THE STR SUMMED VALUE TO NODE
    head = Node()
    n = head
    for count in string:
        n.next = Node(int(count))
        n = n.next

    return head

#TASK06
def insert (a, value):
    head = a
    while (head.next != a):
        head = head.next
    head.next = Node(value, a)

#TASK07
def insertBefore (head, elem, newElement):
    tail = head.next
    node = Node2 (newElement, None, None)
    while (tail.value != elem):
        tail = tail.next
    tail2 = tail.prev
    node.next = tail
    node.prev = tail2
    tail2.next = node
    tail.prev = node
    return head
            
#-------------------------- TESTER CLASS ---------------------------

list01 = [10, 20, 30, 25 ,42, 40, 10, 20, 60]
list02 = [2, 4, 5]
list03 = [1, 3, 6]
list1 = MyList(list01) 
list2 = MyList(list02)
list3 = MyList(list03)


list1.showList()
printDuplicate(list1.head)
list1 = MyList(list01)
list1.showList()
showList2(remove_multiple_of_five(list1.head))


list4 = MyList(summation(Node(None,list2.head), Node(None,list3.head)))
list4.showList()


list5 = Node(0,)
list5.next=Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7,list5))))))) 


insert(list5,8)
head=list5
while True:
    print(list5.element)
    list5=list5.next
    if list5==head:
        break

head = MyList([1,2,3,4]).head 

#NO MyList CLASS EXISTS FOR THIS FILE FOR DHDLCL
task7 = insertBefore(head, 3, 50)

while True:
    task7=task7.next
    if task7==None:
        break
    print(task7)