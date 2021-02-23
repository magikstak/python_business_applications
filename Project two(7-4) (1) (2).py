#!/usr/bin/env python3

import csv
FILENAME = "monthly_sales.csv"

# a file in the current directory
def write_sales(sales):
        with open (FILENAME, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(sales)

def read_sales():
    sales = []
    with open (FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            sales.append(row)
        return sales

def view_monthly_sales(sales):
    counter = 0
    for row in sales: 
        counter += 1
        print(str(counter) + ". " + row[0] + " – " + str(row [1]))
    print()
   
def view_yearly_summary(sales):
    total=0
    for row in sales:
        amount = int(row[1])
        total += amount

    #get count
    count = len(sales)

    #calculate average
    average = total/count
    average = round(average,2)
    
    #format and display the menu
    print ("Yearly total:    ", total)
    print("Monthly average:  ", average)
    print()
        
    
def edit(sales):
    ThreeLetterMonth = input("Three-letter Month:     ")
    while True:
    
        salenumber= int(input("Sales Amount:      "))
        if salenumber < 0:
                print("Salenumber must be greater than 0.")
        else:
                break
    amount = (salenumber)
    
    for s in sales:
        if s[0] == ThreeLetterMonth:
                s[1] = amount

                write_sales(sales)
                print ("Sales amount for", s [0], "was modified.")
                print()           


def display_menu():
    print ("COMMAND MENU")
    print("monthly   – View monthly sales")
    print("yearly    – View yearly summary")
    print("edit      – Edit sales for a month")
    print("exit      – Exit program")

def main():
     # display a welcome message
     print("Monthly Sales program")
     print()
     sales= read_sales()
     display_menu()
     while True:
         command = input ("Command: ")
         if command == "monthly":
             view_monthly_sales(sales)
         elif command == "yearly": 
             view_yearly_summary(sales)
         elif command == "edit":
             edit (sales)
         elif command == "exit":
             break
         else:
                 print ("Not a valid command. Please try again.\n")
     print ("Bye!")

if __name__ == "__main__":
    main()


