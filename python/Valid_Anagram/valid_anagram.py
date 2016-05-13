'''
给予两个字符串s和t，写一个函数判断t是否是s的回文(即s跟t的差别在于字母的顺序)

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
字符串只包含小写字母
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        for c in t:
            if c in d:
                d[c] -= 1
            else:
                return False
                
        for k, v in d.items():
            if v is not 0:
                return False
        return True
