class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        We want to keep asking if the graph is connected and non-cyclical
        Given a list of edges,maybe we try removing an edge and see if it works or not
        and just keep going
        we know there are n nodes, we can remove,

        Brute Force:
        We remove and edge traverse the graph and then ask does it have any
        cycles and is it fully connected

        We have a traverse the graph for every single possible edge, so o(n^2)
        as we would traverse which is o(n) and then for every single edge which is also
        o(n)

        Can we do better

        what if we can build a graph as we traverse our input edges
        We ask, is this edge important, does it add connections to our graph, or does it create a cycle

        I can do the connected part, but the cycle part i dont know
        Psuedocade, we have a set, and everytime we process a connection we see if the nodes in the edge are already in the set, if they arent then that node is a necessary connection
        as it connects new nodes
        if it isn't that we know that node is not needed
        """
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n):
            p = par[n]
            while p!= par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return False #already connected
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] =p2
                rank[p2] +=rank[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        