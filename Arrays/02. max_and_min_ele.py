def max_min(arr):
    minm=arr[0]
    maxm=arr[0]
    for i in range(len(arr)):
        if arr[i]>maxm:
            maxm=arr[i]
        elif arr[i]<minm:
            minm=arr[i]

    return maxm,minm



arr=[1,2,3,4,5,6]
maxm,minm = max_min(arr)
print("maxm:",maxm)
print("minm: ",minm)
