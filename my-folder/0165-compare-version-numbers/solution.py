class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        print(version1)
        print(version2)
        def goToInt(s, ptr):
            while ptr < len(s) and s[ptr] == "0":
                ptr += 1
                
            return ptr
        
        def getInt(s, ptr):
            newS = []
            
            while ptr < len(s) and s[ptr] != ".":
                newS.append(s[ptr])
                ptr += 1
            if len(newS) == 0:
                return 0
            else:
                return int("".join(newS))
    
        def goToDot(s, ptr):
            while ptr < len(s) and s[ptr] != ".":
                ptr += 1
            return ptr
            
        ptr1 = 0
        ptr2 = 0
        
        while ptr1 < len(version1) and ptr2 < len(version2):  
            print(ptr1)
            print(ptr2)
            ptr1 = goToInt(version1, ptr1)
            ptr2 = goToInt(version2, ptr2)
            i1 = getInt(version1, ptr1)
            i2 = getInt(version2, ptr2)
            if i1 > i2:
                return 1
            elif i2 > i1:
                return -1
            ptr1 = goToDot(version1, ptr1) + 1
            ptr2 = goToDot(version2, ptr2) + 1
            
        while ptr1 < len(version1):  

            ptr1 = goToInt(version1, ptr1)
            i1 = getInt(version1, ptr1)
            if i1 > 0:
                return 1

            ptr1 = goToDot(version1, ptr1) + 1
            
        while ptr2 < len(version2):  

            ptr2 = goToInt(version2, ptr2)
            i2 = getInt(version2, ptr2)
            if i2 > 0:
                return -1

            ptr2 = goToDot(version2, ptr2) + 1
        
        return 0
        
