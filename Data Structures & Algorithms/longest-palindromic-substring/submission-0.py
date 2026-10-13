class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pali = ("",-1)
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l>= max_pali[1]:
                    max_pali = (s[l:r+1],r-l)
                l-=1
                r+=1
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l>= max_pali[1]:
                    max_pali = (s[l:r+1],r-l)
                l-=1
                r+=1
        return max_pali[0]
            
            

        