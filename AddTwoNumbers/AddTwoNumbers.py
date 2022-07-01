# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Reference: https://www.youtube.com/watch?v=ZgTOSvc-Z1c&ab_channel=CodingKevinBKH
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 #預設carry = 0
        dummy = ListNode() #紀錄答案
        current = dummy #指向答案，以便更新
        
        while l1 != None or l2 != None:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            current.next = ListNode(carry % 10) #將carry mod 10，將餘數加到答案
            carry = 1 if carry >=10 else 0 #更新carry
            current = current.next #移動current pointer到下一個位置
        
        if carry != 0: #檢查carry 是否為0
            current.next = ListNode(carry) #如果有，將其加到下一node
        return dummy.next #return ans