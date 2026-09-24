

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
Node4.next=None

#assigning Node1 as Head.
head=Node1


class Solution:
     def reverseList(self, head: ListNode | None) -> ListNode | None:

        current=head
        previous=None

        #logic to reverse link-list
        while current!=None:
            front=current.next
            current.next=previous
            previous=current
            current=front


        #print the reversed linked_list.
        head=previous 
        current=head

        while current!=None:
            print(current.val , end=" ")
            current=current.next


SolutionObject=Solution()
SolutionObject.reverseList(head)           

