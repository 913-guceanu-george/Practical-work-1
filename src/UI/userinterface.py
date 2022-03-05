from src.Repo.repo import Repository


class UI:

    def __init__(self, repo: Repository):
        self.__repo = repo
        self.__iter_repo = self.__repo.__iter__()

    @staticmethod
    def welcome():
        print("Hello! Welcome to the graph manager G.")

    @staticmethod
    def menu():
        print("List of commands:\n" +
              "\t1. Prints this menu again.\n" +
              "\t2. Prints the number of vertices.\n" +
              "\t3. Print the vertices of the graph, with their targets and costs.\n" +
              "\t4. Iterate the vertices of the graph with their targets and the target's repsective costs.\n" +
              "\t5. Iterate backwards from the current point.\n" +
              "\t6. Reset the iterator.\n" +
              "\t0. Exit.\n")

    @staticmethod
    def wrong_input():
        print("Wrong input, please try again!\n")

    @staticmethod
    def user():
        return input("Your command (it's number): ")

    def numberofVertices(self):
        print(self.__repo.__len__())

    def printVertices(self):
        data = self.__repo.__getData__()
        for vertex in data:
            print("Vertex number: " + str(vertex.id) + '\n' +
                  "Targets: " + '\n' + str(vertex.targets) + '\n' +
                  "Targets costs: " + '\n' + str(vertex.costsTARGETS) + '\n' +
                  "Vertices IN: " + '\n' + str(vertex.verticesIN) + '\n' +
                  "Vertices IN costs: " + '\n' + str(vertex.costsIN) + '\n\n')

    def iterForward(self):
        try:
            vertex = self.__iter_repo.__next__()
            print("Vertex number: " + str(vertex.id) + '\n' +
                  "Targets: " + '\n' + str(vertex.targets) + '\n' +
                  "Targets costs: " + '\n' + str(vertex.costsTARGETS) + '\n' +
                  "Vertices IN: " + '\n' + str(vertex.verticesIN) + '\n' +
                  "Vertices IN costs: " + '\n' + str(vertex.costsIN) + '\n\n')
        except StopIteration as si:
            print(si)

    def iterBackwards(self):
        try:
            vertex = self.__iter_repo.__prev__()
            print("Vertex number: " + str(vertex.id) + '\n' +
                  "Targets: " + '\n' + str(vertex.targets) + '\n' +
                  "Targets costs: " + '\n' + str(vertex.costsTARGETS) + '\n' +
                  "Vertices IN: " + '\n' + str(vertex.verticesIN) + '\n' +
                  "Vertices IN costs: " + '\n' + str(vertex.costsIN) + '\n')
        except StopIteration as si:
            print(si)

    def resetIter(self):
        self.__iter_repo.__resetIter__()
        print("Now iteration will begin from vertex 0 again.\n")
