

#class to make nodes.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None


#This will makke Singly Linked List.
class singly_linked_list:

    #By default there will be no linked-list so self.head will be None.
    #This is constructor.
    def __init__(self):
        self.head=None

    #append function definition.
    def append(self,data):

        #calling node function to make node of data to append.
        new_node=node(data)


        #two scenario while append.
        #scenario 1: if link list is empty.
        #scenario 2: if link list is not empty there is already existing linklist. 

        if self.head==None:
            self.head=new_node

        else:
              current=self.head
              #traversing.
              while current.next!=None:
                  current=current.next
              
              current.next=new_node


    #traversal function definition.               
    def traversal(self):

        #edge-case:if there is no existing nodes.
        if self.head is None:
            print("Singly-Link-List is empty")

        else:
            current=self.head

            while current!=None:
                print(current.data,end=" ")
                current=current.next


    #inserting element in Linked List.
    #here data =data to insert in linklist, position=in which node position in linklist to insert the data.
    
def insert(self, data, position):

    # Creating node
    new_node = node(data)

    if position == 1:

        new_node.next = self.head
        self.head = new_node

    else:

        previous = None
        current = self.head
        count = 0
        found = False

        while current != None:

            if count == position - 1:
                found = True
                break

            count += 1
            previous = current
            current = current.next

        if found == True:
            previous.next = new_node
            new_node.next = current

        else:
            print("The Position does not exist")




    def remove(self,data):
       temp=self.head

       #it means if there need to be more than 1 node for this logic.
       if temp.next is not None:
         
         if temp.data==data:
             self.head=temp.next
             return
            
         else:
            found=False
            previous=None

            while temp != None:

              if temp.data==data:  
                 found=True
                 break

              previous=temp
              temp=temp.next

              
            if found==True:
                previous.next=temp.next
                return

            else:
                print("Node not found ")


    def delete(self,position):


     if self.head == None:
        print("Linked-List is Empty")
        return

     elif position == 1:
        self.head = self.head.next
        return

     else:
        found = False
        current = self.head
        previous = None
        count = 1

        while current != None:

            if count == position:
                found = True
                break

            previous = current
            current = current.next
            count += 1

        if found == True:
            previous.next = current.next

        else:
            print("The Position does not exist")


                        

sll=singly_linked_list()#making the object named:sll , of class singly_linked_list.
sll.append(4)           
sll.append(7)
sll.append(9)
sll.delete(4)
sll.traversal()

