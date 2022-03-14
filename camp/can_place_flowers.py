class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        count = 0
        ptr = 0
        while ptr < len(flowerbed):
            
            if flowerbed[ptr] == 1:  
                ptr += 2
            elif N == 1 and flowerbed[ptr] == 0:
                count += 1
                break
            elif flowerbed[ptr] == 0 and ptr + 1 < len(flowerbed) and flowerbed[ptr + 1] == 0:
                count += 1
                ptr += 2
            elif ptr == N - 1 and ptr and flowerbed[ptr] == 0 and flowerbed[ptr - 1] == 0:
                count += 1  
                break
            else: 
                ptr += 3
        
        return count >= n