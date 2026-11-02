/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Iteration Solution:
// Algorithm
// 1. Initialize;
// prev = null
// curr = head
// 2. While curr exists
// Save the next node: temp = curr.next
// Reverse the pointer: curr.next = prev
// move prev to curr
// move curr to temp
// when the loop ends, prev is the new head of the reversed list.
// return prev.

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr) {
            ListNode* temp = curr-> next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        return prev;

        // time: O(n)
        // space: O(1)
    }
};
