class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        def getPlacement(i):
            match i:
                case 0:
                    return "Gold Medal"
                case 1:
                    return "Silver Medal"
                case 2:
                    return "Bronze Medal"
                case _:
                    return str(i + 1)
        
        sortedScores = sorted(score, reverse=True)
        ans = ["" for _ in range(len(score))]
        for i, s in enumerate(sortedScores):
            index = score.index(s)
            ans[index] = getPlacement(i)
        return ans
            
