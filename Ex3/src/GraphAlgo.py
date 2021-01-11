from Ex3.src.GraphAlgoInterface import GraphAlgoInterface
from Ex3.src.GraphInterface import GraphInterface
from Ex3.src.DiGraph import DiGraph
from Ex3.src.DiGraph import NodeData
import queue
from typing import List
from math import inf
import json


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph):
        self.Graph = graph

    def get_graph(self) -> GraphInterface:
        return self.Graph

    def load_from_json(self, file_name: str) -> bool:
        load_graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                Nodes = my_dict["Nodes"]
                Edges = my_dict["Edges"]
                for n in Nodes:
                    node_key = n.get("id")
                    pos = n.get("pos")
                    if pos is None:
                        load_graph.add_node(node_key, None)
                        continue
                    if isinstance(pos, str):
                        x, y, z = pos.split(",")
                    else:
                        x = pos[0]
                        y = pos[1]
                        z = pos[2]
                    pos = (float(x), float(y), float(z))
                    load_graph.add_node(node_key, pos)
                for e in Edges:
                    load_graph.add_edge(e.get("src"), e.get("dest"), e.get("w"))

        except IOError as e:
            print(e)
            return False

        self.Graph = load_graph
        return True

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as file:
                Nodes = []
                Edges = []
                for n in self.Graph.get_all_v().keys():
                    for d, w in self.Graph.all_out_edges_of_node(n).items():
                        edge = {"src": n, "w": w, "dest": d}
                        Edges.append(edge)
                for i in self.Graph.get_all_v().values():
                    curr_node = {"pos": i.getPos(), "id": i.getKey()}
                    Nodes.append(curr_node)
                json.dump({"Edges": Edges, "Nodes": Nodes}, fp=file)
            # json.dump(self.Graph, default=lambda m: m.__dict__, indent=4, fp=file)
        except IOError as e:
            print(e)
            return False
        return True

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

    def dfs_algo(self) -> list:
        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * (len(self.get_graph().get_all_v().values()))
        # Fill vertices in stack according to their finishing
        # times
        for i in range(len(self.get_graph().get_all_v().values())):
            if not visited[i]:
                self.fillOrder(i, visited, stack)

                # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (len(self.get_graph().get_all_v()))
        strong_lists = []
        count = 0
        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                l = []
                gr.DFSUtil(i, visited, l)
                strong_lists.insert(count, l)
                count += 1

        return strong_lists

    def connected_component(self, id1: int) -> list:
        if self.Graph.getNode(id1) is None:
            return None
        lists = self.dfs_algo()
        max_list = []
        for i in lists:
            if i.__contains__(id1):
                if len(i) > len(max_list):
                    max_list = i
        return max_list

    def connected_components(self) -> List[list]:
        lists = []
        index = 0
        for i in self.dfs_algo():
            if len(i) > 0:
                lists.insert(index, i)
            index += 1
        return lists

    def DFSUtil(self, v: int, visited: list, l: list):
        # Mark the current node as visited and print it
        visited[v] = True
        l.append(v)
        # Recur for all the vertices adjacent to this vertex
        cur_node = self.Graph.getNode(v)
        for i in cur_node.getOut():
            if not visited[i]:
                self.DFSUtil(i, visited, l)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        curr_node = self.Graph.getNode(v)
        # Recur for all the vertices adjacent to this vertex
        for i in curr_node.getOut():
            if not visited[i]:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        tempG = DiGraph()
        ga = GraphAlgo(tempG)
        for i in self.Graph.get_all_v().values():
            ga.Graph.add_node(i.getKey(), i.getPos())
        # Recur for all the vertices adjacent to this vertex
        for i in self.Graph.get_all_v():
            curr_node = self.Graph.getNode(i)
            for j in curr_node.getOut():
                ga.Graph.add_edge(j, i, 0)
        return ga



