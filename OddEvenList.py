# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class OddEvenList:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head) or (not head.next):
            return head

        temp1 = head
        head2 = temp2 = head.next

        while (temp2 and temp2.next):
            temp1.next = temp2.next
            temp1 = temp1.next
            temp2.next = temp2.next.next
            temp2 = temp2.next
        
        temp1.next = head2
        return head
