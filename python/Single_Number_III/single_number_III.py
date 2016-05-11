'''
给予一个整数数组，其中两个元素只出现一次，其余元素都出现2次，找出两个只出现一次的元素.
例如nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
返回的结果顺序没有要求，[5, 3]也是对的
使用线性时间复杂度，常数级别空间复杂度
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = 0
        a = 0
        b = 0
        mask = 1
        for num in nums:
            xor ^= num
        
        # 从低位到高位找到第一个异或为0的位，也就是两个目标值从右到左第一个值不同的位
        while (xor & mask) == 0:
            mask = mask << 1
            
        # 两个目标值与mask相与刚好一个为0一个非0，这样就可以把结果分开
        for num in nums:
            if num & mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
