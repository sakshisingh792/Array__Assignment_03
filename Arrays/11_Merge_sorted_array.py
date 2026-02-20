def merge(arr1,arr2):
    arr3=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr3.append(arr1[i])
        else:
            arr3.append(arr2[j])

    arr3.extend(arr1[i:])
    arr3.extend(arr2[j:])  
    return arr3          


arr1=[1,2,5]
arr2=[2,4,6]
merge(arr1,arr2)
