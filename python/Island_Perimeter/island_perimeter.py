'''
给予一个2维网格，1表示陆地，0表示水。网格单元水平/垂直(非对角) 连接。网格完全被水包围，并且只有一个岛屿(由一块或多块陆地单元组成)。
岛屿没有湖泊(内部的水跟岛屿周围的水没有连接)。一个单元是长度为1的正方形。网格是长方形的，宽 度和高度都没有超过100
求出岛屿的周长


Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
'''

'''
解题思路:
假设有n个陆地单元，m对连接的陆地单元，如果不考虑连接的部分，总的周长为4*n，考虑每有
一对连接的陆地单元，总的周长减2，此时总的周长为4*n - m * 2。

因此我们可以先求总的陆地单元数，再求出有多少对陆地单元相邻

'''
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        if grid is None:
            return perimeter
        num_of_1 = 0
        cnt = 0
        width = len(grid[0])
        height = len(grid)
        # 从左往右,从上往下遍历，求陆地单元总数同时求出在左右方向上有多少对陆地单元连接
        for i in range(height):
            for j in range(width):
                if grid[i][j] is 1:
                    num_of_1 += 1
                    if j >= 1 and grid[i][j - 1] is 1:
                        cnt += 1
        # 从上往下，从左往右遍历，求上下方向有多少对陆地单元连接
        for i in range(width):
            for j in range(1, height):
                if grid[j - 1][i] is 1 and grid[j][i] is 1:
                    cnt += 1
        result = num_of_1 * 4 - cnt * 2
        return result
    
