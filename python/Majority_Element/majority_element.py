'''
给予一个大小为n的数组，找到多数元素，多数元素就是出现次数大于⌊ n/2 ⌋ 的元素.
假设数组非空，而且多数元素总是存在.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        d = {}
        length = len(nums)
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for k, v in d.items():
            if v >= (length / 2.0):
                return k
           
