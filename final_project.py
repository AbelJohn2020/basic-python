import random

def password_generator():
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minuscule = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simbols = ['!', '"', '·', '$', '%', '&', '/', '(', ')', '=', '|', '@', '#', '~', '€', '¬']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    characters = capital + minuscule + simbols + numbers

    password = []

    for i in range(15):
        random_charapter = random.choice(characters)
        password.append(random_charapter)
    password = ''.join(password)
    return password


def run():
    password = password_generator()
    print(f"Your new password is: {password}")


if __name__ == '__main__':
    run()