"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #so i was basically right but need to understand difference between n and n^2

        #bascially make a copy and have an external data strucuture that will keep track of the connections
        #if the node is null
        hmap = {None : None}

        curr = head

        #first pass is create all the nodes

        while curr:
            cpy = Node(curr.val)
            hmap[curr] = cpy
            curr = curr.next

        #second pass, assign all the connections

        curr = head

        while curr:
            #retrieve our copy
            cpy = hmap[curr]
            #assign connections
            cpy.next = hmap[curr.next]
            cpy.random = hmap[curr.random]

            #iterate curr

            curr = curr.next
        return hmap[head]
        





        