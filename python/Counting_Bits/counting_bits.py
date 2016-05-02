'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2]
'''

'''
O(n) solution
'''
class Solution(object):
    def countBits(self, num):
        l = [0]
        for i in range(1, num + 1):
            if self.is_power_of_two(i):
                l.append(1)
                index = 0
            else:
                l.append(1 + l[index]) 
            index += 1
        return l

    # 是否是2的幂
    def is_power_of_two(self, n):
        return n != 0 and (n & (n - 1)) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.countBits(10))
