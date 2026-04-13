shelf = ['banana','apple']

#funções do programa
def add_item(inventory):
    if len(inventory) < 7:
        item = input("type the item's name to add: ")
        inventory.append(item)
        print(f"{item} added to Shelf")
    else:
        print("Shelf is full! Cannot add item")


def remove_item(inventory):
    item = input("Type the item's name to remove: ")
    if item in inventory:
        inventory.remove(item)
        print(f"{item} removed!")
    else:
        print(f"{item} not found")

#Inicio do programa
print("-----Wellcome to Smart Inventory-----")
print(f"Current shelf: {shelf}")
while True:
    choice = input("choose an option:\n add item(A) \n remove item(R) \n exit(E):" ).upper()
    if choice == "A":
        add_item(shelf)
    elif choice == "R":
        remove_item(shelf)
    elif choice == "E":
        break
    else: 
       print("option nof found, please type 'a' 'r' or 'e'")