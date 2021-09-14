
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
        return None
  
  def size(self):
    return len(self._adajacency_list)


def business_trip(graph,cites):
    trips = True
    cost = 0
    for i in range(len(cites)-1):
        for city_path in graph.get_neighbors(cites[i]):
            if cites[i+1]==city_path[0]:
                cost+=city_path[1]
    if trips == False:
        cost = 0
    return trips, cost   
