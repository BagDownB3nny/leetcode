class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        fracs = []
        for i in range(n):
            for j in range(i, n):
                num = arr[i]
                dem = arr[j]
                frac = num / dem
                fracs.append([num, dem, frac])
        sortedFracs = sorted(fracs, key = lambda x: x[2])
        return sortedFracs[k - 1][:2]
                
            
