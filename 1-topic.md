# Stack

When you think about folding your clothes, you typically start of the stack with the first clothing article you fold. As you continue folding your clothes, you keep stacking on top of the previously folded item. Once organized this way, you navagate through the stack by taking the top item off before you can retrieve the next.

This is how a stack in coding works. This idea is that whatever was added last to a list is the first one to be removed. This is vis versa for the first item added to the stack as you have to make your way to that bottom item from the top.

**How can this form of data structure be useful?**

- This can be used for organization by making it easy to undo the last added array items in an 0(1) time complexity since we are simpliy just removing the last element. 
    - This eliminates the need to iterate through all members of the array to find what need to be deleted.

- Recursion utalizes this process to manage the flow of recalling its own function. 
    - The first instance of the function call (which will return the end value) needs to be the last one to perform its sequence as its answer depends on other calls to itself. 

## Example 1


