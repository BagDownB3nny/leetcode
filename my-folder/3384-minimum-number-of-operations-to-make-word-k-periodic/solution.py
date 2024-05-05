class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        count = {}
        i = 0
        subwords = int(len(word) / k)
        highest = 0
        while i <= len(word):
            s = word[i : i + k]
            if len(s) == 0:
                break
            if s in count:
                count[s] += 1
                if count[s] > highest:
                    highest = count[s]
            else:
                count[s] = 1
                if count[s] > highest:
                    highest = count[s]
            i += k
        return subwords - highest
        
