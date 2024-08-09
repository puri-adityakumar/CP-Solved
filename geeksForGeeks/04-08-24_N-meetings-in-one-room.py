# https://www.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1


class Solution:
    
    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        # code here
        meetings = [(start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x[1])

        count = 0
        last_end_time = 0
        
        for s, e in meetings:
            if s > last_end_time:
                count += 1
                last_end_time = e
                
        return count