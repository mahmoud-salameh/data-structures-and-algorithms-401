from graph_depth_first.graph_depth_first import *



def test_happy_path():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('H')
    graph.add_vertex('F')

    graph.add_edge('A','B')
    graph.add_edge('A','D')
    graph.add_edge('B','D')
    graph.add_edge('B','C')
    graph.add_edge('B','A')
    graph.add_edge('D','F')
    graph.add_edge('D','H')
    graph.add_edge('D','E')
    graph.add_edge('D','A')
    graph.add_edge('C','G')
    graph.add_edge('C','B')
    graph.add_edge('G','C')
    graph.add_edge('E','D')
    graph.add_edge('H','D')
    graph.add_edge('F','D')
    actual = graph.depth_first('A')
    expected = ['A', 'B', 'D', 'F', 'H', 'E', 'C']
    assert actual == expected


def test_expected_failure():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('H')
    graph.add_vertex('F')

    graph.add_edge('A','B')
    graph.add_edge('A','D')
    graph.add_edge('B','D')
    graph.add_edge('B','C')
    graph.add_edge('B','A')
    graph.add_edge('D','F')
    graph.add_edge('D','H')
    graph.add_edge('D','E')
    graph.add_edge('D','A')
    graph.add_edge('C','G')
    graph.add_edge('C','B')
    graph.add_edge('G','C')
    graph.add_edge('E','D')
    graph.add_edge('H','D')
    graph.add_edge('F','D')
    actual = graph.depth_first('A')
    expected = ['A', 'B', 'D', 'F', 'H', 'C', 'E']
    assert actual != expected