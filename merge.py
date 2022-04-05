def merge(arr1,arr2):
    i,j=len(arr1)-1,0
    while i>-1 and j<len(arr2):
          if arr1[i]>arr2[j]:
             arr1[i],arr2[j]=arr2[j],arr1[i]
             i-=1
             j+=1
          else: j+=1
    arr1.sort()
    arr2.sort()  
             




if __name__=="__main__":
   arr1=list(map(int,input().split()))
   arr2=list(map(int,input().split()))
   merge(arr1,arr2)
   print(arr1,arr2)