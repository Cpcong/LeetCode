'''
有n个灯泡初始为off. 你首先打开所有灯泡. 然后，你关闭每第二个灯泡.在第三轮，你切换每第3个灯泡(如果打开则关闭或者如果关闭则打开). 在第i轮，你切换每第i个灯泡. 直到第n轮，你只切换最后一个灯泡. 找出n轮后有多少个灯泡打开着

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
'''

'''
如果灯泡被切换奇数次，则打开. 如果切换偶数次，则关闭.

证明:

我们可以总结出灯泡i将切换k次
这里，k是i的因子数(除了1)
k + 1 是i的所有因子数

我们知道当p是i的因子时，q=i/p也是i的因子（即成对出现）
如果i没有这样一个因子p使得p=i/p，则k + 1是偶数
如果i有这样一个因子p使得p=i/p（i = p^2, i是p的完美平方），则k + 1是奇数
所以
如果i是完美平方（即开方后为整数）, k+ 1 是奇数, k 是偶数 (灯泡i打开).
如果i不是完美平方 , k+ 1 是偶数, k 是奇数 (灯泡i关闭).

我们要找出有多少个灯泡在n轮后打开着，这意味这我们需要找出有多少个完美平方数，该值等于最大完美平方数的平方根

结论:

最大的完全平方数的平方根就是sqrt(n)的整数部分.


'''
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)
