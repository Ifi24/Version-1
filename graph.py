from node import *
from segment import *
import matplotlib.pyplot as plt


class Graph:
    def __init__(self): # inicia la clase Graph
        self.nodes = []
        self.segments = []


    def AddNode(self, node): # añade un node, versión más rudimetaria que la que hay en interface.py
        if node in self.nodes:
            return False
        self.nodes.append(node)
        return True


    def AddSegment(self, name, nameoriginNode, namedestinationNode):  # No se pasa 'self' explícitamente, versión más básica
        origin = next((n for n in self.nodes if n.name == nameoriginNode), None)
        destination = next((n for n in self.nodes if n.name == namedestinationNode), None)

        if not origin or not destination:
            return False

        # Aquí se pasa correctamente el objeto origin y destination a Segment
        segment = Segment(name, origin, destination)
        self.segments.append(segment)
        origin.AddNeighbor(destination)
        return True


    def GetClosest(self, x, y): # encuentra los nodos más cercanos
            closest_node = None
            min_distance = float('inf')

            for node in self.nodes:
                d = ((node.x - x) ** 2 + (node.y - y) ** 2) ** 0.5
                if d < min_distance:
                    min_distance = d
                    closest_node = node

            return closest_node


    def Plot(self): # hace el plot del gráfico
        plt.figure(figsize=(8, 6))
        for segment in self.segments:
            x_values = [segment.origin.x, segment.destination.x]
            y_values = [segment.origin.y, segment.destination.y]
            plt.annotate('', xy=(segment.destination.x, segment.destination.y),
                         xytext=(segment.origin.x, segment.origin.y),
                         arrowprops=dict(arrowstyle='->', color='blue', lw=2))            
            plt.plot(x_values, y_values, 'k-', linewidth=1)
            mid_x = (segment.origin.x + segment.destination.x) / 2
            mid_y = (segment.origin.y + segment.destination.y) / 2
            plt.text(mid_x, mid_y, f"{segment.cost:.1f}", fontsize=10, color='red')

        for node in self.nodes:
            plt.scatter(node.x, node.y, color='red', s=100)
            plt.text(node.x, node.y, node.name, fontsize=12)

        plt.title("Gráfico con nodos y segmentos")
        plt.grid(True)
        plt.show()
        return plt.subplots()


    def PlotNode(self, nameorigin): # hace el plot de los nodos
        origin = next((n for n in self.nodes if n.name == nameorigin), None)
        if not origin:
            return False

        plt.figure(figsize=(8, 6))
        for segment in self.segments:
            if segment.origin == origin or segment.destination == origin:
                x_values = [segment.origin.x, segment.destination.x]
                y_values = [segment.origin.y, segment.destination.y]

                # Dibuja flechas rojas entre los nodos
                plt.annotate('', xy=(segment.destination.x, segment.destination.y),
                             xytext=(segment.origin.x, segment.origin.y),
                             arrowprops=dict(arrowstyle='->', color='blue', lw=2))


                mid_x = (segment.origin.x + segment.destination.x) / 2
                mid_y = (segment.origin.y + segment.destination.y) / 2
                plt.text(mid_x, mid_y, f"{segment.cost:.1f}", fontsize=10, color='black')

        # Dibuja los nodos
        for node in self.nodes:
            color = 'gray'
            if node == origin:
                color = 'blue'
            elif node in origin.neighbors:
                color = 'green'
            plt.scatter(node.x, node.y, color=color, s=100)
            plt.text(node.x, node.y, node.name, fontsize=12)

        plt.title('Gráfico de nodos y segmentos')
        plt.grid(True, color='red')
        plt.show()
        return True

    def LoadGraphFromFile(graph_data): 
        G = Graph()

        with open('graph_data.txt', 'r') as file:
            lines = file.readlines()

        # Read nodes
        for line in lines:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split(',')
            if len(parts) == 3:
                name, x, y = parts
                x, y = float(x), float(y)
                G.AddNode(Node(name.strip(), x, y))

        # Read segments
        for line in lines:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.split(',')
            if len(parts) == 3:
                name, origin, destination = parts
                G.AddSegment(name.strip(), origin.strip(), destination.strip())


        return G
   
    def LoadFromFile(self, filename):
        with open(filename, 'r') as f:
            section = None
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if line.startswith('#nodes'):
                    section = 'nodes'
                    continue
                elif line.startswith('#segments'):
                    section = 'segments'
                    continue


                if section == 'nodes':
                    parts = line.split(',')
                    if len(parts) == 3:
                        name, x, y = parts
                        self.AddNode(Node(name, float(x), float(y)))


                elif section == 'segments':
                    parts = line.split(',')
                    seg_name, origin, destination = parts[:3]
                    self.AddSegment(seg_name, origin, destination)


        return True
    
    def GetNodeByName(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        return None
    
def LoadGraphFromFile(filename):
    G = Graph()
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    LeeNodo = True  # Flag to differentiate nodes from segments
    for line in lines:
        line = line.strip()
        if line[0] == "#" or not line:
            continue     #Si la línea empieza con un # o está vacía, el programa salta esa línea y no ejecuta el resto del código en esa iteración del bucle
        if "Segments" in line:
            LeeNodo = False
            continue
    
        parts = line.split(',')
        if LeeNodo and len(parts) == 3:
            name, x, y = parts
            G.AddNode(Node(name.strip(), float(x), float(y)))
        elif not LeeNodo and len(parts) == 3:
            name, origin, destination = parts
            G.AddSegment(name.strip(), origin.strip(), destination.strip())


    return G
    

    