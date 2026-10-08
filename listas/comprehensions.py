# List comprehension com mais de um for
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]

print(lista)

# Comprehension dentro de list comprehension
nome = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]

print(nome)