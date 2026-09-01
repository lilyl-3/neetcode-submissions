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
        meetings = []

        for interval in intervals:
            if not meetings or meetings[-1].end <= interval.start:
                meetings.append(interval)
            else:
                return False
        return True
