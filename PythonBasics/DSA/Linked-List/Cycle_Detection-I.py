


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next


#making Linked-List manually.
Node1=ListNode(8)
Node2=ListNode(9)
Node3=ListNode(13)
Node4=ListNode(21)

#Linking the Node manually.
Node1.next=Node2
Node2.next=Node3
Node3.next=Node4
Node4.next=Node1

#assigning Node1 as Head.
head=Node1

class Solution:
 
   def has_cycle(self,head):
      slow=head
      fast=head
     
      while fast!=None and fast.next!=None:
         slow=slow.next
         fast=fast.next.next
     
         if slow==fast:
            print("The Link_List has cycle ")
            return True
     
      print("The Link_List does not have cycle ")
      return False

                
SolutionObject=Solution()
SolutionObject.has_cycle(head)          