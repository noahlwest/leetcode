class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        counter = 0
        length = len(flowerbed)
        for i in range(0, length):
            #special cases: i == 0 or i == length-1
            if i == 0 and flowerbed[i] == 0 and i+1 < length and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                counter += 1
            elif i == length-1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                flowerbed[i] = 1
                counter += 1
            elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                counter += 1
            else:
                pass
                
        return counter >= n

#runtime: O(n)
#memory: O(1)