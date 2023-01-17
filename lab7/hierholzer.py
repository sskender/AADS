from collections import deque
from typing import List, Dict, Tuple
import copy

def AugmentedHierholzer(G: Dict[str, List[str]], start: str) -> Tuple[List[str], List[List[str]]]:
    """
    Args:
        G (dict): Adjacency matrix implemented as dictionary.
        start (str): Starting node for the algorithm.
    Returns:
        Tuple[List[str], List[List[str]]]: A tuple containing path in Euler graph.
    """
    stack = deque()
    stack.append(start)
    
    path: List[str] = []
    cycles: List[List[str]] = []
    
    while stack:
        u = stack[-1]
        adj = G[u]
        if len(adj) > 0:
            v = G[u][0]
            stack.append(v)
            G[u].remove(v)
            G[v].remove(u)
        else:
            path.append(u)
            stack.pop()

    return (path, cycles)



G = {'a': ['b', 'c', 'd', 'e'],
     'b': ['a', 'd', 'e'],
     'c': ['a', 'e'],
     'd': ['a', 'b', 'e'],
     'e': ['a', 'b', 'c', 'd']}
     
G1 = copy.deepcopy(G)

path, circles = AugmentedHierholzer(G1, 'b')
path.reverse()

assert path == ['b', 'a', 'c', 'e', 'a', 'd', 'b', 'e', 'd']
assert circles == [['d', 'e', 'b', 'd'], ['e', 'b', 'd', 'a', 'e'], ['a', 'e', 'c', 'a'], ['b', 'd', 'a', 'e', 'c', 'a', 'b']]

G1 = copy.deepcopy(G)

path, circles = AugmentedHierholzer(G1, 'd')
path.reverse()

assert path == ['d', 'a', 'b', 'd', 'e', 'a', 'c', 'e', 'b']
assert circles == [['e', 'c', 'a', 'e'], ['b', 'e', 'c', 'a', 'e', 'd', 'b'], ['a', 'e', 'd', 'b', 'a'], ['d', 'b', 'a', 'd']]
