class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        occs = {}

        for i in arr:
            if i not in occs:
                occs[i] = 1
            else:
                occs[i] += 1
            
        tmp = arr[0]
        flags = {}
        for occ in occs:
            if occs[occ] not in flags:
                flags[occs[occ]] = True
            else: 
                return False
            
        return True