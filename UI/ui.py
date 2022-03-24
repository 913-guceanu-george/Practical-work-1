from Graph.graph import *


class UI:
    def __init__(self, type_of_graph):
        self.type_of_graph = type_of_graph
        self.graph = None

    def empty_graph(self):
        self.graph = self.type_of_graph()
        print("Done!\n")

    def n_graph(self):
        n = input("Input the graph's no of vertices: ")
        try:
            self.graph = self.type_of_graph(int(n))
            print("Done!\n")
        except Exception as e:
            print(e)

    def m_graph(self):
        n = input("Input the graph's no. of vertices: ")
        m = input("Now the no. of edges: ")
        try:
            self.graph = self.type_of_graph(int(n), int(m))
            print("Done!\n")
        except Exception as e:
            print(e)

    def add_vertex(self):
        n = input("Vertex you want to add: ")
        try:
            self.graph.addVertex(int(n))
        except Exception as e:
            print(e)

    def add_edge(self):
        v1 = input("First vertex of the edge: ")
        v2 = input("Second vertex of the edge: ")
        c = input("Cost of the edge: ")
        try:
            self.graph.addEdge(int(v1), int(v2), int(c))
        except Exception as e:
            print(e)

    def rem_vertex(self):
        n = input("Type the vertex you wish to remove: ")
        try:
            self.graph.removeVertex(int(n))
        except Exception as e:
            print(e)

    def rem_edge(self):
        v1 = input("First vertex of the edge: ")
        v2 = input("Second vertex of the edge: ")
        try:
            self.graph.removeEdge(int(v1), int(v2))
        except Exception as e:
            print(e)

    def change_edge(self):
        v1 = input("First vertex of the edge: ")
        v2 = input("Second vertex of the edge: ")
        c = input("Cost of the edge: ")
        try:
            self.graph.setEdgeCost(int(v1), int(v2), int(c))
        except Exception as e:
            print(e)

    def print_edge(self):
        v1 = input("First vertex of the edge: ")
        v2 = input("Second vertex of the edge: ")
        try:
            print("The cost of the given edge is {0}.".format(
                self.graph.getEdgeCost(int(v1), int(v2))))
        except Exception as e:
            print(e)

    def inDegree(self):
        n = input("Vertex for which you want to find the in degree: ")
        try:
            print(self.graph.inDegree(int(n)))
        except Exception as e:
            print(e)

    def outDegree(self):
        n = input("Vertex for which you want to find the out degree: ")
        try:
            print(self.graph.outDegree(int(n)))
        except Exception as e:
            print(e)

    def cnt_vertices(self):
        print("Total of {0} vertices.".format(
            self.graph.countVertices()))
        print("\n")

    def cnt_edges(self):
        print("Total of {0} edges.".format(
            self.graph.countEdges()))
        print("\n")

    def isVertex(self):
        n = input("Type the vertex you wish to check: ")
        try:
            if self.graph.isVertex(int(n)):
                print("The given vertex is in the graph.\n")
            else:
                print("The given vertex is not in the graph.\n")
        except Exception as e:
            print(e)

    def isEdge(self):
        v1 = input("Type the first vertex of the edge: ")
        v2 = input("Type the second vertex of the edge: ")
        try:
            if self.graph.isEdge(int(v1), int(v2)):
                print("The edge does exist.\n")
            else:
                print("The edge doesn't exist.\n")
        except Exception as e:
            print(e)

    def print_vertex_list(self):
        for node in self.graph.verticesIterator():
            print(node, end=" ")
        print()

    def print_neighbour_list(self):
        n = input("Type the vertex you want to find neighbours for: ")
        try:
            anyone = False
            for node in self.graph.neighboursIterator(int(n)):
                print(node, end=" ")
                anyone = True
            if not anyone:
                print("Vertex {0} has no neighbours.".format(n))
                print("\n")
            else:
                print()
        except Exception as e:
            print(e)

    def print_transpose_list(self):
        n = input("Type the vertex you want to find inbound neighbours for: ")
        try:
            anyone = False
            for node in self.graph.transposeIterator(int(n)):
                print(node, end=" ")
                anyone = True
            if not anyone:
                print("Vertex {0} has no inbound neighbours.".format(n))
                print("\n")
            else:
                print()
        except Exception as e:
            print(e)

    def print_edges(self):
        anyone = False
        for triple in self.graph.edgesIterator():
            print("Vertices {0}, {1} and cost {2}.".format(
                triple[0], triple[1], triple[2]))
            anyone = True
        if not anyone:
            print("No edges in the graph.\n")

    def readFile(self):
        path = input("Type the file from which read: ")
        try:
            self.graph = readFile(path)
        except Exception as e:
            print(e)

    def writeFile(self):
        path = input("Type the file you write to: ")
        try:
            writeFile(path, self.graph)
        except Exception as e:
            print(e)

    def start(self):
        cmds = {"1": self.empty_graph,
                "2": self.n_graph,
                "3": self.m_graph,
                "4": self.add_vertex,
                "5": self.add_edge,
                "6": self.rem_vertex,
                "7": self.rem_edge,
                "8": self.change_edge,
                "9": self.print_edge,
                "10": self.inDegree,
                "11": self.outDegree,
                "12": self.cnt_vertices,
                "13": self.cnt_edges,
                "14": self.isVertex,
                "15": self.isEdge,
                "16": self.print_vertex_list,
                "17": self.print_neighbour_list,
                "18": self.print_transpose_list,
                "19": self.print_edges,
                "20": self.readFile,
                "21": self.writeFile}
        while True:
            print("1. Generate empty graph")
            print("2. Generate graph with n vertices")
            print("3. Generate graph with n vertices and m random edges")
            print("4. Add vertex")
            print("5. Add edge")
            print("6. Remove vertex")
            print("7. Remove edge")
            print("8. Change the cost of an edge")
            print("9. Print the cost of an edge")
            print("10. Print in degree of a vertex")
            print("11. Print out degree of a vertex")
            print("12. Print number of vertices")
            print("13. Print number of edges")
            print("14. Check if a vertex belongs to the graph")
            print("15. Check if an edge belongs to the graph")
            print("16. Print the list of vertices")
            print("17. Print the list of outbound neighbours of a vertex")
            print("18. Print the list of inbound neighbours of a vertex")
            print("19. Print the list of edges")
            print("20. Read the graph from a file")
            print("21. Write the graph to a file")
            print("0. Exit")
            cmd = input(">>> ")
            if cmd in cmds:
                cmds[cmd]()
            elif cmd == "0":
                break
            else:
                print("Invalid choice.")
