'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
写一个函数删除链表中的一个节点（除了尾节点），你能拿到的是要删除的那个节点
例如linked list 是 1 -> 2 -> 3 -> 4，你拿到值为3的节点，调用你的函数后linked list应该变为1->2->4
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
