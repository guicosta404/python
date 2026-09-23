# Retangulo com FOR

largura = 5
altura = 3
for i in range(altura):
    for j in range(largura):
        print("*", end=" ")
    print()

# Triangulo com FOR
altura = 5

for i in range(altura):
    espacos = altura - i - 1
    estrelas = 2 * i + 1
    print(" " * espacos + "*" * estrelas)