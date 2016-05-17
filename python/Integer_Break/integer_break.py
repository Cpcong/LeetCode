'''
给予一个正整数n，把n分解成至少2个正整数(分解后所有整数的和等于n)，使得分解后的所有整数的乘积最大，返回它们的乘积

Note:假设n不小于2
'''

'''
解题思路：可以试着分解7到10去发现规律
7 --> 3, 4
8 --> 3, 3, 2
9 --> 3, 3, 3
10 --> 3, 3, 4
11 --> 3, 3, 3, 2
通过分析得到：尽量分解出更多的3(剩余4的话不可再分)
'''

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n is 2:
            return 1
        if n is 3:
            return 2
        if n % 3 is 0:
            return 3**(n/3)
        elif n %3 is 1:
            return 3**(n/3 - 1) * 4
        else:
            return 3**(n/3) * 2
