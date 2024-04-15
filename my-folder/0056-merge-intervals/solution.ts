function merge(intervals: number[][]): number[][] {

    if (intervals.length == 0) {
        return intervals;
    }

    const compare = (a: number[], b: number[]): number => {
        if (a[0] > b[0]) {
            return 1;
        } else if (a[0] < b[0]) {
            return -1;
        } else {
            return 0;
        }
    }

    intervals.sort(compare);

    let currentInterval = intervals[0];
    const newIntervals = [];
    for (const interval of intervals) {
        if (currentInterval[1] >= interval[0]) {
            currentInterval[1] = Math.max(interval[1], currentInterval[1]);
        } else {
            newIntervals.push(currentInterval);
            currentInterval = interval;
        }
    }
    newIntervals.push(currentInterval);
    return newIntervals;
};
