class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        try:
           popValue = self.top.value
           self.top = self.top.next
           return popValue
        except:
            return "An empty stack"

    def peek(self):
        try:
            return self.top.value
        except:
            return "An empty stack"

    def isEmpty(self):
        return self.top == None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        node  =  Node(value)
        if not self.front:
            self.front  =  node
            self.rear  =  node
        else:
            self.rear.next  =  node
            self.rear  =  node
    
    def dequeue(self):
        try:
           dequeue_input = self.front.value
           self.front = self.front.next
           return dequeue_input
        except :
           return "An empty Queue"

    def peek(self):
        try:
           return self.front.value
        except :
            return "An empty Queue"

    def isEmpty(self):
        return self.front  ==  None
        

""" ---------------------------------------------stack-queue-pseudo tests---------------------------------------------------- """
    
class Stack:
    def __init__(self):
        self.top = None
    
    def push(self,value):
        node = Node(value)
        node.next=self.top
        self.top=node

    def pop(self):
        try:
           popValue = self.top.value
           self.top = self.top.next
           return popValue
        except:
            return 'An empty stack'

    def peek(self):
        try:
            return self.top.value
        except:
            return 'An empty stack'

    def isEmpty(self):
        return self.top == None

class PseudoQueue:
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()
    
    def enqueue(self,value=None):
        if value == None:
            return 'Please put a value'
    
        self.front.push(value)
        
    def dequeue(self):
        
        if not self.front.top:
            return 'The Queue is empty'
           
        while self.front.top:
            
       
            self.rear.push(self.front.pop())

        dequeue_value = self.rear.pop()

        while self.rear.top:
        
    
            self.front.push(self.rear.pop())

        return dequeue_value
""" ---------------------------------------------stack-queue-animal-shelter---------------------------------------------------- """
            
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, value):
        node = Node(value)
        if not self.front:

            self.front = node
            self.rear = node
        else:

            self.rear.next = node
            self.rear = node
    
    def dequeue(self):
        try:
           dequeue_value = self.front.value
           self.front = self.front.next
           return dequeue_value
        except :
           return 'The Queue is empty'

class Dog:
    def __init__(self,name):
        self.name = name
        self.kind = 'dog'

class Cat:
    def __init__(self,name):
        self.name = name
        self.kind = 'cat'

class Animal:
    def __init__(self,name,kind):
        self.name = name
        self.kind = kind


class Animal_shelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()
    
    def enqueue(self,animal):
        
        if animal.kind == 'cat':
            self.cat.enqueue(animal)
        elif animal.kind == 'dog':
            self.dog.enqueue(animal)
        else: 
            return 'the animal can be either dog or cat' 
    def dequeue(self,pref = None):
        if pref == 'cat':
            return self.cat.dequeue().name
        elif pref == 'dog':
            return self.dog.dequeue().name
        else:
            return None








    