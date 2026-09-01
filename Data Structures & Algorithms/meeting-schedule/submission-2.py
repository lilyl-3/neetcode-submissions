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
        result = []

        for interval in intervals:
            if not result or result[-1].end <= interval.start:
                result.append(interval)
            else:
                return False
        return True