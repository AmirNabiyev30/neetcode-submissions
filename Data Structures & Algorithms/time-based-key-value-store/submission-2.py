class TimeMap:
    #so im thinking we use a stack, but that doesnt work, so we are
    #going to do a binary search algo to find the most recent timestamp
    
    def __init__(self):
        #we need a dict
        self.dict = {} # keys will be string and values will be tuples
        self.best = None

    def set(self, key: str, value: str, timestamp: int) -> None:
        #adding it to our dictionary
        #if we've never seen the key before we intilize the list
        if key not in self.dict.keys():
            self.dict[key] = [(value,timestamp)]
        #or we just append to the list
        else:
            self.dict[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        #now we need to perform a binary search amongst all tuples
        #to find our most recent timestamp
        if key not in self.dict.keys():
            return ""
        
        vals = self.dict[key] #vals is a list of tuples
        
        #2 cases:
        #we find the exact timestamp as the requested timestamp
        #we find the most recent timestamp from request timestamp
        print(vals)
        if not vals:
            return ""
        l,r  = 0,len(vals)-1
        #since timestamps are in the most recent order
        #the far right timestamp will be the most recent
        if vals[r][1] < timestamp:
            return vals[r][0]
        if vals[l][1] > timestamp:
            return ""
        #if not then our required timestamp is somewhere in vals

        while l <= r:
            #we want to keep track of our last best value
            mid = (l+r)//2


            if vals[mid][1] == timestamp:
                return vals[mid][0]
            elif vals[mid][1] > timestamp:
                r = mid - 1
            else:
                #if our timestamp is lower we want to keep track of this but also move right
                self.best = vals[mid][0]
                l = mid+1
        return self.best
            


        
