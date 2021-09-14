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
  
  def add_vertex(self, value):
    """ 
    Adds a vertex to the graph
    arguments
    vertex: Vertex
    """
    vertex = Vertix(value)
    self._adjacency_list[vertex.value] = []
    return vertex.value


  def add_edge(self, vertex1, vertex2, weight=1):
    """ 
    Adds an edge to our graph
    """  
    all_vertix=self._adjacency_list.keys()
    if not vertex1 in all_vertix and not vertex2 in all_vertix:
        return 'Both vertex are not in the Graph'
    elif not vertex1 in all_vertix:
        return 'The first vertex is not in the Graph'
    elif not vertex2 in all_vertix:
        return 'The seconde vertex is not in the Graph'
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
        return 'None'
  
  def size(self):
    return len(self._adajacency_list)


  def depth_first(self, start_vertix):
    array = []
    def helper(vertex):
        array.append(vertex)
        neighbors = self.get_neighbors(vertex)
        for neighbor in neighbors:
            if neighbor[0] not in array:
                helper(neighbor[0])
    helper(start_vertix)
    return array



  