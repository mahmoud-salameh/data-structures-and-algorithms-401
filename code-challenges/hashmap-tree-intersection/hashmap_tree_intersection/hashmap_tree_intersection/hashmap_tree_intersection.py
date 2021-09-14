class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.left = None
    self.right = None


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
    arraygument: key and value 
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


class BinaryTree(object):
    def __init__(self):
        self.root = None

def intersection(tree1,tree2):
    array=[]
    hashtable = Hashtable(1024)
    if tree1.root== None or tree2.root == None:
        return 'The trees are empty'

    def search(node):
        if hashtable.contains(str(node.value)):
            nonlocal array
            array+=[node.value]
        else:
            hashtable.add(str(node.value),True)
        
        if node.left:
            search(node.left)
        if node.right:
            search(node.right)
    search(tree1.root)
    search(tree2.root)
    return array