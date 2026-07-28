class Solution:
    def maxsubarray(self, nums):
        max_num = nums[0]
        current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_num = max(max_num, current_sum)
        return max_num
obj = Solution()
print(obj.maxsubarray([5, -2, 8, -1, 6, -3, 4, 2]))