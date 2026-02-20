def remove_dup(arr):
    res=[]
    for num in arr:
        if num not in res:
            res.append(num)
    return res


arr=[1,1,3,4,5,3,4]
remove_dup(arr)
