"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # need to sort first!!
        intervals.sort(key=lambda x: x.start)
        merged_intervals = []

        for interval in intervals:
            if not merged_intervals or merged_intervals[-1].end <= interval.start:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1] = Interval(min(merged_intervals[-1].start, interval.start), max(merged_intervals[-1].end, interval.end))
                return False
        
        return True