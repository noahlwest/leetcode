class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = int(sqrt(area))
        w = int(sqrt(area))
        cur_area = l * w
        while cur_area != area:
            if cur_area < area:
                l += 1
            elif cur_area > area:
                w -= 1
            cur_area = l * w
        
        return [l, w]

#runtime: scales with area, not sure how to analyze this
#memory: O(1)