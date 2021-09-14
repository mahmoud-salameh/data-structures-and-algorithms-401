class Vertex:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return f'Vertix > {self.value}'
        
class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight
# edge1 = Edge(vertex)

class Graph:
  def __init__(self):
    self._adjacency_list = {
    # vertux: [edge1, edge2]
}
  
  def add_vertex(self, vertex: Vertex):
    """ 
    Adds a vertex to the graph
    arguments
    vertex: Vertex
    """
    vertex = Vertix(value)
    self.adjacency_list[vertex] = []
    return vertex

  def add_edges(self, vertex1, vertex2, weight=1):
    """ 
    Adds an edge to our graph
    """  
    pass
  
  def get_nodes(self):
    array=[]
    for vertix in self.adjacency_list.keys():
        array.append(vertix)
    if len(array)==0:
        return None
    return array

  def get_neighbors(self, vertex):
    array=[]
    if vertex in self.adjacency_list :
        for edge in self.adjacency_list[vertex]:
            array.append((edge.vertix, edge.weight))
        return array
    if len(array)==0:
        return None
  
  def size(self):
    return self._adajacency_list
  
#   def _breadthFirst(self, action=lambda x: print(x)):
#     """ 
#     Performs a level order traversal of the graph and calls action at each node
#     """

#     # ALGORITHM BreadthFirst(vertex)
#     def BreadthFirst(self, vertex):
#     # DECLARE nodes <-- new List()
#         nodes = new_list()
#     # DECLARE breadth <-- new Queue()
#         breadth = new_queue()
#     # DECLARE visited <-- new Set()
#         visited = new_set()
#     # breadth.Enqueue(vertex)
#         breadth.Enqueue(vertex)
#     # visited.Add(vertex)
#         visited.add(vertex)
#     # while (breadth is not empty)
#         while breadth:
#     #     DECLARE front <-- breadth.Dequeue()
#             front = breadth.Dequeue()
#     #     nodes.Add(front) # call action here
#             nodes.add(front)
#     #     for each child in front.Children
#         for child in front.Children:
# #         if(child is not visited)
#             if child not in visited:
#     #             visited.Add(child)
#                 visited.add(child)
#     #             breadth.Enqueue(child)   
#                 breadth.Enqueue(child)
#     # return nodes;
#         return nodes

