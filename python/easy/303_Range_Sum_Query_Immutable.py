class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = []
        sum = 0
        for num in nums:
            sum += num
            self.arr.append(sum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.arr[right]
        return self.arr[right] - self.arr[left-1]

#init: O(n)
#sumRange: O(1)