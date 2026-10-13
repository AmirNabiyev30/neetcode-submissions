class Node:
        def __init__(self,key = None,val=None):
            self.prev,self.nxt  = None, None
            self.key = key
            self.val = val


class LRUCache:
    #so in order to have that reordering we need something that we consintely change
    #in a linked list with nodes can also to do this

    #we will have a most recent and least recently used nodes that will act as dummy
    #nodes that will allow us to access the values we need

    def __init__(self, capacity: int):
        #we want the dictionary to be able to have O(1) retrieval
        self.cache = {}
        self.size = capacity
        #institate our dummy nodes least recently used and most receent
        self.lru, self.recent = Node(0,0),Node(0,0)
        #connect them to each other for now
        self.recent.prev = self.lru
        self.lru.nxt = self.recent 
    def insert(self,node):
        #we insert from the right
        #Example  1 <=> 2 <=> 3
        #get previous node and nxt node
        prev,nxt = self.recent.prev,self.recent
        #assign new node connections
        node.prev = prev
        node.nxt = nxt

        prev.nxt = nxt.prev = node
          
    def remove(self,node):
        #we take this nodes connection and make them skip over
        prev = node.prev
        nxt = node.nxt
        prev.nxt,nxt.prev = nxt,prev

    def get(self, key: int) -> int:
        #this assume we have nodes in between LRU and recent
        if key in self.cache:
            #we want to remove our node and then insert from the right
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        #key not found
        return -1

    def put(self, key: int, value: int) -> None:
        #now putting the node will almost be simple
        #we want to insert from the right
        #first we check if the node is already there
        if key in self.cache:
            self.remove(self.cache[key]) 
        node = Node(key,value)  
        self.insert(node)
        self.cache[key] = node
        #now we check the size of the cache

        if len(self.cache) > self.size:
            #remove the LRU
            del self.cache[self.lru.nxt.key] #this is why store key-value pairs
            self.remove(self.lru.nxt)


        
