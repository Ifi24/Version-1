from node import *
from segment import *

class Graph:
    def __init__(self):
        self.nodes = []
        self.segments = []

def AddNode (g, n):
    if n in g.nodes:
        return False
    else:
        g.nodes.append(n)
        return True

def AddSegment(g, nameOriginNode, nameDestinationNode):
    origin = None
    destination = None
    for node in g.nodes:
        if node.name == nameOriginNode:
            origin = node
        if node.name == nameDestinationNode:
            destination = node
    if (origin is None) or (destination is None):
        return False
    
    g.segments.append(Segment(f"{nameOriginNode.name}{nameDestinationNode.name}", nameOriginNode, nameDestinationNode))
    nameOriginNode.neighbours.append(nameDestinationNode)
    AddNeighbour(nameOriginNode, nameDestinationNode)
    return True

#esta mal la manera en que he usado la distancia, esta tarde lo arreglo
def GetClosest(g, x, y):
    for n in g.nodes:
        given_distance = Distance(x, y)
        distances = []
        for x, y in n.x, n.y:
            distances.append(Distance(x, y))
        for d in distances:
            if d < given_distance