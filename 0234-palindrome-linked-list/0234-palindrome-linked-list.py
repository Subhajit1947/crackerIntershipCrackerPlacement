# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=''
        temp=head
        while temp:
            s+=str(temp.val)
            temp=temp.next
        for i in range(len(s)//2):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True