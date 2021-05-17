money = int(input("How much money is your salary? "))
no_disccount = str(money);
if money >= 1000:
    # pass              #this is when you write code later
    your_money_is = money - money*0.015
    your_money_is = str(your_money_is)
    print("You have " + your_money_is + " in your target")
else:
    print("You have " + no_disccount + " in your target")