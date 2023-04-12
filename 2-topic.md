# Linked Lists

Have you ever followed a list of instructions from a lego set, each page connects to the next as you flip through the instruction book. This instruction book would be like a linked list since each page is connected to a page after it and one before it. This data structure has most of its benefits in the ability to add items into the middle with a lot more ease.

Rather than needing to move the rest of the list down 1 more, we can simply remove the connections from one page (node) to the other and place our new node in between. Then we can simply reconnect the nodes to each side that were previously connected and connect them instead to the new node. 

This allows us to have a structure that does not need to worry about size and can always add a new node anywhere in the linked list in an O(1) time complexity. 

**How is this form of data Structure useful?**

- The size of this linked list will never effect new inserts. 
    - No matter how mnay links we have within the list, we can always add a new element without changing the time needed. It stays constant

## Example 1
```Python
class LinkedList:

    class Node:

    
        def __init__(self, data):
            '''
            Initialize what is required for a node to connect and what the 
            node holds in itself 
            '''
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize a 2 way linked list using a head of the list and a tail.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node as the head
        """
        new_node = LinkedList.Node(value)  
        
        # If the list is empty connect both head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty only self.head will be altered.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.prev = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def insert_tail(self, value):
        """
        Insert a new node as the tail of the linked list.
        """
        new_node = LinkedList.Node(value)
        # If the list is empty, then point both head and tail to the new node.
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.tail will be altered 
        else:
            new_node.prev = self.tail # Connect new node to the previous tail
            self.tail.next = new_node # Connect the previous tail to the new node
            self.tail = new_node      # Update the tail to point to the new node
```
This shows how a new head and tail would be added to the lisked list. When you make a new node class, you initiale it by telling it what the next node and the previous node are so that it connects to the other node objects. In python we need to utalize object oriented programming to make linked lists work but other coding languages make this process much easier.

## Example 2
```Python
def remove_head(self):
        """ 
        Remove the head from the linked list.
        """
        # If the list has only one item in it, set the head and tail of the list 
        # to None just as we initialized (as an empty list).
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # else make the next node the head and remove the connection to the previous head
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

def remove_tail(self):
        """
        Remove the last node of the linked list.
        """
        # If the list has only one item in it, set the head and tail of the list 
        # to None just as we initialized (as an empty list).
        if self.tail == self.head:
            self.tail = None
            self.head = None
        # else make the previous node the tail and remove the connection to the previous tail
        elif self.head is not None:
            self.tail.prev.next = None  #Disconnect the second from last node from the last
            self.tail = self.tail.prev  #Update the tail to point to the previous node
```

Here we can see the process needed to remove a head or a tail. We need to break off the connection that our Linked List has to these node objects, in doing so we effectivly remove the node as there is no other node that can point to it. This is like if you could point to your classmates to either side of you but then suddenly one of them leaves. You can no longer point to them and prove that they exist, so therefore they dont. You forget about how you could previously point to them.

## Activity
Using the above code as well as this function to add a new node after a set value.
```Python
    def insert_after_value(self, value, new_value):
            """
            Insert 'new_value' after the first occurance of 'value' in
            the linked list.
            """
            # look for the node that equals 'value'. Start at the head of the list.
            current = self.head
            while current is not None:
                if current.data == value:
                    # If the node equal to 'value' is at the end,
                    # then we can call insert_tail to add 'new_value' so we have
                    # something to connect to
                    if current == self.tail:
                        self.insert_tail(new_value)
                    # For any other location of 'value', need to create a 
                    # new node and reconenct the links to insert.
                    else:
                        new_node = LinkedList.Node(new_value)
                        new_node.prev = current       # Connect new node to the node containing 'value'
                        new_node.next = current.next  # Connect new node to the node after 'value'
                        current.next.prev = new_node  # Connect node after 'value' to the new node
                        current.next = new_node       # Connect the node containing 'value' to the new node
                    return # We can exit the function after we insert
                current = current.next # Go to the next node to search for 'value'
```
Find a way to remove a node of a certain value. Doing this you will need to change what the previous node and the next node are connected to. Use the insert_after_value function as a guide.

- [Soultion](linkedlistprove.py)