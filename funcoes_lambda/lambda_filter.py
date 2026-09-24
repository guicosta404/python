# Filter de números

numeros = [1,2,3,4,5,6,7,8,9,10]

lista_pares = list(filter(lambda x : x % 2 == 0, numeros))

print(lista_pares)

#Filter de strings

nomes = ["Alice", "Bob", "Ana", "Charlie", "Alex", "Tom"]

nomes_a = list(filter(lambda nome : nome[0] == "A", nomes))

print(nomes_a)

"""Dada uma lista de nomes, filtre-a para obter apenas os nomes 
que começam com a letra "A".
"""

# Lista original de nomes
nomes = ["Alice", "Bob", "Anna", "Charlie", "Alex", "Tom", "Alice"]

nomes_Alice = list(filter(lambda nome : nome == "Alice", nomes))
print(nomes_Alice)