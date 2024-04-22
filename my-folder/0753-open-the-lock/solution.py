from queue import Queue

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def increaseLock(index, current):
            newCurrent = ""
            for i in range(4):
                if i == index:
                    newDigit = int(current[i]) + 1
                    if newDigit == 10:
                        newCurrent += "0"
                    else:
                        newCurrent += str(newDigit)
                else:
                    newCurrent += current[i]
            return newCurrent
        
        def decreaseLock(index, current):
            newCurrent = ""
            for i in range(4):
                if i == index:
                    newDigit = int(current[i]) - 1
                    if newDigit == -1:
                        newCurrent += "9"
                    else:
                        newCurrent += str(newDigit)
                else:
                    newCurrent += current[i]
            return newCurrent
                    
        visited = set()
        deadendsSet = set()
        for deadend in deadends:
            deadendsSet.add(deadend)
            if deadend == "0000":
                return -1
        q = Queue()
        q.put("0000")
        steps = -1
        while not q.empty():
            currentLocks = q.qsize()
            steps += 1
            for i in range(currentLocks):
                current = q.get()
                if current == target:
                    return steps
                if current in visited:
                    continue
                else:
                    visited.add(current)
                for n in range(4):
                    increasedLock = increaseLock(n, current)
                    decreasedLock = decreaseLock(n, current)
                    if increasedLock not in deadendsSet and increasedLock not in visited:
                        q.put(increasedLock)
                    if decreasedLock not in deadendsSet and decreasedLock not in visited:
                        q.put(decreasedLock)
        return -1
                    
                
        
            
