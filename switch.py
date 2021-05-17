print("**** You can only change your money to dollars ****")
options = """
    Welcome to change home:

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
    money = int(input("How much money do your want to change? "))
    money = money/3.74
    money = round(money, 2)
    print("Your money is: ",money,"dollars")

elif country_money == "Chilean pesos":
    money = int(input("How much money do your want to change? "))
    money = money/712.38
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Mexican pesos":
    money = int(input("How much money do your want to change? "))
    money = money/20.32
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Uruguayan pesos":
    money = int(input("How much money do your want to change? "))
    money = money/44.88
    money = round(money, 2)
    print("Your money is: ",money,"dollars")

elif country_money == "Argentine pesos":
    money = int(input("How much money do your want to change? "))
    money = money/95.74
    money = round(money, 2)
    print("Your money is: ",money,"dollars")  

elif country_money == "Colombian pesos":
    money = int(input("How much money do your want to change? "))
    money = money/3789.1
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Bolivian":
    money = int(input("How much money do your want to change? "))
    money = money/7.02
    money = round(money, 2)
    print("Your money is: ",money,"dollars")

elif country_money == "Brazilian real":
    money = int(input("How much money do your want to change? "))
    money = money/5.38
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

elif country_money == "Guarani":
    money = int(input("How much money do your want to change? "))
    money = money/6790.34
    money = round(money, 2)
    print("Your money is: ",money,"dollars") 

else:
    print("Invalid option, try again")
    