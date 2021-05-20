import random


def run():
    random_number = random.randint(1, 100)
    player_number = int(input("Introduce a number between 1 and 100: "))
    while player_number != random_number:
        if player_number < random_number:
            print(f"Your number was: {player_number}. Choose a bigger number")
            player_number= int(input("Choose another number: "))
        else:
            print(f"Your number was: {player_number}. Choose a smaller number")
            player_number= int(input("Choose another number: "))
    print(f"Congratulations, your win! the number was: {random_number}")
    

if __name__ == '__main__':
    run()