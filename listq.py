# initialise variables to manage the list
head = 0
# used to support accessing the array elements to make it more readable
data = 0
pointer = 1
# used to track size of list to check if empty or fulll
maxCounter=4
linkedlist = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Sharon", None],
    ["Roberto", 1],
    [None, None],
    [None, None]
]
# set the size of the list to begin
maxSize = len(linkedlist)


def traverseList():
    global head, data, pointer, linkedlist
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

def addToEndOfList():
    '''
        check that there is free space in the array
        traverse the list to find the end of the list (this will be the element whose next_position index pointer has the value Null)
        store the new item in the free space found; this item is now the end of the list
        adjust the next_position index pointer of the element that was previously last in the list
    '''
    global head, data, pointer, linkedlist
    #  check that there is free space in the array
    if maxCounter == maxSize:
        print("Error: List is full")
    else:
        #traverse the list to find the end of the list (this will be the element whose next_position index pointer has the value Null)
        #store the new item in the free space found; this item is now the end of the list
        #adjust the next_position index pointer of the element that was previously last in the list
        current = head
        while current != None:
            print(linkedlist[current][data])
            current = (linkedlist[current][pointer])
        
  
addToEndOfList()
