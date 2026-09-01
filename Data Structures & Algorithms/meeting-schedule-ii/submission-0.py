"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        rooms = 0
        max_rooms = 0
        s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                # A meeting starts before the earliest one ends
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                s += 1
            else:
                # A meeting has ended, so free a room
                rooms -= 1
                e += 1

        return max_rooms