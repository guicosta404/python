# Função lambda com map 

# Elevando cada número de uma lista ao quadrado

numeros =[1,2,3,4,5]

numeros_quad = list(map(lambda num : num ** 2, numeros))

# Map e lambda com strings

# Retornando o comprimento de cada palavra

palavras = ["Maça","Banana", "Laranja"]

comprimentos = list(map(lambda palavra : len(palavra), palavras))
print(comprimentos)

#######

nums = [2, 5, 8, 10, 12, 15, 18, 20, 23, 25, 28]

impares = list(filter(lambda x : x % 2 != 0, nums))

quadrado_impares = list(map(lambda x : x**2, impares))

print(impares)
print(quadrado_impares)