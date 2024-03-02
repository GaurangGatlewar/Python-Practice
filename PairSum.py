# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class PairSum:
    def pairSum(self, head: Optional[ListNode]) -> int:
        middle_node = self.findMiddleNode(head)
        next_node = middle_node.next
        middle_node.next = None
        tail = self.reverseLinkedList(next_node)
        maxSum = float(-inf)
        while head and tail:
            if (head.val+tail.val)>maxSum:
                maxSum = head.val+tail.val
            head = head.next
            tail = tail.next
        return maxSum

    def findMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:return head
        temp1 = head
        temp2 = head.next
        while (temp2 and temp2.next):
            temp1 = temp1.next
            temp2 = temp2.next.next
        return temp1

    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev