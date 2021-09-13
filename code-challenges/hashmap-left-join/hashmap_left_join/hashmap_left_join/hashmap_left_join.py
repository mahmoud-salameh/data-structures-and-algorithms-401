class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    
  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)
    
  def insert(self, value):
    node = Node(value)
    if self.head:
        node.next = self.head
    self.head = node

class LinkedList:
  def __init__(self):
    self.head = None



  def includes(self,vlaue):
    current=self.head
    while current :
        if vlaue ==current.value[0]:
            return True
        current=current.next
    return False

  def append(self,value):
    new_node=Node(value)

    if self.head == None:
        self.head = new_node
    else:
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

class Hashtable:
  def __init__(self, size = 1024):
    self.size = size
    self._buckets = [None]*size 
    
  def hash(self,key):
    '''Get the index number of the key string and it take the key as a parameter
    return: number
    '''
    value=0
    for x in key:
      value += ord(x)
    index = (value * 7) % self.size   
    return index
    
  def add(self,key,value):
    '''add a value to the hashtable by its key 
    parameters:
        key: a string
        value: any type
    Arrgument: key and value 
    return: nothing

    '''
    index = self.hash(key) 

    if not self._buckets[index]:
      self._buckets[index] = LinkedList()
      

    self._buckets[index].append([key,value])

  def contains(self,key):
    """this function will check if the there is a value for the key 
    parameters:
      key: a string
    return: a boolean
    """
    index=self.hash(key)
    if self._buckets[index]:
      return self._buckets[index].includes(key)
    else:
      return False

  def get(self,key):
    """this function will search in the hashtable about the key and return the value
    parameters:
      key: a string
    return: the value 
      """
    index = self.hash(key)
    if self._buckets[index] == None:
        return None
    else:
        current=self._buckets[index].head
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next


def left_join(hashmap1,hashmap2):
    array=[]
    if hashmap1._buckets == hashmap1.size*[None] or hashmap2._buckets == hashmap2.size*[None] :
        return 'The hashtable are empty'
    for item in hashmap1._buckets:
        if item:
            array_2=[]
            array_2.append(item.head.value[0])
            array_2.append(hashmap1.get(item.head.value[0]))
            array_2.append(hashmap2.get(item.head.value[0]))
            array.append(array_2)
    return array

