import unittest
from src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):

    def test_add_node(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        self.assertEqual(graph.v_size(), 10)
        graph.add_node(10)
        graph.add_node(11)
        self.assertEqual(graph.v_size(), 12)
        graph.add_node(0)
        self.assertEqual(graph.v_size(), 12)

    def test_add_edge(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        graph.add_edge(0, 1, 1.2)
        graph.add_edge(1, 2, 1.2)
        graph.add_edge(2, 3, 1.2)
        graph.add_edge(3, 4, 1.2)
        self.assertEqual(graph.Es, 4)
        graph.remove_edge(3, 4)
        self.assertEqual(graph.Es, 3)
        graph.remove_edge(3, 4)
        self.assertEqual(graph.Es, 3)
        graph.add_edge(3, 4, 2)
        self.assertEqual(graph.Es, 4)
        graph.add_edge(3, 4, 2)
        self.assertEqual(graph.Es, 4)

    def test_remove_node(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        graph.add_edge(0, 1, 1.2)
        graph.add_edge(1, 2, 1.2)
        graph.add_edge(2, 3, 1.2)
        graph.add_edge(3, 4, 1.2)
        graph.remove_node(0)
        self.assertEqual(graph.Es, 3)
        self.assertEqual(graph.v_size(), 4)
        graph.remove_node(0)
        self.assertEqual(graph.Es, 3)
        self.assertEqual(graph.v_size(), 4)

    def test_remove_edge(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        graph.add_edge(0, 1, 1.2)
        graph.add_edge(1, 2, 1.2)
        graph.add_edge(2, 3, 1.2)
        graph.add_edge(3, 4, 1.2)
        graph.remove_edge(0, 1)
        self.assertEqual(graph.Es, 3)
        self.assertEqual(graph.v_size(), 5)
        graph.remove_edge(0, 1)
        self.assertEqual(graph.Es, 3)
        self.assertEqual(graph.v_size(), 5)

    def test_get_all_v(self):
        graph = DiGraph()
        for i in range(5):
            graph.add_node(i)
        graph.add_edge(0, 1, 1.2)
        graph.add_edge(1, 2, 1.2)
        graph.add_edge(2, 3, 1.2)
        graph.add_edge(3, 4, 1.2)

        n = graph.getNode(0)
        c = graph.get_all_v()
        z = c.keys()
        self.assertTrue(z.__contains__(n.getKey()))
        c.pop(n.getKey())
        self.assertFalse(z.__contains__(n.getKey()))

    def test_all_in_edges_of_node(self):
        graph = DiGraph()
        for i in range(0, 20):
            graph.add_node(i)
        for i in range(0, 10):
            graph.add_edge(i, i + 1, 2)
        for i in graph.all_in_edges_of_node(10):
            self.assertTrue(10 in graph.all_out_edges_of_node(i))

    def test_all_out_edges_of_node(self):
        graph = DiGraph()
        for i in range(0, 20):
            graph.add_node(i)
        for i in range(0, 10):
            graph.add_edge(i, i + 1, 2)
        for i in graph.all_in_edges_of_node(10):
            self.assertTrue(10 in graph.all_out_edges_of_node(i))

    def test_mc(self):
        graph = DiGraph()
        for i in range(10):
            graph.add_node(i)
        graph.add_edge(0, 1, 1.2)
        graph.add_edge(1, 2, 1.2)
        graph.add_edge(2, 3, 1.2)
        graph.add_edge(3, 4, 1.2)
        self.assertEqual(14, graph.get_mc())
        graph.add_edge(0, 1, 1)
        self.assertEqual(14, graph.get_mc())
        graph.add_node(3)
        self.assertEqual(14, graph.get_mc())
        graph.remove_edge(0, 1)
        self.assertEqual(15, graph.get_mc())
        graph.remove_edge(0, 1)
        self.assertEqual(15, graph.get_mc())
        graph.remove_node(0)
        self.assertEqual(16, graph.get_mc())
        graph.remove_node(0)
        self.assertEqual(16, graph.get_mc())
