#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      adsmith
#
# Created:     20/09/2024
# Copyright:   (c) adsmith 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice"))
        if user == 1:
            menuItemOne()
        if user == 2:
            menuItemTwo()
        if user == 3:
            menuItemThree()
        if user == 4:
            menuItemFour()
        if user == 5:
            menuItemFive()
        if user == 6:
            menuItemSix()
        if user == 7:
            menuItemSeven()
        if user == 8:
            print("thank you for using the menu")


def printMenu():
    print("1. Item one")
    print("2. Item two")
    print("3. Item three")
    print("4. Item four")
    print("5. Item five")
    print("6. Item six")
    print("7. Item seven")
    print("8. exit")

def menuItemOne():
    mylist = [1,2,3,4,5]
    print(mylist)
    mylist.append(int(input("Type a number to add to the list: ")))
    print(mylist)
def menuItemTwo():
    print("This is Menu Item 2")
def menuItemThree():
    print("This is Menu Item 3")
def menuItemFour():
    print("This is Menu Item 4")
def menuItemFive():
    print("This is Menu Item 5")
def menuItemSix():
    print("This is Menu Item 6")
def menuItemSeven():
    print("This is Menu Item 7")

def main():
    menu()

if __name__ == '__main__':
    main()
