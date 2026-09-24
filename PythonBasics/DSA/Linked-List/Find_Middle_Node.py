#here we use the concept of :totrise and hare , 
#fast will traverse by 2 times speed and slow by 1 times 
#and when the fast is at the end node we will note the position of slow ,
#that is the middle node which is what we required.


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#creating the node with value: 1 ,2,3,4,5.
node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)

#linking the nodes.
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5

#assigning node1 as head node.
head=node1

#up to this we only created the linked_list ,below we create the class Solution and
#write the solution in method:deleteMiddle().


class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow=head
        fast=head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        print("The Middle of the linked_list is:", slow.val)

SolutionObject=Solution()
SolutionObject.middleNode(head)        

