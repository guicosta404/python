# Exemplo 1

quadrados_impares = [x**2 for x in range(10) if x % 2 != 0]
print(quadrados_impares)

# forma sem list comprehension

lista = []
for x in range (10):
    if x % 2 != 0:
        lista.append(x**2)

print(lista)        

# Exemplo 2
texto = "Hello World"
consoantes = [char for char in texto if char.lower() not in "aeiou"]

print(consoantes)

# Sem list comprehension
tradicional = []
for char in texto:
    if char not in "aeiou":
        tradicional.append(char)

print(tradicional)        

# Exemplo 3 - Fatorial

n = int(input("Digite um número: "))
fatorial = 1
for multiplicador in range(1,n+1):

    fatorial *= multiplicador

    print(f"{multiplicador}! =", end=" ")

    for i in range(multiplicador + 1):
        print(i, end = " ")

        if i != multiplicador:
            print("*", end = " ")

    print(" = ", fatorial)        
    

print(f"O fatorial de {n} é {fatorial}.")