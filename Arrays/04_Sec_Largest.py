def sec_lar(arr):
    largest=float("-inf")
    sec=float("-inf")
    for num in arr:
        if num>largest:
            sec=largest
            largest=num
        elif num>sec and num!=largest:
            sec=num
    return sec



arr=[1,2,3,4,5]
sec_lar(arr)
