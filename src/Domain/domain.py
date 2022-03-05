class Vertex:

    """
        This is the domain of our program, and like this, we can store vertices with their
    IN vertices and edges and their costs, along with their OUT vertices and edges and their costs.
    """

    def __init__(self, vertex_id: int):
        self.__id = vertex_id
        self.__verticesIN = list()
        self.__costsIN = list()
        self.__targets = list()
        self.__costsTARGETS = list()

    def __addTarget__(self, target: int, cost: int):
        self.__targets.append(target)
        self.__costsTARGETS.append(cost)

    def __addVertexIN__(self, vertexIN: int, cost: int):
        self.__verticesIN.append(vertexIN)
        self.__costsIN.append(cost)

    @property
    def id(self):
        return self.__id

    @property
    def verticesIN(self):
        return self.__verticesIN

    @property
    def costsIN(self):
        return self.__costsIN

    @property
    def targets(self):
        return self.__targets

    @property
    def costsTARGETS(self):
        return self.__costsTARGETS
