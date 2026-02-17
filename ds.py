# Super simple List program for beginners
mylist = []

while True:
    print("\n--- My List ---")
    print("Current list:", mylist)
    print("\nWhat do you want to do?")
    print("1 = Add item")
    print("2 = Remove item")
    print("3 = Show list")
    print("4 = Clear list")
    print("5 = Exit")

    choice = input("Enter number (1-5): ")

    if choice == "1":
        item = input("What do you want to add? ")
        mylist.append(item)
        print(item, "was added!")

    elif choice == "2":
        if mylist == []:
            print("List is already empty!")
        else:
            print("Items:", mylist)
            what = input("What do you want to remove? ")
            if what in mylist:
                mylist.remove(what)
                print(what, "was removed!")
            else:
                print("I didn't find", what)

    elif choice == "3":
        if mylist == []:
            print("List is empty")
        else:
            print("Your list has", len(mylist), "items")

    elif choice == "4":
        mylist = []
        print("List is now empty!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3, 4 or 5")