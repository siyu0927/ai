## 根據陳鍾誠老師未完成的code寫的,有借助chatgpt的幫助

from random import random, randint, choice
import numpy as np

citys = [
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(plen):
        dist += distance(citys[p[i]], citys[p[(i+1)%plen]])
    return dist

def neighbor(p):  ##隨機選兩個城市交換
    new_p = p.copy()
    i, j = randint(0, len(p)-1), randint(0, len(p)-1)
    new_p[i], new_p[j] = new_p[j], new_p[i]
    return new_p

def hillClimbing(p, pathLength, neighbor, max_iter):
    print("Initial Path Length:", pathLength(p))
    for i in range(max_iter):
        new_p = neighbor(p)
        if pathLength(new_p) < pathLength(p):
            p = new_p
    return p

initial_path = [i for i in range(len(citys))]  
print("Initial Path:", initial_path) 
optimal_path = hillClimbing(initial_path, pathLength, neighbor, max_iter=1000)
print("Optimal Path:", optimal_path)
print("Optimal Path Length:", pathLength(optimal_path))
