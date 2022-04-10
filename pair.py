def getPairsCount(self, arr, n, k):
        # code here
        d={}
        cnt=0
        for i in range(n):
            if k-arr[i] in d: cnt+=d[k-arr[i]] 
                
            if arr[i] in d: d[arr[i]]+=1
            else: d[arr[i]]=1
                    
        return cnt