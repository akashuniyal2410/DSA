def maxi(arr,n):
    s=ms=0
    for i in arr:
        s=max(0,s+i)
        ms=max(s,ms)
    return ms



if __name__=="__main__":
   li=list(map(int,input().split()))
   print(maxi(li,len(li)))