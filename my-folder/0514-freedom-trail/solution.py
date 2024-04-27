class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}
        
        def turnToLetter(index: int, letter: str, isTurnClockwise: bool):
            currentLetter = ring[index]
            turns = 0
            while (currentLetter != letter):
                if isTurnClockwise:
                    index = (index + 1) % len(ring)
                else:
                    index = (index - 1 + len(ring)) % len(ring)
                turns += 1
                currentLetter = ring[index]
            return [turns, index]
        
        def helper(currentIndex: int, currentDialIndex: int):
            memoKey = str(currentIndex) + ", " + str(currentDialIndex)
            if memoKey in memo:
                return memo[memoKey]
            if currentIndex == len(key):
                return 0
            [turnClockwiseTurns, turnClockwiseIndex] = turnToLetter(currentDialIndex, key[currentIndex], True)
            [turnAnticlockwiseTurns, turnAnticlockwiseIndex] = turnToLetter(currentDialIndex, key[currentIndex], False)
            nextIndex = currentIndex + 1
            if turnClockwiseTurns == 0:
                ans = helper(nextIndex, currentDialIndex)
                memo[memoKey] = ans
                return ans
            elif turnAnticlockwiseTurns == 0:
                ans = helper(nextIndex, currentDialIndex)
                memo[memoKey] = ans
                return ans
            else:
                ans = min(helper(nextIndex, turnClockwiseIndex) + turnClockwiseTurns, helper(nextIndex, turnAnticlockwiseIndex) + turnAnticlockwiseTurns)
                memo[memoKey] = ans
                return ans
                
            
        return helper(0, 0) + len(key)
            
