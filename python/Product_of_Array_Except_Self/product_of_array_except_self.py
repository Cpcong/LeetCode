'''
给予一个大小为n(n > 1)的整数数组nums，返回一个数组output比如output[i]等于除了它之外其他元素的乘积

不用除法并且时间复杂度为O(n)

For example, given [1,2,3,4], return [24,12,8,6].

常数级别空间复杂度(Note: 返回的数组output使用的空间不算进空间复杂度)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        result = [1]*length
        # 计算每个元素左边元素的累乘
        for i in range(1, length):
            result[i] = result[i - 1] * nums[i - 1]
        tmp = 1
        # 计算每个元素右边元素的累乘
        for i in range(0, length)[::-1]:
            result[i] = result[i] * tmp
            tmp *= nums[i] 
        return result

