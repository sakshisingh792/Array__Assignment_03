def rot_right(arr,k):
    n=len(arr)
    temp=arr[-k:]
    for i in range(n-k-1,-1,-1):
        arr[i+k]=arr[i]

    for i in range(k):
        arr[i]=temp[i]


    return arr



arr=[1,2,3,4,5]
k=2
rot_right(arr,k)
