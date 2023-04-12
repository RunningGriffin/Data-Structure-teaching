# Stack

When you think about folding your clothes, you typically start of the stack with the first clothing article you fold. As you continue folding your clothes, you keep stacking on top of the previously folded item. Once organized this way, you navagate through the stack by taking the top item off before you can retrieve the next.

This is how a stack in coding works. This idea is that whatever was added last to a list is the first one to be removed. This is vis versa for the first item added to the stack as you have to make your way to that bottom item from the top.

**How can this form of data structure be useful?**

- This can be used for organization by making it easy to undo the last added array items in an 0(1) time complexity since we are simpliy just removing the last element. 
    - This eliminates the need to iterate through all members of the array to find what need to be deleted.

- Recursion utalizes this process to manage the flow of recalling its own function. 
    - The first instance of the function call (which will return the end value) needs to be the last one to perform its sequence as its answer depends on other calls to itself. 

## Example 1

```python
import json

def grant_username(username_attempt):
    if check_user(username_attempt):
        return f"{username_attempt} is avalible"
    else: 
        return "Username already in use"
    
def check_user(username_attempt):
    f = open("data.json")
    data = json.load(f)

    if username_attempt in data:
        return False
    else:
        return True

username_attempt = input("What username would you like for your account?")
print(grant_username(username_attempt))
```

Here we have an example that uses the stack to process data procedurally. After we attempt to check for an avalible username we would like to use, we are sent to the grant username function. This function however has another function call in the if statment that will determine how the rest of the function will proform. This is like us placing the grant username function on the bottom of the stack and then placing check user function on top of it. Therefore we have to complete the check user function to remove it off the stack before going back and completing what was on the stack below it. 

If coding did not use a stack and instead did first in first out then we would not be able to complete this varification save it be in the same function which would make each function extrenuous.

## Example 2
```python
shopping_list = []
done = False

while not done:
    choice = input("ADD another item or REMOVE last input? (type DONE if finished)").lower()
    
    if choice == "add":
        item = input("what item would you like to add?")
        shopping_list.append(item)

    elif choice == "remove":
        shopping_list.pop()

    elif choice == "done":
        done = True
```

This is a simple organizing tool that can hold items in an array using a stack to be able to keep track of the last item added. Since we order the items in this data structure, we can easily remove the last item added.

This can be really useful as you will see in this following activity.

## Activity

Here is a story to set the stage:

You are a tour bus driver that sells tickets ahead of time so that passengers are able to reserve their spot on your bus. Unfortunatly you keep accidently overselling more tickets than seats avalible on your bus. Write a program where you can add new ticket buyers with their names to a list. Continue this process for as many tickets as you sell, then once you are ready to take the trip, if you have oversold tickets again, remove the ticket buyers that bought them most recently so that those that have resevered their spots FIRST are the ones that will take the seats.

- [Solution](busdriver.py)