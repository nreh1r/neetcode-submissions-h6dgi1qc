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

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode d;
        ListNode* dummy = &d;
        ListNode* curr = dummy;
        ListNode* left = head;
        ListNode* right = head;

        while (right) {
            for (size_t i = 0; i < k - 1; i++) {
                right = right->next;
                if (right == nullptr) {
                    break;
                }
            }

            if (right == nullptr) {
                break;
            }

            ListNode* temp = right->next;
            right->next = nullptr;
            right = temp;
            ListNode* revList = reverseList(left);
            curr->next = revList;
            left->next = temp;
            curr = left;
            left = right;
        }

        return dummy->next;
    }

    ListNode* reverseList(ListNode* lst) {
        ListNode* tail = nullptr;
        ListNode* curr = lst;

        while (curr) {
            ListNode* temp = curr->next;
            curr->next = tail;
            tail = curr;
            curr = temp;
        }

        return tail;
    }
};
