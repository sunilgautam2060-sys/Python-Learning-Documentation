

#this will make the new node.
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

#making nodes.
node1=ListNode(4)
node2=ListNode(5)
node3=ListNode(10)
node4=ListNode(13)
node5=ListNode(90)

#making links.
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node1

#assigning head as node1
head=node1


class Solution:
    def cycle_detection_II(self,head):
        fast=head
        slow=head

        while fast!=None and fast.next!=None : 
            fast=fast.next.next
            slow=slow.next

            if fast==slow:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next

                print("The starting node of the cycle is : ", fast.data)
                return


        print("There is no cycle")
        return None 

            
SolutionObject=Solution()
SolutionObject.cycle_detection_II(head) 