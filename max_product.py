def maxProduct(self,arr, n):
    p=pr=1
    mp=arr[0]
    mpr=arr[-1]
    for i in arr:
        if p==0: p=1
        p*=i
        mp=max(mp,p)
    for j in range(len(arr)-1,-1,-1):
        if pr==0: pr=1
        pr*=arr[j]
        mpr=max(mpr,pr)
    return max(mpr,mp)