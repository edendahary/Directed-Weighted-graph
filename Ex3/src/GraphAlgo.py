from Ex3.src.GraphAlgoInterface import GraphAlgoInterface
from Ex3.src.GraphInterface import GraphInterface
from Ex3.src.DiGraph import DiGraph
from Ex3.src.DiGraph import NodeData
import queue
from math import inf

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        self.Graph = graph

    def get_graph(self) -> GraphInterface:
        return self.Graph

  #  def load_from_json(self, file_name: str) -> bool:

   # def save_to_json(self, file_name: str) -> bool:

    def dijkstra(self, id1: int, id2: int) -> (float, dict):
        dist = {}
        perv = {}
        q = queue.PriorityQueue()
        for i in self.Graph.Nodes:
            curr = self.Graph.getNode(i)
            curr.setTag(i)
            curr.setInfo("in_queue")
            if curr.getKey() == id1:
                dist[i] = 0
            else:
                dist[i] = inf
            q.put(curr.getKey())
        while not q.empty():
            n = q.get()
            curr_node = self.Graph.getNode(n)
            curr_node.setInfo("not_in_queue")
            edges = self.Graph.getNode(n).out
            for i in edges:
                curr_edge = self.Graph.getNode(i)
                if curr_edge.getInfo().__eq__("in_queue"):
                    alt = dist.get(n) + edges.get(i)
                    if alt < dist.get(curr_edge.getKey()):
                        dist[curr_edge.getKey()] = alt
                        perv[curr_edge.getKey()] = curr
                        q.get(curr_edge.getKey())
                        q.put(curr_edge.getKey())
        return dist[self.Graph.getNode(id2).getKey()], perv

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 == id2:
            return inf, None
        path = self.dijkstra(id1, id2)
        if path[0] == inf:
            return inf, []

        return path
    def fillOrder(self, node: NodeData , q: queue):
        node.setInfo("True")
        for i in node.out:
            curr = self.Graph.getNode(i)
            if curr.getInfo.__eq__("False"):
                self.fillOrder(curr, q)
        q.put(node)
    def get_transpose(self):
        ga = GraphAlgo(self.get_graph())
        for i in ga.Graph.get_all_v().values():
            for n in i.getOut():
                curr = self.Graph.getNode(n)
                if curr is None:
                    continue
                curr.AddGetOut(i,0)
        return ga

    def DFSUtill(self, node: NodeData):
        node.setInfo("True")
        for i in self.Graph.get_all_v().values():
            if i.getInfo.__eq__("False"):
                self.DFSUtil(i)

    def connected_component(self, id1: int) -> list:
        q = queue.Queue()
        parent = {}
        src_node = self.Graph.getNode(id1)
        nodes = self.Graph.get_all_v()
        for i in nodes.values():
            i.setInfo("False")
            parent[i.getKey()] = None
        for i in nodes.values():
            if i.getInfo().__eq__("False"):
                self.fillOrder(i, q)
        gt = self.get_transpose()

        nodes_transpose = gt.Graph.get_all_v().values()
        for i in nodes_transpose.values():
            i.setInfo("False")

        while not q.empty():
            v = q.get()
            if v.getInfo().__eq__("False"):
                gt.DFSUtill(v)









if __name__ == '__main__':
        a = DiGraph()
        a.add_node(0)
        a.add_node(1)
        a.add_node(2)
        a.add_node(3)
        a.add_edge(0, 1, 5)
        a.add_edge(1, 2, 6)
#    a.add_edge(2, 3, 7)
#   a.add_edge(0, 3, 2)

        ga = GraphAlgo(a)
        d = ga.connected_component(0)
        d = 0










