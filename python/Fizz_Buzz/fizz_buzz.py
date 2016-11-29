'''
编写程序输出数字1到n的字符串表达式.
但对3的倍数的数字应该输出"Fizz"，5的倍数应该输出"Buzz"，既是3又是5的倍数输出"FizzBuzz".

Example:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

'''

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rlist = []
        for i in range(1, n + 1):
            if i % 5 is 0 and i % 3 is 0:
                rlist.append("FizzBuzz")
            elif i % 3 is 0:
                rlist.append("Fizz")
            elif i % 5 is 0:
                rlist.append("Buzz")
            else:
                rlist.append(str(i))
        return rlist