#Products of array discluding self Solution
class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)

        answer[0] = 1
        for i in range(1,len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        
        prev = 1
        for i in range(len(nums)-2,-1,-1):
            prev *= nums[i+1]
            answer[i] *= prev

        return answer
