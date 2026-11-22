# Idea is kind of similar to the previous question: First, sort the intervals ased on their first element (that's critical)
# Then, for each two consecutive indices i, i + 1: if they overlap (end of first is larger the the beginning of the second), merge them: start = min(starts) = start[i], end = max of ends (could be either of i and i+1), keep the merged value in memory, here I call it temp (don't add it to output yet as me may still want to merge it with next intervals)
# If they don't overlap, append intervals[i] to the output, and set temp to be the second element (intervals[i+1])
# We need to append the "temp" variable when i == len(intervals) - 2

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda l: l[0])
        print(intervals)
        out = []
        temp = intervals[0]
        
        for i in range(len(intervals) - 1):
            if temp[1] >= intervals[i + 1][0]:
                temp = [temp[0], max(temp[1], intervals[i + 1][1])]


            else:
                out.append(temp)
                temp = intervals[i + 1]
            if i == (len(intervals) - 2):
                out.append(temp)

        if len(intervals) == 1:
            return [temp]
        else:
            return out
