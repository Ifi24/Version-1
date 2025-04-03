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
        return True

def AddSegment(g, nameOriginNode, nameDestinationNode):
    g.segments.append(Segment(nameOriginNode, nameDestinationNode))
    nameOriginNode