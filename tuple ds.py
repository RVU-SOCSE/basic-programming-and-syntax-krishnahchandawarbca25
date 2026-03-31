mytuple = ()

while True:
    print("----My Tuple----")
    print("current tuple:", mytuple)
    print("1= add item")
    print("1= remove item")
    print("3= Show List")
    print("4= Clear tuple")
    print("5= Exit")

    choice = input("Enter a number (1-5)")

    if choice == "1":
        item = input("What do you want to add?")
        mylist.append(item)
        print(item, "was added!")

    elif choice == "2":
            if mytuple == ():
                print("List is already empty!")
            else:
            print("Items:", mytuple)
            what = input("What do you want to remove? ")
            if what in mytuple:
                mytuple.remove(what)
                print(what, "was removed!")
            else:
                print("I didn't find", what)

    elif choice == "3":
        if mytuple == ():
            print("List is empty")
        else:
            print("Your list has", len(mytuple), "items")

    elif choice == "4":
        mytuple = ()
        print("List is now empty!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3, 4 or 5")
    
      
