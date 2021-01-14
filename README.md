# Ex3-OOP
# Directed Weighted graph 

### This is an object oriented programmin project which his main idea is based on functions.

### This Project Made by Eden Dahary Student in Ariel University.

### This project contains a directional weighted graph with vertexs and edges.

### in this project we implements data structure, algorithms and GUI.

## NodeData Class

This Class represents a node with unique key and a string ,tag and pos location that is a 3D point and two dict that one is all the edges that get out of the current node and the other one contains all the edges that get in this node.

### This Class contains serval methods:

| **Methods**      |    **Details**        |
|-----------------|-----------------------|
| `__init__(self, key: int, pos: tuple = None, weight: float = 0, tag: int = 0, info: str = "", **kwargs):` | create a new node with the given id |
| getKey(self) -> int:` | Returns the node key |
| `getInfo(self) -> str:` | Returns the node String |
| `setInfo(self, i: str):` | Sets the node String  |
| `getTag(self) -> int:` | Returns the node tag |
| `setTag(self, t: int):` | Sets the node tag |
| `getPos(self) -> float:` | Returns the node pos |
| `setPos(self, p: float):` | Sets the node pos |


## DiGraph(GraphInterface):

This Class represents the set of operations applicable on a node (vertex) in a directional weighted graph.

### This Class contains serval methods:

| **Methods**      |    **Details**        |
|-----------------|-----------------------|
| `__init__(self):` | Default constructor     |
| `getNode(self, key: int) -> NodeData:` | Returns a node by the nodeKey |
| `v_size(self) -> int:` | Returns the amount of the nodes in the graph|
| `e_size(self) -> int:` | Returns the amount of edges in the graph |
| `get_all_v(self) -> dict:` | Returns a dict that contains all the nodes in the graph |
| `all_in_edges_of_node(self, id1: int) -> dict:` | Returns a dict that contains all that edges that get in the current node|
| `all_out_edges_of_node(self, id1: int) -> dict:` | Returns a dict that contains all that edges that get out from current node|
| `add_edge(self, id1: int, id2: int, weight: float) -> bool:` | Returns ture if edge was added false other wise | 
| `add_node(self, node_id: int, pos: tuple = None) -> bool:` | Returns ture if node was added false other wise | 
| `remove_node(self, node_id: int) -> bool:` | Returns ture if the node was removed false other wise  |
| `remove_edge(self, node_id1: int, node_id2: int) -> bool:` | Returns ture if edge the was removed false other wise | 
| `get_mc(self) -> int:)` | Returns the mode count|

## GraphAlgo(GraphAlgoInterface):

This class represents a Directed (positive) Weighted Graph Theory Algorithms including:
 shortest_path(self, id1: int, id2: int) -> (float, list):
 save_to_json(self, file_name: str) -> bool: // JSON file
 load_from_json(self, file_name: str) -> bool: // JSON file
 connected_component(self, id1: int) -> list: // Returns the Strongly Connected Component(SCC) that node id1 is a part of.
 connected_components(self) -> List[list]: // Returns all the Strongly Connected Component(SCC) in the graph.
 plot_graph(self) -> None: // draw the graph

implement this Grpah Algorithms with a private class that called DijkstraResult that compute the functions in this class.

| **Method**      |    **Details** |
|-----------------|--------------|
| `__init__(self, g: GraphInterface = None):` | Initialize the graph |
| `get_graph(self) -> GraphInterface:` | Returns a pointer to the initialized graph |
| `load_from_json(self, file_name: str) -> bool:` | Returns true if the graph was loaded false otherwise |
| `save_to_json(self, file_name: str) -> bool:` | Returns true if the graph was saved in the file false otherwise |
| `shortest_path(self, id1: int, id2: int) -> (float, list):` | Return the the shortest path between id1 to id2 |
| `connected_components(self) -> List[list]:` | Returns all the Strongly Connected Component(SCC) in the graph |
| `connected_component(self, id1: int) -> list:` | Returns the Strongly Connected Component(SCC) that node id1 is a part of. |



