# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Algorithm: Solved Iteratively
1. Create a dummy node and a node pointer pointing to it.
2. While both lists have nodes:
    Compare list1.val and list2.val
    Attach the smaller node to node.next
    Move forward in the chosen list.
    Move node to node.next.
3. When one list becomes empty:
    Attach the remaining nodes of the other list to node.next
4. Return dummy.next, which is the head of the merged list
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2: 
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next

        # time : O(n + m)
        # space: O(1)
        