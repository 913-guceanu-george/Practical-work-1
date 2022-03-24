import unittest
from Graph.graph import *


class Tests(unittest.TestCase):
    def test_add_rem_vertex(self):
        g = Graph()
        self.assertEqual(g.countVertices(), 0)
        g.addVertex(2)
        g.addVertex(4)
        self.assertEqual(g.countVertices(), 2)
        g.removeVertex(4)
        self.assertEqual(g.countVertices(), 1)
        with self.assertRaises(VertexError):
            g.addVertex(2)
        with self.assertRaises(VertexError):
            g.removeVertex(100)

    def test_add_rem_edge(self):
        g = Graph(10)
        g.addEdge(1, 2, 1)
        g.addEdge(1, 3, 2)
        g.addEdge(4, 2, 10)
        g.addEdge(2, 4, 9)
        self.assertEqual(g.countEdges(), 4)
        g.removeEdge(1, 2)
        self.assertEqual(g.countEdges(), 3)
        with self.assertRaises(EdgeError):
            g.addEdge(1, 3)
        with self.assertRaises(EdgeError):
            g.addEdge(11, 12)
        self.assertEqual(set(g.edgesIterator()), {
                         (1, 3, 2), (4, 2, 10), (2, 4, 9)})

    def test_parse_set_of_vertices(self):
        g = Graph()
        g.addVertex(4)
        g.addVertex(1)
        g.addVertex(9)
        v = set(g.verticesIterator())
        self.assertEqual(v, {1, 4, 9})
        g.addVertex(10)
        v = set(g.verticesIterator())
        self.assertEqual(v, {1, 4, 9, 10})

    def test_is_edge(self):
        g = Graph(4)
        g.addEdge(1, 2)
        g.addEdge(2, 3)
        self.assertTrue(g.isEdge(1, 2))
        self.assertFalse(g.isEdge(2, 1))

    def test_indegree_outdegree(self):
        g = Graph(6)
        g.addEdge(1, 2)
        g.addEdge(1, 3)
        g.addEdge(1, 5)
        g.addEdge(2, 1)
        g.addEdge(4, 1)
        self.assertEqual(g.inDegree(1), 2)
        self.assertEqual(g.outDegree(1), 3)
        self.assertEqual(g.inDegree(4), 0)
        self.assertEqual(g.outDegree(4), 1)

    def test_parse_outbound_edge(self):
        g = Graph(5)
        g.addEdge(1, 2)
        g.addEdge(1, 3)
        g.addEdge(1, 4)
        g.addEdge(0, 1)
        self.assertEqual(set(g.neighboursIterator(1)), {2, 3, 4})

    def test_parse_inbound_edge(self):
        g = Graph(5)
        g.addEdge(1, 2)
        g.addEdge(1, 3)
        g.addEdge(1, 4)
        g.addEdge(0, 1)
        self.assertEqual(set(g.transposeIterator(1)), {0})

    def test_get_set_edge_cost(self):
        g = Graph(4)
        g.addEdge(1, 2, 5)
        g.addEdge(1, 0, 3)
        self.assertEqual(g.getEdgeCost(1, 2), 5)
        g.setEdgeCost(1, 2, 10)
        self.assertEqual(g.getEdgeCost(1, 2), 10)

    def test_copy_graph(self):
        g = Graph(4, 7)
        a = g.copy()
        a.removeVertex(1)
        self.assertEqual(set(g.verticesIterator()), {0, 1, 2, 3})
