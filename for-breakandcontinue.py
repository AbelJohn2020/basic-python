def run():
    # for contador in range(1001):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(101):
    #     print(i)
    #     if i == 50:
    #         break

    phrase = input("Write a phrase: ")
    for letter in phrase:
        if letter == 'o':
            continue
        print(letter)

if __name__ == '__main__':
    run()