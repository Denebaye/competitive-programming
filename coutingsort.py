

def countingSort(arr):
    
    ans = [0] * 100

    for num in arr:
        ans[num] += 1
        
    return ans
