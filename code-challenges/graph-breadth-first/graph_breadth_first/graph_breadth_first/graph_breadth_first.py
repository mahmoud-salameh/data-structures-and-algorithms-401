from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


class Vertix:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'

class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight

class Graph:
  def __init__(self):
    self._adjacency_list = {
    # vertux: [edge1, edge2]
}
  
  def add_vertex(self, vertex):
    """ 
    Adds a vertex to the graph
    arguments
    vertex: Vertex
    """
    vertex = Vertix(vertex)
    self._adjacency_list[vertex] = []
    return vertex

#   def add_edges(self, vertex1, vertex2, weight=1):
#     """ 
#     Adds an edge to our graph
#     """  
#     pass
  def add_edge(self, vertex1, vertex2, weight=1):
    """ 
    Adds an edge to our graph
    """  
    all_nodes=self._adjacency_list.keys()
    if not vertex1 in all_nodes and not vertex2 in all_nodes:
        return 'Both nodes are not in the Graph'
    elif not vertex1 in all_nodes:
        return 'The first node is not in the Graph'
    elif not vertex2 in all_nodes:
        return 'The seconde node is not in the Graph'
    
    edge = Edge(vertex2, weight)
    self._adjacency_list[vertex1].append(edge)
  def get_nodes(self):
    array=[]
    for vertix in self._adjacency_list.keys():
        array.append(vertix)
    if len(array)==0:
        return None
    return array

  def get_neighbors(self, vertex):
    array=[]
    if vertex in self._adjacency_list :
        for edge in self._adjacency_list[vertex]:
            array.append((edge.vertix, edge.weight))
        return array
    if len(array)==0:
        return None
  
  def size(self):
    return self._adajacency_list
  
#   def BreadthFirst(self,vertix, action=lambda x: print(x)):
   
    # ALGORITHM BreadthFirst(vertex)
    # DECLARE nodes <-- new List()
    # DECLARE breadth <-- new Queue()
    # DECLARE visited <-- new Set()
    # breadth.Enqueue(vertex)
    # visited.Add(vertex)
    # while (breadth is not empty)
    #     DECLARE front <-- breadth.Dequeue()
    #     nodes.Add(front) # call action here
    #     for each child in front.Children
    #         if(child is not visited)
    #             visited.Add(child)
    #             breadth.Enqueue(child)   
    # return nodes;
  def BreadthFirst(self, vertex):
    """ 
    Performs a level order traversal of the graph and calls action at each node
    """
    if vertex not in self._adjacency_list:
        return 'This node is not in the graph'
        nodes = new_list()
        breadth = new_queue()
        visited = new_set()
        breadth.enqueue(vertex)
        visited.add(vertex)
        while breadth:
            front = breadth.dequeue()
            nodes.append(front)
        for child in front.Children:
            if child not in visited:
                visited.add(child)
                breadth.enqueue(child)
        return nodes
