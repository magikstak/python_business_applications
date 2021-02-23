print ("Change Calclator")
print()

choice = "y"
while choice.lower() == "y":
    Quarter = 25
    Dime = 10
    Nickel = 5
    Penny = 1

#get input from user
    while True:
        moneygiven = int(input("Enter number of cents (0-99):"))
        if moneygiven > 0 and moneygiven <=100:
            break
        else:
            continue

    moneygiven = int(float(moneygiven))
    moneyback = moneygiven 

    qmb = moneyback // Quarter
    partialtotal = moneyback - (qmb * Quarter) 
    dmb = partialtotal // Dime
    dpartialtotal = partialtotal - (dmb * Dime)
    nmb = dpartialtotal // Nickel
    npartialtotal = dpartialtotal - (nmb * Nickel)
    pmb = npartialtotal // Penny
    ppartialtotal = npartialtotal - (pmb * Penny)

    print("Quarters",qmb) 
    print("Dimes", dmb)
    print("Nickels", nmb)
    print("Pennies",pmb) 

    # see if the user wants to continue
    choice =input("Continue (y/n)? ")
    print()

print("Bye!")
