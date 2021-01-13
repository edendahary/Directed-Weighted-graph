import unittest
from math import inf

from Ex3.src.DiGraph import DiGraph
from Ex3.src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        for i in range(9):
            graph.add_edge(i, i + 1, 3)

        self.ga = GraphAlgo(graph)

    def test_Save_and_load(self):
        file_name = "ga.json"
        self.ga.save_to_json(file_name)
        la = GraphAlgo()
        la.load_from_json("ga.json")
        self.assertEqual(self.ga.Graph, la.Graph)

    def test_shortest_path(self):
        self.assertEqual(self.ga.shortest_path(0, 1), [3.0, [0, 1]])
        self.assertEqual(self.ga.shortest_path(0, 0), [inf, []])
        self.assertEqual(self.ga.shortest_path(0, 9), [27.0, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
        self.ga.Graph.add_edge(0, 9, 5)
        self.assertEqual(self.ga.shortest_path(0, 9), [5.0, [0, 9]])

    def test_connected_components(self):
        self.assertEqual(self.ga.connected_components(), [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
        self.ga.Graph.add_edge(1, 0, 5)
        self.assertEqual(self.ga.connected_components(), [[0, 1], [2], [3], [4], [5], [6], [7], [8], [9]])
        self.assertEqual(self.ga.connected_component(0), [0, 1])
        empty_graph = GraphAlgo()
        self.assertEqual(empty_graph.connected_components(), [])
