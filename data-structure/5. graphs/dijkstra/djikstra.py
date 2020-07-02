import sys

# Grafo por Lista de adjacencia PONDERADO SEM DIREÇÃO
class Graph():

    def __init__(self, qtd_vertex):
        self.V = qtd_vertex
        self.graph = {}

    # Sem direação
    def addEdge(self, src, dest, v):
        if(src not in self.graph.keys()):
            self.graph[src] = {}
        self.graph[src][dest] = v
        if(dest not in self.graph.keys()):
            self.graph[dest] = {}
        self.graph[dest][src] = v

    def minimunDistance(self, dist, sptSet):
        minimun = 999 #sys.maxsize

        # print("\tdist:", dist)
        self.print_dist(dist)
        for v in self.graph.keys():
            # print("=> v[" + str(v) + "]")
            # print("dist[v]:", dist[v], "minimun", minimun)
            if( dist[v] < minimun and sptSet[v] == False):
                # print("entrou")
                minimun = dist[v]
                min_index = v
        # print("min_index_output", min_index)
        return min_index

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def dijkstra(self, origin):
        V = self.V

        dist = {i:999 for i in range(self.V)}
        dist[origin] = 0
        sptSet = { j:False for j in range(self.V)}

        # print("sptSet", sptSet)

        for _ in self.graph.keys():

            u = self.minimunDistance(dist, sptSet)
            sptSet[u] = True
            print("u", u)

            for v in self.graph[u]:
                print("=>    u", u, "v", v)

                if( self.graph[u][v] > 0 and
                    sptSet[v] == False and
                    dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)

    def print_dist(self, dist):
        for i in dist.keys():
            print("\t" + str(i), end="")
        print()
        for j in dist.values():
            print("\t" + str(j), end="")
        print()

# print(sys.maxsize)
graph = Graph(9)

graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)

graph.dijkstra(0)
