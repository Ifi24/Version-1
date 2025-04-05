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
import math
class Node:
    def __init__(self, name, x ,y):
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.neighbors = []
    def AddNeighbor (self, n2):
        if n2 in self.neighbors:
           return False
        self.neighbors.append(n2)
        return True
def Distance(n1, n2):
    return math.sqrt((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2)
