from src.Domain.domain import Vertex


class Repo:

    def __init__(self):
        self.__data = list()
        self.__max = 1000

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        self._n = 0
        return self

    def __next__(self):
        if self._n <= self.__max:
            self._n += 1
            return self.__data[self._n - 1]

    def __prev__(self):
        if self._n == 0:
            return False
        self._n -= 1
        return self.__data[self._n]

    def __getVertex__(self, vertex_id: int):
        return self.__data[vertex_id]

    def __addVertex__(self, vertex: Vertex):
        self.__data.append(vertex)

    def __addEdge__(self, vertex_in: Vertex, vertex_out: Vertex, cost: int):
        self.__data[vertex_out.id].targets.append(vertex_out.id)
        self.__data[vertex_out.id].costs.append(cost)

    def __loadData__(self, data: list):
        self.__data = data

    def data(self):
        return self.__data


class TxtRepo(Repo):

    def __init__(self):
        super().__init__()

        self.__filename = "vertices.txt"
        self.load_file()

    def load_file(self):
        # Skipping the first line of the file because it doesn't help us anymore.
        file = open(self.__filename, "r+")
        line = file.readline()

        # Actually getting the vertices from the .txt file.
        line = file.readline()
        line = line.split(sep=" ")

        _id = int(line[0])
        targets = [int(line[1])]

        line[2] = line[2].strip('\n')
        costs = [int(line[2])]

        data = list()

        for _line in file.readlines():

            # Checking if there aren't anymore vertices to load in the repo
            if(_line == '\n'):
                vertex = Vertex(_id, targets, costs)
                data.append(vertex)
            else:
                _line = _line.split(sep=' ')
                _line[2] = _line[2].strip('\n')

                # Building the lists of targets and costs
                if int(_line[0]) == _id:
                    targets.append(int(_line[1]))
                    costs.append(int(_line[2]))

                # Appending new vertices the newly formed vertices with their targets and costs
                else:
                    vertex = Vertex(_id, targets, costs)
                    data.append(vertex)

                    new_id = int(_line[0])

                    while(new_id <= _id):
                        data.append(Vertex(new_id, [], []))
                        new_id += 1
                    _id = int(_line[0])

                    targets = [int(_line[1])]

                    _line[2] = _line[2].strip('\n')
                    costs = [int(_line[2])]

        self.__loadData__(data)
        file.close()

    def save_file(self):

        file = open(self.__filename, "r+")
        data = self.data()
        for vertex in data:
            for i in range(len(vertex.targets)):
                file.write(str(vertex.id) + " " +
                           str(vertex.targets[i]) + " " + str(vertex.costs[i]) + '\n')

        file.close()
