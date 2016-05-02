'''
给予一个Integer数组，除了某个元素出现一次外其余元素出现两次，请找出出现一次的那个元素
要求线性复杂度并且不使用额外空间
'''

'''
对所有元素进行异或，最终得到的就是出现一次的那个元素
'''
class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x, y: x^y, nums)
