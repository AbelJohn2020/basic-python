# Type money's cahnge

dollar = 3.75
soles = input("How much soles do your want to change to dollars? ")
soles = float(soles)        #decimal
dollars_total = soles/dollar
dollars_total = round(dollars_total, 2) #dollar, number of decimals that you want
dollars_total = str(dollars_total) #string
print("Your have: "+dollars_total+" dollars")


dollar = 3.75
soles = input("How much soles do your want to change to dollars? ")
soles = float(soles)        #decimal
dollars_total = soles*dollar
dollars_total = round(dollars_total, 2) #dollar, number of decimals that you want
dollars_total = str(dollars_total) #string
print("Your have: "+dollars_total+" soles")
