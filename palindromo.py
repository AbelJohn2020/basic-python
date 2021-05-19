def palindrom(text):
    text = text.replace(' ', '')
    text = text.lower()
    palindrom_text = text[::-1]

    if text == palindrom_text:
        return True
    else:
        return False

def run():
    text = input("introduce your text: ")
    is_palindrom = palindrom(text)
    if is_palindrom == True:
        print(f"'{text}' Es un palindromo")
    else:
        print(f"'{text}' No es un palindromo")

if __name__ == '__main__':
    run()