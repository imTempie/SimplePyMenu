import time

def menu():
    print("[1] Option 1")
    print("[2] Option 2")
    print("[0] Exit")

menu()
option = int(input("Enter Your Option:  "))

while option != 0:
    if option == 1:
        #do option 1
        print("Option 1 Selected")
        pass
    elif option == 2:
        #do option 2
        print("Option 2 Selected")
        pass
    else:
        print("Invalid Option.")

    print()
    menu()
    option = int(input("Enter Your Option:  "))

print("Thanks for using this menu.")
time.sleep(2)
