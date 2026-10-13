class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        
        """
        preMap = {i:[] for i in range(numCourses)}

        #iterate through courses
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        #visit set
        visitSet = set()
        def dfs(crs):
            #2 cases
            if crs in visitSet:
                return False
            if preMap[crs] == []: # course has reqs
                return True
            #now we want to add this course to our visited set
            visitSet.add(crs)
            #we run it on all prereqs
            for pre in preMap[crs]:
                if not dfs(pre): return False
            #every course worked
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True 








        