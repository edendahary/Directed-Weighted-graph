import unittest

from Ex3.src.DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_node(5)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
