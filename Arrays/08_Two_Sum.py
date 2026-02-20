def pair(arr,target):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i]+arr[j]==target:
                return (arr[i],arr[j])


arr=[1,2,3,4,5]
target=3
pair(arr,target)
