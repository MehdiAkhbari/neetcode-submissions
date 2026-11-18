# idea: sort by starting time O(nlogn), then check if each interval's end is later than the next one's start date, return false if you find any 
# The sort method is something you need to know:  intervals.sort(key=lambda x: x.start)
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        else:
            return True