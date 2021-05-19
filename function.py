# def print_message(name):
#     print('Special message: ')
#     print('Today is a wonderfull day, enjoy it and be happy, ' + name)

# print_message('mom and dad')

class choose_an_option:
    option = input("""
        Welcome to the "Casa de Cambio" where you can change your money to US dollars

        1.- Nuevo sol.
        2.- Chilean pesos.
        3.- Mexican pesos.
        4.- Uruguayan pesos
        5.- Argentine pesos.
        6.- Colombian pesos.
        7.- Bolivian.
        8.- Brazilian real.
        9.- Guarani.

        Choose an option, please: 
    """)
    option = option.capitalize()

def client_money(change):
    your_money = round(float(input("How much money do your want to change? ")), 2)
    change = round(float(change), 2)
    your_money = your_money/change
    money = round(your_money, 2)
    print("Your money is: ",money,"dollars")

def change_money():
    if choose_an_option.option == 'Nuevo sol' or choose_an_option.option == '1':
        client_money(3.74)

    elif choose_an_option.option == 'Chilean pesos' or choose_an_option.option == '2':
        client_money(712.38)

    elif choose_an_option.option == 'Mexican pesos' or choose_an_option.option == '3':
        client_money(20.32)
    
    elif choose_an_option.option == 'Uruguayan pesos' or choose_an_option.option == '4':
        client_money(44.88)

    elif choose_an_option.option == 'Argentine pesos' or choose_an_option.option == '5':
        client_money(95.74)

    elif choose_an_option.option == 'Colombian pesos' or choose_an_option.option == '6':
        client_money(3789.1)

    elif choose_an_option.option == 'Bolivian' or choose_an_option.option == '7':
        client_money(7.02)
    
    elif choose_an_option.option == 'Brazilian real' or choose_an_option.option == '8':
        client_money(5.38)

    elif choose_an_option.option == 'Guarani' or choose_an_option.option == '9':
        client_money(6790.34)
        
    else :
        print("Invalid option, try again")

change_money()