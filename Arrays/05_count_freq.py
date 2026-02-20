def count_freq(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    return freq        

arr=[1,1,2,2,2,3,45,4,3,4]
count_freq(arr)
