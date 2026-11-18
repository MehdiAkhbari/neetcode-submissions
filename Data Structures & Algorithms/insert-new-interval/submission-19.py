# My idea (after watching the video):
# 1. If intervals is empty, return newInterval
# 2. Otherwise: there are three cases when comparing intervals[i] and newInterval:
    # i. newInterval is completely before intervals[i]: first append newInterval to output, then add the rest of "intervals" to output and FINISH
    # ii. newInterval is completely after intervals[i]: append intervals[i] and increase i
    # iii. if newInterval and intervals[i] are overlapping: merge the two intervals (start=min of starts , end = max(ends)) and update newInterval, don't append it to output yet beacuse we still may need to merge it with the next intervals
    # In cases ii, iii nothing is appended. We only append in these cases when i = len(intervals) - 1 (in the last repetition if it is not already appended (which we automatically get into))

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
 
        if intervals == []:
            return [newInterval]

        output = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:   # completely before
                output.append(newInterval)
                output = output + intervals[i : ]
                break

            elif newInterval[0] > intervals[i][1]: # completely after
                output.append(intervals[i])
                if i == len(intervals) - 1:
                    output.append(newInterval)
            else: # overlap
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                if i == len(intervals) - 1:
                    output.append(newInterval)

        return output