'''
给予一个数组，将值为0的元素移动至最后，并保证非0元素的相对位置不变
例如nums = [0, 1, 0, 3, 12], 调用方法后nums应该为[1, 3, 12, 0, 0].
要求原地操作，不可复制数组
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=0 
        # step1:remove all 0 element
        for i in nums:
            if i != 0:
                nums[k]= i
                k+=1

        nums[k:]=[0]*(len(nums)-k) #step2: set the rest of the list to be zero


