class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=self.sortbybegin)
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True
        
        
    def sortbybegin(self, element):
        return element[0]