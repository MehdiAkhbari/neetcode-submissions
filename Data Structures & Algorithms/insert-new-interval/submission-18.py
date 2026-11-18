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
        # print(i)
        # print(output)

        return output