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
        #iterate over entire thing
        st,e = 0 ,0
        while e < len(s):
            if s[e] in t_dict:
                t_dict[s[e]] -=1
            e+=1 
            if fin(t_dict):
                #now we have finsihed dict
                #have another while loop that trys to shrink the window as much as possible
                print(e)
                while fin(t_dict):
                    #record size
                    if self.res[0] == -1:
                            self.res[0] = e-st
                            self.res[1] = s[st:e]
                    else:
                        if e-st < self.res[0]:
                            self.res[0] = e - st
                            self.res[1] = s[st:e]
                    if s[st] in t_dict:
                        t_dict[s[st]]+=1
                    st+=1
                print(s[st:e])                
        return self.res[1]
        