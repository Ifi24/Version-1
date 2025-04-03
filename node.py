def HaversineDistance(lat1, lon1, lat2, lon2):
    dLat = (lat2 - lat1) * (math.pi/180)
    dLon = (lon2 - lon1) * (math.pi/180)
    lat1 = lat1 * (math.pi/180)
    lat2 = lat2 * (math.pi/180)
    a = pow(math.sin(dLat/2), 2)
    b = pow(math.sin(dLon/2), 2)
    raiz = math.sqrt((a + (math.cos(lat1)) * (math.cos(lat2)) * b))
    c = 2 * math.asin(raiz)
    R = 6371000 #Earths's radius in meters
    return c * R

#paso 1
class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.neighbours = []

def AddNeighbour(n1, n2):
    if n2 in n1.neighbours:
        return False
    else:
        return True

import math
def Distance(n1, n2):
    a = ((n2.x) - (n1.x)) ** 2
    b = ((n2.y) - (n1.y)) ** 2
    d = math.sqrt(a + b)
    return d

#paso 2
