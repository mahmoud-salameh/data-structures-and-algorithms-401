from graph_breadth_first.graph_breadth_first import Graph, Vertix
import pytest

def test_happy_path():
    graph = Graph()
    pandora= graph.add_vertex('pandora')
    arendelle= graph.add_vertex('arendelle')
    metroville= graph.add_vertex('metroville')
    narina= graph.add_vertex('narina')
    naboo= graph.add_vertex('naboo')
    manstropolis= graph.add_vertex('manstropolis')
    graph.add_edge(pandora,arendelle)
    graph.add_edge(arendelle,pandora)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(metroville,arendelle)
    graph.add_edge(metroville,manstropolis)
    graph.add_edge(metroville,naboo)
    graph.add_edge(metroville,narina)
    graph.add_edge(narina,metroville)
    graph.add_edge(narina,naboo)
    graph.add_edge(naboo,narina)
    graph.add_edge(naboo,metroville)
    graph.add_edge(naboo,manstropolis)
    graph.add_edge(manstropolis,naboo)
    graph.add_edge(manstropolis,arendelle)
    graph.add_edge(manstropolis,metroville)
    actual=graph.BreadthFirst(pandora)
    expected=None
    assert actual==expected



def test_edge_case():
    graph = Graph()
    pandora=Vertix('pandora')
    actual=graph.BreadthFirst(pandora)
    expected='This node is not in the graph'
    assert actual==expected

def test_expected_failure():
    graph = Graph()
    pandora= graph.add_vertex('pandora')
    arendelle= graph.add_vertex('arendelle')
    metroville= graph.add_vertex('metroville')
    narina= graph.add_vertex('narina')
    naboo= graph.add_vertex('naboo')
    manstropolis= graph.add_vertex('manstropolis')
    graph.add_edge(pandora,arendelle)
    graph.add_edge(arendelle,pandora)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(arendelle,metroville)
    graph.add_edge(metroville,arendelle)
    graph.add_edge(metroville,manstropolis)
    graph.add_edge(metroville,naboo)
    graph.add_edge(metroville,narina)
    graph.add_edge(narina,metroville)
    graph.add_edge(narina,naboo)
    graph.add_edge(naboo,narina)
    graph.add_edge(naboo,metroville)
    graph.add_edge(naboo,manstropolis)
    graph.add_edge(manstropolis,naboo)
    graph.add_edge(manstropolis,arendelle)
    graph.add_edge(manstropolis,metroville)

    actual=graph.BreadthFirst(pandora)
    expected=[pandora,arendelle,metroville,manstropolis,narina,naboo]
    assert actual!=expected