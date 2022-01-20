class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def rev(end):
            start = 0
            while start < end:
                arr[start],arr[end] = arr[end],arr[start]
                #print(arr[start])
                start += 1
                end -= 1
                #print("haleluja")
        n = len(arr)
        ans = []
        for i in range(n-1,-1,-1):
            mxidx = i
            mxval = arr[i]
            for j in range(i-1,-1,-1):
                if arr[j] > mxval:
                    mxidx= j
                    mxval = arr[j]
                          
            
            if mxidx != i:
                rev(mxidx)
                rev(i)
                ans.append(mxidx + 1)
                ans.append(i + 1)
        return ans  
        
        
        
                
                        
                   
          