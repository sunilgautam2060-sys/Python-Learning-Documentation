

#this will make a new node.
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

class solution:
    def length_of_cycle(self,head):
        fast=head
        slow=head
        count=0

        #traversing logic of fast and slow pointer.
        while fast is not None and fast.next is not None:

            fast=fast.next.next
            slow=slow.next

            #fast and slow will meet in the  any node .
            #if cycle exists if there is no cycle than they will never meet.
            if fast==slow:
                slow=slow.next    #move slow one at a time put fast as it is 
                count+=1          #than count one by one ,there is cycle so ,slow will again come at fast node for sure.
                         

                while fast!=slow:   #this will keep increasing slow and keep counting length .
                    slow=slow.next
                    count+=1

                print("The Length of Linked List cycle is:",count)
                return


        print("Length is 0 there is no cycle  ")      
        return

solutionobject=solution()
solutionobject.length_of_cycle(head)      
                    