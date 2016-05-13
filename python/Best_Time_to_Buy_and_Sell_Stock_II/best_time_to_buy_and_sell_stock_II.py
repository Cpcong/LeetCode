'''
给予一个数组，第i个元素的值为一支股票在第i天的价格.

设计一个算法找到最大收益，你可以尽可能多的交易(多次买入卖出)，然而在你买之前要卖掉之前买的.
'''


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit=0
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                profit+=(prices[i+1]-prices[i])
        return profit
