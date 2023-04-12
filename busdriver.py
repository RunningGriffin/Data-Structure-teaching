def add_buyer():
    done = False
    ticket_list = []

    while not done:
        name = input("Who just bought a ticket? (enter done when ready to go)").lower()
        if name != "done":
            ticket_list.append(name) #Adds new name to the list
        else:
            list_to_go(check_list(ticket_list))
            
def check_list(ticket_list):
    if len(ticket_list) <= 30: #Assume that you have 30 seats on your bus
        return ticket_list
    else:
        overflow = len(ticket_list) - 30 #Find out how many seats you sold over your cap (30)
        ticket_list.pop(overflow) #Remove the excess over 30 from the top of the stack moving backwards
        return ticket_list

def list_to_go(ticket_list):
    print(f"The list of buyers going on the bus are {ticket_list}") #Prints at most 30 people


add_buyer()