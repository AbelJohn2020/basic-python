print("**** You can only change your money to dollars ****")
options = """
    Welcome to "Casa de Cambio":

    1.- Nuevo sol.
    2.- Chilean pesos.
    3.- Mexican pesos.
    4.- Uruguayan pesos
    5.- Argentine pesos.
    6.- Colombian pesos.
    7.- Bolivian.
    8.- Brazilian real.
    9.- Guarani.

    Choose an option:
"""
# You can write """ """ when you want to write more than one string and you want to work with spaces or try to write in the next space

print(options)

country_money = input().capitalize()

if country_money == "Nuevo sol":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 3.74
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars")

elif country_money == "Chilean pesos":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 712.38
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Mexican pesos":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 20.32
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Uruguayan pesos":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 44.88
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars")

elif country_money == "Argentine pesos":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 95.74
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars")  

elif country_money == "Colombian pesos":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 3789.1
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Bolivian":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 7.02
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars")

elif country_money == "Brazilian real":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 5.38
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Guarani":
    money = round(float(input("How much money do your want to change? ")), 2)
    change = 6790.34
    money = money/change
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

else:
    print("Invalid option, try again")