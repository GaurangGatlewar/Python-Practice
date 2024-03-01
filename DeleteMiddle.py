# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class DeleteMiddle:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = head
        try:
            temp2 = temp1.next.next
        except:
            return None
            
        while (temp2 and temp2.next):
            temp2 = temp2.next.next
            temp1 = temp1.next
        temp1.next = temp1.next.next
        return head