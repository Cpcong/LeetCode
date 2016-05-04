'''
给出一个非负整数，重复对该整数所有位相加，直到剩下一位整数
比如38，3 + 8 = 11， 1 + 1 = 2，return 2
要求不用循环/递归，O(1)
'''

class Solution(object):
    def addDigits(self, num):
    """
    :type num: int
    :rtype: int
    """
    if (num % 9 == 0) and (num != 0):
        return 9
    else:
        return num % 9
