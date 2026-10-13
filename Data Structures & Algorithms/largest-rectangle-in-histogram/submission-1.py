class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area  = 0
        stck = [] # store index and heights

        for i, h in enumerate(heights):
            start = i
            while stck and stck[-1][1] > h:
                #we pop that rectangle from the stack 
                index , height = stck[-1]
                #we check if that rectangle had a larger area 
                max_area = max(max_area,height * (i-index))
                #then we pop that rectangle
                stck.pop()
                #but we can extend the height back since the previous rectangle is taller so
                start = index
            #if it is a larger height
            stck.append((start,h))
        
        #now we compute the remaining parts of the stack
        for i , h in stck:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
