def update_inventory(inventory, name, quantity):
    if name in inventory:
        if quantity <= inventory[name]:
            inventory[name] -= quantity
            return True
        else:
            return False
    else:
        return False

inventory = {}

print("Welcome to the alcohol bar management program!\n")

while True:
    print("Choose an option:\n1. Add bottles to the bar\n2. Remove a bottle from the bar\n3. Purchase a bottle from the bar\n4. Print the current inventory of the bar\n5. Quit the program")
    
    choice = int(input("\nEnter your choice: "))

#Add bottles to the bar

    if choice == 1:
        num_bottles = int(input("\nEnter the number of bottles you want to add: "))
        
        for i in range(num_bottles):
            name = input(f"\nEnter the name of bottle #{i+1}: ")
            quantity = int(input("Enter the quantity of the bottle: "))

            if quantity < 0:
                print("\nInvalid quantity. Please enter a non-negative value.\n")
                continue
            
            if name in inventory:
                inventory[name] += quantity
            else:
                inventory[name] = quantity
                
            print(f"\n{name} has been added to the bar.\n")

#Remove a bottle from the bar  

    elif choice == 2:
        name = input("\nEnter the name of the bottle you want to remove: ")

        if name in inventory:
            quantity = int(input("Enter the quantity you want to remove: "))

            if inventory[name] >= quantity:
                inventory[name] -= quantity
            print(f"\n{name} has been removed from the bar.\n")
        else:
            print(f"\n{name} is not in the bar.\n")

#Purchase a bottle from the bar  

    elif choice == 3:
        name = input("\nEnter the name of the bottle you want to purchase: ")
        quantity = int(input("Enter the quantity you want to purchase: "))

        if update_inventory(inventory, name, quantity):
            print(f"\nYou have purchased {quantity} bottles of {name}.")
        else:
            print(f"\n{name} is either not in the inventory or the quantity you entered is greater than the available quantity.")
        
#Print the current inventory of the bar
       
    elif choice == 4:
        print("\nCurrent inventory:")
        for name, quantity in inventory.items():
            print(f"- {name}: {quantity}")
        print()
        
    elif choice == 5:
        print("\nThank you for using the alcohol bar management program!")
        break
        
    else:
        print("\nInvalid choice. Please try again.\n")
