class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        
        start = sorted_intervals[0][0]
        end = sorted_intervals[0][1]
        ret = []
        for index, interval in enumerate(sorted_intervals):
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                ret.append([start, end])
                start = interval[0]
                end = interval[1]
            if index == len(sorted_intervals)-1:
                ret.append([start, end])
                
        return ret

    #runtime: O(n log n)
    #memory: O(n)