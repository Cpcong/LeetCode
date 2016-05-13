'''
给予一列exelc表的标题，返回相应的列数目

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        column = 0
        for i in range(len(s)):
            column = column * 26 + ord(s[i]) - 64
        return column
