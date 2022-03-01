from src.Repo.repo import TxtRepo


class UI:

    def __init__(self, repo: TxtRepo):
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
              "\t6. Exit.\n")

    @staticmethod
    def wrong_input():
        print("Wrong input, please try again!\n")

    @staticmethod
    def user():
        return input("Your command (it's number): ")

    def printNumberOfVertices(self):
        print(self.__repo.__len__())

    def printVertices(self):
        data = self.__repo.data()
        for vertex in data:
            print("Vertex " + str(vertex.id))
            print("Targets:", vertex.targets)
            print("Costs: ", vertex.costs)
            print()

    def iterateVertices(self):
        vertex = self.__iter_repo.__next__()
        print("Vertex " + str(vertex.id))
        print("Targets:", vertex.targets)
        print("Costs: ", vertex.costs)
        print()

    def iterateVerticesBackwards(self):
        vertex = self.__iter_repo.__prev__()
        if vertex is not False:
            print("Vertex " + str(vertex.id))
            print("Targets:", vertex.targets)
            print("Costs: ", vertex.costs)
            print()
        else:
            print("Can't iterate backwards anymore!\n")
