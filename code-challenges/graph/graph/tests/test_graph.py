from graph.graph import *


import pytest

def test_can_add():
    graph = Graph()
    actual = graph.add_vertex('a')
    expected=graph.get_nodes()[0]
    assert actual==expected

def test_can_addedge():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    graph.add_edge(a, b)
    actual=graph.get_neighbors(a)[0][0]
    expected=b
    assert actual==expected

def test_get_nodes():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex('d')
    e = graph.add_vertex('e')
    f = graph.add_vertex('f')
    actual=graph.get_nodes()
    expected=[a,b,c,d,e,f]
    assert actual==expected

def test_get_neighbors_node():
    graph = Graph()
    a = graph.add_vertex('a')
    c = graph.add_vertex('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][0]
    expected=c
    assert actual==expected

def test_get_neighbors_weight():
    graph = Graph()
    a = graph.add_vertex('a')
    c = graph.add_vertex('c')
    graph.add_edge(a, c)
    actual=graph.get_neighbors(a)[0][1]
    expected=1
    assert actual==expected


def test_size():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex('d')
    e = graph.add_vertex('e')
    f = graph.add_vertex('f')
    actual=graph.size()
    expected=6
    assert actual==expected

def test_only_one_node():
    graph = Graph()
    a = graph.add_vertex('a')
    actual=graph.get_neighbors(a)
    expected=[]
    assert actual==expected


def test_empty_graph():
    graph = Graph()
    actual=graph.get_nodes()
    expected=None
    assert actual==expected





@pytest.fixture
def prepared_graph():
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
    return graph

