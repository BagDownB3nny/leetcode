class Solution(object):
    def insert(self, intervals, newInterval):
        new_intervals = []
        new_inserted_interval = newInterval
        add_rest = False
        interval_added = False
        for interval in intervals:
            if add_rest:
                new_intervals.append(interval)
                continue
            if interval[1] < newInterval[0]:
                new_intervals.append(interval)
            elif interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1]:
                new_inserted_interval = [min(interval[0], new_inserted_interval[0]), max(interval[1], new_inserted_interval[1])]
            elif new_inserted_interval[1] < interval[0]:
                add_rest = True
                interval_added = True
                new_intervals.append(new_inserted_interval)
                new_intervals.append(interval)
        if len(new_intervals) == 0 or not interval_added:
            new_intervals.append(new_inserted_interval)
        return new_intervals

        
