from src.Domain.domain import Vertex


class Repository:

    def __init__(self):
        self.__fileName = "vertices.txt"
        self.__data = list()
        self.__loadFile()

    def __iter__(self):
        self.__n = 0
        return self

    def __next__(self):
        self.__n += 1
        if self.__n > len(self.__data):
            raise StopIteration("No more vertices!")
        return self.__data[self.__n - 1]

    def __prev__(self):
        self.__n -= 1
        if self.__n < 0:
            raise StopIteration("No more vertices!")
        return self.__data[self.__n]

    def __resetIter__(self):
        self.__n = 0

    def __getData__(self):
        return self.__data

    def __len__(self):
        return len(self.__data)

    def __loadFile(self):
        file = open(self.__fileName, "rt")

        for line in file.readlines():
            _line = line.split(sep=' ')

            if len(_line) == 2:
                edges_no = int(_line[0])
                for i in range(edges_no):
                    self.__data.append(Vertex(i))

            elif len(_line) == 3:
                _line[2].strip('\n')
                id_vout = int(_line[0])
                idTarget = int(_line[1])
                cost = int(_line[2])

                self.__data[id_vout].__addTarget__(idTarget, cost)

                self.__data[idTarget].__addVertexIN__(id_vout, cost)

            else:
                continue
