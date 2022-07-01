'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
'''

class Solution:
    def minMeetingRooms(self, intervals):
        # e is pointer to first available room
        e = rooms = 0
        # Intervals based on start times
        start = sorted(i[0] for i in intervals)
        # Intervals based on end times
        end = sorted(i[1] for i in intervals)
        
        for s in range(len(start)):
            if start[s] < end[e]: 
                rooms += 1
            else: 
                e += 1
        return rooms


input = [[0, 30], [5, 10], [15, 20]]
sol = Solution()
print(sol.minMeetingRooms(input))
