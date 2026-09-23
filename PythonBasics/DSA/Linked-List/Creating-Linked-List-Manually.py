
### OOP and Data Structures

#**Why List was easier:**
#Python already provides the List data structure, so I can directly create and solve problems using it.
#
#**Why Linked List is different:**
#Python does not provide a simple built-in Linked List. I need to understand how a **Node** stores:
#
#* `Data`
#* `Next` → reference to the next node
#
#**Do I need to learn full OOP first?**
#No. I only need the basic OOP concepts required to create a Node:
#
#* `class`
#* `__init__()`
#* `self`
#* object
#
#I do **not** need to study full OOP before continuing DSA.
#
#**Learning approach:**
#Learn the minimum OOP needed → create and understand Node → understand Linked List → solve a few important problems → move to the next data structure.
#
#**Main idea:**
#I should understand how a data structure works internally once, but I don't need to repeatedly implement the entire data structure for every problem.


#This will Create A Node.
class Node:
 def __init__(self,data):
       self.data=data
       self.next=None

#creating the object Node with the data in it.
node1=Node(10)
node2=Node(7)
node3=Node(8)
node4=Node(11)

#linking the nodes.
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

#printing the link-list manually. 
print(node1.data,end=" ->")
print(node1.next.data,end=" ->")
print(node1.next.next.data,end=" ->")
print(node1.next.next.next.data)


#This is not efficient ,creating the node one by one ,than assigning the 
#address one by one and printing one by one is not efficient for large scale.
#this only show the demonstration .