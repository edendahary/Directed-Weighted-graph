import time
from src.GraphAlgo import GraphAlgo


def check0():
    ga = GraphAlgo()
    file = '../data/A5'
    ga.load_from_json(file)
    start1 = time.time()
    dist, path = ga.shortest_path(0, 5)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(ga.connected_component(7))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(ga.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check1():
    ga = GraphAlgo()
    file = '../data/G_10_80_1.json'
    ga.load_from_json(file)
    start1 = time.time()
    dist, path = ga.shortest_path(0, 5)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(ga.connected_component(7))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(ga.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check2():
    ga = GraphAlgo()
    file = '../data/G_100_800_1.json'
    ga.load_from_json(file)
    start1 = time.time()
    dist, path = ga.shortest_path(0, 45)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(ga.connected_component(34))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(ga.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check3():
    ga = GraphAlgo()
    file = '../data/G_1000_8000_1.json'
    ga.load_from_json(file)
    start1 = time.time()
    dist, path = ga.shortest_path(3, 450)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(ga.connected_component(900))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(ga.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check4():
    ga = GraphAlgo()
    file = '../data/G_10000_80000_1.json'
    ga.load_from_json(file)
    start1 = time.time()
    dist, path = ga.shortest_path(3324, 3333)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(ga.connected_component(5000))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(ga.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check5():
    ga = GraphAlgo()
    file = '../data/G_20000_160000_1.json'
    ga.load_from_json(file)
    start1 = time.time()
    dist, path = ga.shortest_path(25, 300)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(ga.connected_component(900))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(ga.connected_components())
    end3 = time.time()
    print(end3 - start3)


def check6():
    ga = GraphAlgo()
    file = '../data/G_30000_240000_1.json'
    ga.load_from_json(file)
    start1 = time.time()
    dist, path = ga.shortest_path(9, 25000)
    print(dist, path)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    print(ga.connected_component(20000))
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    print(ga.connected_components())
    end3 = time.time()
    print(end3 - start3)


if __name__ == '__main__':
    check0()
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()
