class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum = 1
        answer = nums
        flag = False
        flag2 = False
        for i in nums:
            if i!=0:
                sum *= i
            else:
                if flag:
                    flag2 = True
                flag = True
        for index, i in enumerate(nums):
            if not flag2:
                if i!=0:
                    if flag:
                        answer[index] = 0
                    else:
                        tmp = sum/i
                        answer[index] = int(tmp)
                else:
                    answer[index] = int(sum)
            else:
                answer[index] = 0                    
        return answer
        