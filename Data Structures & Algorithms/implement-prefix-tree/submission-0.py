class PrefixTree:
    #tries are just finite state machine, they have transitions
    #we can have infinite amount of children, all that needs to happen is that they share the same parent
    class treeNode:
        def __init__(self,val = None):
            self.val = val
            self.children = {}
            self.end = False
    def __init__(self):
        self.root = self.treeNode("")
        

    def insert(self, word: str) -> None:
        #have a pointer to iterate
        curr = self.root
        for let in word:
            if let not in curr.children:
                curr.children[let] = self.treeNode(let)
            curr = curr.children[let]
        #end of word marker
        curr.end = True
        #there is no more children and once we hit none
    def search(self, word: str) -> bool:
        #building answering, which will be a dfs search over a tree
        def dfs(node, i):
            if i == len(word):
                if node.end:
                    return True
                else:
                    return False
            if word[i] in node.children:
                    return dfs(node.children[word[i]],i+1)
            return False
              
        return dfs(self.root,0)
        
    def startsWith(self, prefix: str) -> bool:
        #we want to see if we can construct a word using this prefix
        def dfs(node,i):
            if i == len(prefix):
                return True
            if prefix[i] in node.children:
                return dfs(node.children[prefix[i]],i+1)
            return False
        return dfs(self.root,0)
        