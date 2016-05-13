'''
给予一个整数数组，判断数组是否包含重复.你的函数应该返回true如果任何值在数组中至少出现两次，并且应该返回false如果每个元素是独立的.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        s = set(nums)
        if len(s) != len(nums):
            return True
        return False
        
