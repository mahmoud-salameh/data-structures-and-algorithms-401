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
  def BreadthFirst(self, vertex):
    """ 
    Performs a level order traversal of the graph and calls action at each node
    """
    if vertex not in self._adjacency_list:
        return 'This node is not in the graph'
    # DECLARE nodes <-- new List()
        nodes = new_list()
    # DECLARE breadth <-- new Queue()
        breadth = new_queue()
    # DECLARE visited <-- new Set()
        visited = new_set()
    # breadth.Enqueue(vertex)
        breadth.enqueue(vertex)
    # visited.Add(vertex)
        visited.add(vertex)
    # while (breadth is not empty)
        while breadth:
    #     DECLARE front <-- breadth.Dequeue()
            front = breadth.dequeue()
    #     nodes.Add(front) # call action here
            nodes.append(front)
    #     for each child in front.Children
        for child in front.Children:
    #         if(child is not visited)
            if child not in visited:
    #             visited.Add(child)
                visited.add(child)
    #             breadth.Enqueue(child)   
                breadth.enqueue(child)
    # return nodes;
        return nodes


if __name__ == '__main__':

    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex('d')
    e = graph.add_vertex('e')
    f = graph.add_vertex('f')
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(b, f)
    graph.add_edge(c, a)
    graph.add_edge(c, b)
    graph.add_edge(c, e)
    graph.add_edge(d, a)
    graph.add_edge(d, e)
    graph.add_edge(e, c)
    graph.add_edge(e, d)
    graph.add_edge(e, f)
    graph.add_edge(f, b)
    graph.add_edge(f, e)
    # print(graph.get_nodes())

    graph2 = Graph()

    pandora= graph2.add_vertex('pandora')
    arendelle= graph2.add_vertex('arendelle')
    metroville= graph2.add_vertex('metroville')
    narina= graph2.add_vertex('narina')
    naboo= graph2.add_vertex('naboo')
    manstropolis= graph2.add_vertex('manstropolis')

    graph2.add_edge(pandora,arendelle)
    graph2.add_edge(arendelle,pandora)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(arendelle,metroville)
    graph2.add_edge(metroville,arendelle)
    graph2.add_edge(metroville,manstropolis)
    graph2.add_edge(metroville,naboo)
    graph2.add_edge(metroville,narina)
    graph2.add_edge(narina,metroville)
    graph2.add_edge(narina,naboo)
    graph2.add_edge(naboo,narina)
    graph2.add_edge(naboo,metroville)
    graph2.add_edge(naboo,manstropolis)
    graph2.add_edge(manstropolis,naboo)
    graph2.add_edge(manstropolis,arendelle)
    graph2.add_edge(manstropolis,metroville)

    print(graph2.BreadthFirst(pandora))