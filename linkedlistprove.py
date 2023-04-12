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

    def remove(self, value):
            """
            Remove the first node that contains 'value'.
            """
            # Start at the beginning (the head)
            current = self.head
            done = False

            # Loop until we have reached the end (None)
            while not done:
            
                if current is not None:
                    if current.data == value:
                        current.next.prev = current.prev
                        if current == self.head:
                            self.head.next.prev = None  # Disconnect the second node from the first node
                            self.head = self.head.next  # Update the head to point to the second node
                        else:
                            current.prev.next = current.next
                        done = True

                    if current.next == self.tail:
                        if self.tail.data == value:
                            self.tail.prev.next = None  #Disconnect the second from last node from the last
                            self.tail = self.tail.prev  #Update the tail to point to the previous node
                            done = True
                        else:
                            done = True

                    # Follow the pointer to the next node
                    current = current.next
                else:
                    done = True
