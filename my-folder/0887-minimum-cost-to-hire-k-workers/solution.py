import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # for every worker, if they have the worst pay ratio, then we pick k - 1 workers with
        # a better pay ratio of the least quality
        n = len(quality)
        ratios = [0 for _ in range(n)]
        workers = []
        for i in range(n):
            ratios[i] = (-wage[i] / quality[i], quality[i], i)
            
        s = sorted(ratios, key = lambda x : x[1])
        maxRatio = 0
        qSum = 0
        ans = 10000000000
        
        for i in range(k):
            heapq.heappush(workers, s[i])
            qSum += s[i][1]
            if -s[i][0] > maxRatio:
                maxRatio = -s[i][0]
                
        for i in range(k, n + 1):
            newAns = maxRatio * qSum
            ans = min(newAns, ans)
            if i != n:
                worker = heapq.heappop(workers)
                qSum -= worker[1]
                heappush(workers, s[i])
                maxRatio = -workers[0][0]
                qSum += s[i][1]
            
        return ans
        
