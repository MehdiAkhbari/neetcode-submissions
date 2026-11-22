class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda l: l[0])
        print(intervals)
        out = []
        temp = intervals[0]
        
        for i in range(len(intervals) - 1):
            if temp[1] >= intervals[i + 1][0]:
                temp = [temp[0], max(temp[1], intervals[i + 1][1])]
                if i == (len(intervals) - 2):
                    out.append(temp)

            else:
                out.append(temp)
                temp = intervals[i + 1]
                if i == (len(intervals) - 2):
                    out.append(temp)

        if len(intervals) == 1:
            return [temp]
        else:
            return out
