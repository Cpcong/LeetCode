'''
给予一个非空整型数组，返回K个出现频率最高的元素
例如[1,1,1,2,2,3], k = 2, 返回 [1,2]
要求：算法必须优于O(nlogn), n为数组大小
'''

#solution : O(kn)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        r = []
        # d记录每个元素出现的次数
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        # 每次取出出现次数最多的元素，并从d中删除
        for i in range(k):
            max = 0
            for key, value in d.items():
                if value > max:
                    max = value
                    maxKey = key
            r.append(maxKey)
            del d[maxKey]
        return r


