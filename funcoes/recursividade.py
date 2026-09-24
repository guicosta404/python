# Função que chama ela mesma

# Contar regressivamente

def regres(n):
    if n > 0:
        print(n, end="-" if n != 1 else "\n")

        regres(n-1)

regres(5)

# Calculo de fatorial

def fat(n):
    if n == 0:
        return 1

    else:
        return n *fat(n-1)

print(fat(5))