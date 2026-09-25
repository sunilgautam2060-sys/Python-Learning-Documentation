

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
         self.traversal()
         return

        else:

         previous = None
         current = self.head
         count = 1
         

         while current != None and count<position:

             previous = current
             current = current.next
             count += 1

        if count==position:
           previous.next = new_node
           new_node.next = current
           self.traversal()
           return

        else:
            print("The Position does not exist")
            self.traversal()
            return


    def remove(self,data):
       temp=self.head

       if temp is None:
          print("Linked_List is empty")
          return

       if temp.data==data :
           self.head=temp.next
           return self.traversal()
        
       while temp.next!=None:

           if temp.next.data==data:
               break

           temp=temp.next

       temp.next=temp.next.next   

       print("The Linked List after removing : ")    
       return self.traversal() 
           

        
    def delete(self,position):
     count=1

     if self.head == None:
        print("Linked-List is Empty")
        return

     elif position == 1:
        self.head = self.head.next
        self.traversal()
        return

     else:
        previous=None
        current=self.head
        while current!=None :
           
           if count==position:
              break

           previous=current
           current=current.next
           count+=1

        else:
           print("The position does not exist ")
           return
        
        previous.next=current.next
        self.traversal()
        return
         

sll=singly_linked_list()#making the object named:sll , of class singly_linked_list.
sll.append(4)           
sll.append(7)
sll.append(14)
sll.append(22)
sll.insert(17,3)


