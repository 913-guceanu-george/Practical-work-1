class Vertex:

    def __init__(self, __id: int, targets: list, costs: list):
        self.__id = __id
        self.__targets = targets
        self.__costs = costs

    @property
    def id(self):
        return self.__id

    @property
    def targets(self):
        return self.__targets

    @property
    def costs(self):
        return self.__costs
