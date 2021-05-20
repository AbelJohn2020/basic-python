################ DICTIONARY ##########################

def run():
    my_dictionary = {
        # key: value,
        'Aries': 'Shion',
        'Tauro': 'Aldebaran',
        'Geminis': 'Deuteros and Aspros',
        'Cancer': 'Manigoldo',
        'Leo': 'Regulus',
    }

    # print(my_dictionary['Aries'])
    for knight in my_dictionary.values():
        print(knight)
    
    for house, knight in my_dictionary.items():
        print(knight+' of '+house)


if __name__ == '__main__':
    run()