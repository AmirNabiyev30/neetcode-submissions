"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        """
        keep a set and check membership
        and iterate through graph using bfs
        """
        if not node:
            return None
        res = None
        q = deque()
        q.append(node)
        cloned = {}
        cloned[node] = Node(val=node.val, neighbors=[])
        while q:
            curr = q.popleft()
            # set add to visited set
            #create node
            #now we want to iterate through neigbors
            for adj in curr.neighbors:
                #only add non visited nodes to the queue 
                if adj not in cloned:
                    cloned[adj] = Node(adj.val)
                    q.append(adj)
                #add the neighbor
                cloned[curr].neighbors.append(cloned[adj])

        return cloned[node]
        



        