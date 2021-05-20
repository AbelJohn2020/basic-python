def is_prim(number):
    contador = 0
    for i in range(1, number+1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    number=int(input("Insert a number: "))
    if is_prim(number):
        print(f"{number} is prime number")
    else:
        print(f"{number} is not a prime number")

if __name__ == '__main__':
    run()