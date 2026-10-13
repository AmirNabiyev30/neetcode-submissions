class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        can we spilt s into a way where it only consists of dictionary words
        always assume false and if we can find a situation then return true
        I think we can treat as a graph problem.

        I think a brute force solution, would be that for every letter, we recurse over the rest, and if its true that we can have the first spilt in word dict then we perform the same operation for the rest of the dict

        its basically a dfs

        iterate over every letter, we check if the first section is in dict, if it is then we recurse.
        this can become an o(2^n) algorithm because we look at power set of the string

        now we need to be able to save computation, use extra memory to save on possible computations
        we can use a hash table to store possible subtrings so we dont have to recompute them. cause we are recomputing a lot. 

        we want these recursive sub calls to do less work

        can we do one forward pass to see if 

        yes we have a dictionary but we need to be able to store the ones that we know break down into true sitations to save on computation time. 
        """
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                #checking if the length of word exceeds string length and if
                #substirng is actually equal to string length
                if (i+len(w)<=len(s) and s[i:i+len(w)]==w):
                    #then we have good situation
                    dp[i] = dp[i+len(w)]
                #if we found our match then dont need to check other words
                if dp[i]:
                    break
        return dp[0]







