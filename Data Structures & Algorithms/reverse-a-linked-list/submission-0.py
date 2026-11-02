# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive solution:
        # Algorithm: Pseudocode
        # 1. If the list is empty, return null.
        # 2. Recursively call the function on head.next to reverse the rest of the list.
        # 3. After the recursive call returns:
        # Make the head.next.next = head so the next node points back to the current node.
        # 4. Set head.next = null
        # 5. Return the new head returned by the deepest recursive call
        # Time: O(N) Space: O(N)
        if not head: 
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None

        return newHead