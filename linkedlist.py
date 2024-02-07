#Implementing using classes
class Node():
    def __init__(self, given_data):
        """Constructor method"""
        self.data = given_data
        self.next = None


class LinkedList():
    def __init__(self):
        """Constructor method"""
        self.head = None

#Instantiaite an empty linked list object
my_list = LinkedList()




#Traversing using classes
class Node():

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next


class LinkedList():
    
    def traverse(self):
        #Set the current node as the head
        current = self.head

        #Repeat until there are no more linked nodes
        while current is not None:
            print(current.get_data())
            current = current.get_next()




#Adding a new node to an unordered list
class LinkedList():

    def insert_at_front(self, data):

        #Create a new node
        new_node = Node(data)

        #check if the node exists
        if self.head is None:
            self.head = new_node
        else:
            #Update the pointers so the new node is the head
            new_node.set_next(self.head)
            self.head = new_node



#Adding a new node to an ordered list
class LinkedList():

    def insert_in_order(self, data):
        """Insert a node into the correct position in an ordered list"""
        
        #Create a new node
        new_node = Node(data)

        #Start at the head of the list
        current = self.head

        #Check if there are no nodes in the list
        if current is None:
            self.head = new_node

        #Check if the new node is before the head data
        elif new_node.get_data() < current.get_data():
            #Set the new node as the head of the list
            new_node.set_next(self.head)
            self.head = new_node

        #Otherwise find where the new node should be positioned
        else:
            #Repeat until the point of insertion is found
            while (current.get_next() is not None and current.get_next().get_data() < new_node.get_data()):
                #Get the next node
                current = current.get_next()

            #Update the pointers of the new and current nodes
            new_node.set_next(current.get_next())
            current.set_next(new_node)




#Deleting a node
class LinkedList():


    def delete(self, data):

        #Start at the head of the list
        current = self.head

        #Check if the head node is to be deleted
        if current.get_data() == data:
            #Update the head pointer
            self.head = current.get_next()
        else:
            #Repeat until the node has been found
            while current.get_next().get_data() != data:
                #Change the current node to be the next node
                current = current.get_next()

            #Set the pointer to be the next node's pointer
            current.set_next(current.get_next().get_next())



