# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # for i in range(1, len(head)):
        #     key = head[i]
        #     j = i - 1

        #     while j >= 0 and head[j] > key:
        #         head[j + 1] = head[j]
        #         j -= 1

        #     head[j + 1] = key
        # return head

        # For Leetcode
        dummy = ListNode(0)
        curr = head  # current node from the original list

        while curr:
            # Save next node before we re-link curr
            next_node = curr.next

            # Find position in sorted part (dummy -> sorted list)
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next

            # Insert curr between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # Move to the next node in original list
            curr = next_node

        return dummy.next


        

head = [-1,5,3,4,0]
sol = Solution()
result = sol.insertionSortList(head)
print(result)