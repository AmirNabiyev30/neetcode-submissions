class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_pali(s):
            return s == s[::-1]
        """
        we need to build up our answer. The key question how does adding
        another letter to our previous solution change our current solution
        one obvious observation is that when we add a letter, we have that
        letter that can be an palindrome and the new string that can be
        created
        are there cases where this doesnt become true

        it could be better to process via indices

        """
        res = 0
        curr = ""
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r<len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            l = i
            r= i+1
            while l >= 0 and r<len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
        return res




        
        