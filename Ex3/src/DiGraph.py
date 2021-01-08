from Ex3.src.GraphInterface import GraphInterface


class NodeData:
    def __init__(self, key: int, pos: tuple = None, weight: float = 0, tag: int = 0, info: str = ""):
        self.key = key
        self.pos = pos
        self.weight = weight
        self.tag = tag
        self.info = info
        self.IN = {}
        self.out = {}

    def HasNi(self, dest: int) -> bool:
        for i in self.dest.keys():
            if i == dest:
                return True
        return False

    def AddGetIn(self, dest: int, w: float):
        self.IN[dest] = w

    def AddGetOut(self, src: int, w: float):
        self.out[src] = w

    def getIn(self) -> int:
        return self.IN

    def getOut(self) -> int:
        return self.out

    def getKey(self) -> int:
        return self.key

    def setKey(self, k: int):
        self.key = k

    def getWeight(self) -> float:
        return self.weight

    def setWeight(self, w: float):
        self.weight = w

    def getTag(self) -> int:
        return self.tag

    def setTag(self, t: int):
        self.tag = t

    def getInfo(self) -> str:
        return self.info

    def setInfo(self, i: str):
        self.info = i

    def __cmp__(self, other):
        return other.tag < self.tag


class DiGraph(GraphInterface):

    def __init__(self):
        self.Nodes = {}
        self.Es = 0
        self.Mc = 0

    def getNode(self, key: int) -> NodeData:
        return self.Nodes.get(key)

    def v_size(self) -> int:
        return len(self.Nodes)

    def e_size(self) -> int:
        return self.Es

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.getNode(id1).getIn()

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.getNode(id1).getOut()

    def get_mc(self) -> int:
        return self.Mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if id1 == id2:
            return False

        if not self.Nodes.__contains__(id1) or not self.Nodes.__contains__(id2):
            return False

        self.getNode(id2).AddGetIn(id1, weight)
        self.getNode(id1).AddGetOut(id2, weight)

        self.Es += 1
        self.Mc += 1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if self.Nodes.__contains__(node_id):
            return False
        self.Nodes[node_id] = NodeData(node_id, pos)
        self.Mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if self.Nodes.__contains__(node_id):
            node = self.getNode(node_id)
            for curr in node.IN:
                self.getNode(curr).out.pop(node_id)
                self.Es -= 1
            for curr in node.out:
                self.getNode(curr).IN.pop(node_id)
                self.Es -= 1
            self.Nodes.pop(node_id)
            self.Mc += 1
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 == node_id2:
            return False
        if self.Nodes.__contains__(node_id1) and self.Nodes.__contains__(node_id2):
            self.getNode(node_id1).out.pop(node_id2)
            self.Es -= 1
            self.Mc += 1
            return True
        return False


