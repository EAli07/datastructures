head = 0
data = 0
pointer = 1
linkedlist = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Sharon", None],
    ["Roberto", 1],
    [None, None],
    [None, None]
]

#check if list is empty
if (linkedlist[head]) == None:
    print("List empty)")
else:
    current = head
    while current != None:
        #start at the head
        #print data of current node
        print(linkedlist[current][data])
        #go to pointer of current node
        current = (linkedlist[current][pointer])
        #if the head is none, list is empty
        if current == None:
            #if the pointer of the current node is none, then the list is finished
            print("List is finished")



#traversed the list now need to move onto adding a new node
#potentially putting new node in order