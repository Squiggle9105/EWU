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
import turtle

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
    print("This is Menu Item 1")
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

def menuItemOne():
    bobjr = turtle.Turtle()
    width = 2.544
    height = 3.55
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = float(input("enter width"))
    height = float(input("enter height"))
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = 5
    height = 2
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = float(input("enter width again"))
    height = float(input("enter height again"))
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = 10
    height = 10
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)
    width = float(input("enter width AGAIN AGAIN"))
    height = float(input("enter height AGAIN AGAIN"))
    for i in range(2):
        bobjr.forward(width)
        bobjr.left(90)
        bobjr.forward(height)
        bobjr.left(90)

def printrectangle(height,width):
    
        bobjr = turtle.Turtle()
        perimeter= 12.188
        area= 9.031
        for i in range(2):
            bobjr.forward(width)
            bobjr.left(90)
            bobjr.forward(height)
            bobjr.left(90)
        
def menuItemTwo():
        bobjr = turtle.Turtle()
        printrectangle(3.55,2.544)
        uirectangle()
def uirectangle():
        height=float(input("enter height"))
        width=float(input("enter width"))
        printrectangle(height,width)
        
def evaluate():
    holeNum=str(input("what hole are you on?"))
    parValue=int(input("What is the value of par?"))
    strokes=int(input("How many strokes did you need to complete the hole?"))
    score= strokes-parValue
    scoreSlang=0
    special=0
    if score == 0:
        scoreSlang = "even par"
    elif score == 1:
        scoreSlang = "Bogey"
    elif score == 2:
        scoreSlang = "Double Bogey"
    elif score == 3:
        scoreSlang = "Triple Bogey"
    elif score == 4:
        scoreSlang = "4 over par"
    elif score == 5:
        scoreSlang = "5 over par"
    elif score == 6:
        scoreSlang = "6 over par"
    elif score == 7:
        scoreSlang = "7 over par"
    elif score == 8:
        scoreSlang = "8 over par"
    elif score == -1:
        scoreSlang = "Birdie"
    elif score == -2:
        scoreSlang = "Eagle"
    elif score == -3:
        scoreSlang = "Albatross"
    elif score == -4:
        scoreSlang == "Condor"
    elif score == -5:
        scoreSlang == "Ostrich"
    else:
        scoreSlang = "I don't know"
    if strokes ==1:
        special="with a Hole in One!"
    elif strokes ==4:
        special="with a Sailboat."
    elif strokes ==8:
        special="with a Snowman."
    elif strokes ==10:
        special ="with a Bo Derek."
    else:
        special= "."
    if strokes == parValue*2:
        scoreSlang = "Beagle"
    print("On hole "+ holeNum +" a par " + str(parValue) + " you shot a " + scoreSlang + " " + special)

    def menuItemFour():
        startnum=(int(input(("Starting number":))
        endnum=(int(input(("Ending number":))
        for i in range(Startnum,endnum))
        for number in range
    


    
def menuItemThree():
    evaluate()
    
        

if __name__ == '__main__':
    main()
