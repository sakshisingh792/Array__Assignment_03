def find(arr):
    n=len(arr)+1
    total_sum=n*(n+1)//2
    act_sum=0
    for num in arr:
        act_sum+=num

    return total_sum-act_sum


arr=[1,2,4,5]
find(arr)
