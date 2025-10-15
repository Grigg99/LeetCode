class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        pass_elem1 = {}
        pass_elem2 = {}
        answer = [[], []]

        for i in range(max(len(nums1), len(nums2))):
            if i < len(nums1):
                if nums1[i] not in nums2 and nums1[i] not in pass_elem1:
                    answer[0].append(nums1[i])
                    pass_elem1[nums1[i]] = True

            if i < len(nums2):
                if nums2[i] not in nums1 and nums2[i] not in pass_elem2:
                    answer[1].append(nums2[i])
                    pass_elem2[nums2[i]] = True

        return answer                 
        