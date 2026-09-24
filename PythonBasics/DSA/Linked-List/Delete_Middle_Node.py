


# Definition for singly-linked list.
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
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:

        # If there is only one node
        if head.next == None:
            return None

        n = 0 #it calculate the total node in linked_list.
        current = head

        # this will traverse entire linked_list and calculate n .
        while current != None:
            n += 1
            current = current.next

        # Middle index
        k = n // 2

        # Move to node BEFORE the middle
        current = head
        x = 0

        while x != k - 1:
            current = current.next
            x += 1

        # Delete middle node
        current.next = current.next.next

        #this block will print the linked_list after middle node gets deleted.
        current=head
        while current!=None:
            print(current.val,end=" ")
            current=current.next



SolutionObject=Solution()
SolutionObject.deleteMiddle(head)