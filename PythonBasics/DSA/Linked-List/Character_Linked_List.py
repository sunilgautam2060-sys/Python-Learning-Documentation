

class Listnode:
    def __init__(self,data):
        self.data=data
        self.next=None


#making nodes.
node1=Listnode("T")
node2=Listnode("h")
node3=Listnode("e")
node4=Listnode("/")
node22=Listnode("/")
node5=Listnode("s")
node6=Listnode("k")
node7=Listnode("y")
node8=Listnode("/")
node9=Listnode("i")
node10=Listnode("s")
node11=Listnode("/")
node12=Listnode("*")
node13=Listnode("b")
node14=Listnode("l")
node15=Listnode("u")
node16=Listnode("e")


#linking the nodes.
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node22
node22.next=node5
node5.next=node6
node6.next=node7
node7.next=node8
node8.next=node9
node9.next=node10
node10.next=node11
node11.next=node12
node12.next=node13
node13.next=node14
node14.next=node15
node15.next=node16
node16.next=None

#assigning head as node1
head=node1

#pointing current to head to traverse to keep head in head position.
current=head

#problem logic .
class solution:
    def traversal(self):
        
        current=head
        
        while current!=None:
            print(current.data,end="")
            current=current.next

            

    def change_sentence(self,head):
        current=head

        print("Before:")
        self.traversal()

        while current!=None:

            if current.data=="/" or current.data=="*":
                current.data=" "

                if current.next.data=="/" or current.next.data=="*":
        
                    current.next.next.data=current.next.next.data.upper()
                    current.next=current.next.next
                    

            current=current.next

        current=head

        print("\nAfter:")
        self.traversal()
       

solutionobject=solution()
solutionobject.change_sentence(head)

