import heapq
import random

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
from typing import List
from math import inf
import json
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: GraphInterface = None):
        self.Graph = g

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
        except IOError as e:
            print(e)
            return False
        return True

    def dijkstra(self, id1: int, id2: int) -> (float, dict):
        dist = {}
        perv = {}
        h = []
        heapq.heappush(h, (0, id1))
        for i in self.Graph.Nodes:
            curr = self.Graph.getNode(i)
            curr.setTag(inf)
            curr.setInfo("in_queue")
            if curr.getKey() == id1:
                dist[i] = 0
                curr.setTag(0)
            else:
                dist[i] = inf
        while len(h) != 0:
            currcost, currvertx = heapq.heappop(h)
            curr_node = self.Graph.getNode(currvertx)
            curr_node.setInfo("not_in_queue")
            edges = self.Graph.getNode(currvertx).out
            for i in edges:
                curr_edge = self.Graph.getNode(i)
                if curr_edge.getInfo().__eq__("in_queue"):
                    alt = dist.get(currvertx) + edges.get(i)
                    if alt < dist.get(curr_edge.getKey()):
                        dist[curr_edge.getKey()] = alt
                        perv[curr_edge.getKey()] = currvertx
                        heapq.heappush(h, (currcost + edges.get(i), curr_edge.getKey()))
        return dist[self.Graph.getNode(id2).getKey()], perv

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        s_p = []
        if id1 not in self.Graph.get_all_v().keys() or id2 not in self.Graph.get_all_v().keys():
            return [inf, s_p]
        if id1 == id2:
            return [inf, s_p]
        path = self.dijkstra(id1, id2)
        if path[0] == inf:
            return inf, []
        p = path[1]
        s_p.append(id2)
        x = p.get(id2)
        i = p.get(id2)
        while len(p) != 0:
            s_p.append(i)
            i = p.get(i)
            if i is None:
                break
            p.pop(x)
            x = i
        l = s_p
        l.reverse()
        k = [float(path[0]), l]
        return k

    def connected_components(self) -> List[list]:
        lists = []
        flag = True
        if self.Graph is not None:
            if self.Graph.v_size() > 0:
                for i in self.Graph.get_all_v().keys():
                    if flag:
                        list1 = self.connected_component(i)
                        lists.append(list1)
                        flag = False
                    if i not in list1:
                        list1 = self.connected_component(i)
                        lists.append(list1)
        return lists

    def connected_component(self, id1: int) -> list:
        if self.Graph.getNode(id1) is None:
            return []
        list_scc = self.dfs_algo(id1)
        list_transpose_scc = self.graph_transpose(id1)
        result = []
        for i in list_scc:
            if list_transpose_scc.__contains__(i):
                result.append(i)
        return result

    def graph_transpose(self, src: int) -> list:

        transpose_src_scc = []
        list_of_src = [src]
        visited = [False] * (len(self.get_graph().get_all_v().values()))
        visited[src] = True
        while list_of_src:
            curr_src = list_of_src.pop(0)
            if self.Graph.all_in_edges_of_node(curr_src) is not None:
                for i in self.Graph.all_in_edges_of_node(curr_src).keys():
                    if visited[i] is False:
                        visited[i] = True
                        list_of_src.append(i)
            transpose_src_scc.append(curr_src)
        return transpose_src_scc

    def dfs_algo(self, src: int) -> list:

        src_scc = []
        list_of_src = [src]
        visited = [False] * (len(self.get_graph().get_all_v().values()))
        visited[src] = True
        while list_of_src:
            curr_src = list_of_src.pop(0)
            if self.Graph.all_out_edges_of_node(curr_src) is not None:
                for i in self.Graph.all_out_edges_of_node(curr_src).keys():
                    if visited[i] is False:
                        visited[i] = True
                        list_of_src.append(i)
            src_scc.append(curr_src)
        return src_scc


    def plot_graph(self) -> None:
        x_values = []
        y_values = []
        h_w = 0.0008
        w_arrow = 0.000005
        if self.Graph.v_size() > 10:
            h_w = 0.0003
            w_arrow = 0.000007
        for i in self.Graph.get_all_v().values():
            if i.getPos() is None:
                random_x = random.uniform(0.5, self.Graph.v_size())
                random_y = random.uniform(0.5, self.Graph.v_size())
                i.setPos((random_x, random_y, 0.0))

                x_values.append(i.getPos()[0])
                y_values.append(i.getPos()[1])
            else:
                x_values.append(i.getPos()[0])
                y_values.append(i.getPos()[1])
        l = []
        for i in self.Graph.get_all_v():
            l.append(i)
        fig, ax = plt.subplots()
        ax.scatter(x_values, y_values)
        for i, txt in enumerate(l):
            ax.annotate(l[i], (x_values[i], y_values[i]))
        for n in self.Graph.get_all_v().keys():
            for j in self.Graph.all_out_edges_of_node(n):
                x1 = self.Graph.get_all_v().get(n).getPos()[0]
                y1 = self.Graph.get_all_v().get(n).getPos()[1]
                x2 = self.Graph.get_all_v().get(j).getPos()[0]
                y2 = self.Graph.get_all_v().get(j).getPos()[1]
                plt.arrow(x1, y1, (x2 - x1),
                          (y2 - y1), length_includes_head=True, width=w_arrow,
                          head_width=h_w, ec='k')
        plt.plot(x_values, y_values, "ro")
        plt.ylabel("y")
        plt.title("Ex3-OOP")
        plt.xlabel("x")
        plt.show()
