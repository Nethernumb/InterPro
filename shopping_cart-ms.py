# CISW 126
# Objects Lab
# 
#Mason Shaw


# Instantiate a class called item.
class Item():
    def __init__(self, desc, price, amnt):
        self.desc = desc
        self.price = price
        self.amnt = amnt

    def getcost(self):
        return self.price * self.amnt
    
def itemnames():
    for items in cart:
        print(items.desc)

def itemcosts():
    total = 0
    for stuff in cart:
        total += stuff.getcost()
    print(f"Your total is ${total}")

    # In your class constructor:
    # Create an attribute called description
    # - Description will hold a description of a given item.

    # Create an attribute called price
    # - Price will have the price for one individual item.

    # Create an attribute called quantity
    # - Quantity is the number of this item to be purchased.

    # Create a method called cost
    # -  When called, cost will calculate the cost of
    #    purchasing *quantity* items at *price* per item
    #    and return that value.


if __name__ == "__main__":
   
    # First: Explain what if __name__ == "__main__ " is doing.
    # I have seen this more than once when watching videos mainly, or looking at other forums or so but I still have no idea what this is. 

    # Next: Make an empty list called 'cart'.
    cart = []

    # Then: Create a new object from the item class you created above.
    # Give it a description, quantity and price. Whatever you like.
    # Add it to the list. HINT: You can use .append() to add the objects you make to a list

item1 = Item("Milk", 3, 2)
item2 = Item("19 Dollar Fortnite Card", 19, 5)
item3 = Item("Covert Compantion(TM) Lockpicking Kit", 90, 1) 
item4 = Item("Corsair Vengeance 16BG DDR5 RAM (2x8)", 64, 2)
#additem = Item(input"What would you like to add? > "), input("What is its price? > "), input("How many? > "), input("What is that total cost? > ")

cart.append(item1)
cart.append(item2)
cart.append(item3)
cart.append(item4)

    # At this point you should have a list with four class objects
    # in it.
    # Write a loop that loops over the list, print out each of the
    # item descriptions and costs, and then print the total of
    # all of the items in the list.

def listloop():
    print(f"Hello!")
    while True:
        print("1 : Show List Items")
        print("2 : Add up Total")
        print("Exit")
        choice = input("Choose an option: (1-2) > ")

        if choice == "1":
            itemnames()

        if choice == "2":
           itemcosts()

        if choice.lower() == "exit":
            exit()

listloop()
