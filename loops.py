def run():
    i=1
    numero=2
    limite=100
    while (i<=limite):
        print(f"2 elevado a {i} es igual a {numero**i}")
        i += 1
        numero**i

if __name__ == '__main__':    #entri point
    run()