# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        prev, current = dummy, head

        while current and current.next:
            #save pointers
            nextPair = current.next.next
            second = current.next

            #reverse nodes
            current.next = nextPair
            second.next = current
            prev.next = second
            
            #change current and prev for the next iteration
            prev = current
            current = nextPair

        return dummy.next


            