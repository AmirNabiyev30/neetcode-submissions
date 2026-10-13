class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Brute Force Approach:
        For every letter we run a sliding window algorithm,
        where if that letter is part of t set then we run an algroithm
        that will find the substring, store the length and the string
        and we do this for the entire string, this could be o (n^2) op
        """
        #sets up a freqeuncy dict for O(1) checks
        t_dict = {}
        for let in t:
            if let in t_dict:
                t_dict[let]+=1
            else:
                t_dict[let] = 1

        self.res = [-1,""]

        def fin(curr):
            for val in curr.values():
                if val > 0:
                    return False
            return True
        def slide(i,curr):# take a position, and a set of characters to look for
            f,l = i,i
            while l < len(s): #reach end or set equality
                if fin(curr):
                    break
                if s[l] in curr and curr[s[l]] > 0:
                    curr[s[l]] -= 1 # reduce frequency if we find that thing
                l+=1
            if fin(curr):
                print("Found!: ", s[f:l])
                #if never intialized before
                if self.res[0] == -1:
                    self.res[0] = l-f
                    self.res[1] = s[f:l]
                    print("String:",s[f:l])
                else:
                    if l-f < self.res[0]:
                        self.res[0] = l-f
                        self.res[1] = s[f:l]
        #iterate over entire thing
        for i in range(len(s)):
            if s[i] in t_dict:
                curr = t_dict.copy()
                print("Looking for",curr)
                slide(i,curr)
        
        print(self.res)
        return self.res[1]
        