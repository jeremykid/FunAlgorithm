class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        #sortInterval
        if (not len(intervals)):
            return []
        
        startSortedIntervals = sorted(intervals, key=self.sortByStartFunction)
        
        startIndex = 0
        start = 0
        end = 0
        results = []
        while startIndex < len(intervals):
            if (startSortedIntervals[startIndex].start > end):

                if (startIndex != 0):
                    results.append([start, end])

                start = startSortedIntervals[startIndex].start
                end = startSortedIntervals[startIndex].end
            elif (startSortedIntervals[startIndex].end > end):
                end = startSortedIntervals[startIndex].end

            startIndex = startIndex + 1

        if (startSortedIntervals[-1].end > end):
            end = startSortedIntervals[-1].end
        results.append([start, end])
        
        return results


    def sortByStartFunction(self, interval):
        return interval.start   