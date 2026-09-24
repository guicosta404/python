# Função lambda para dobrar um número

dobrar_lambda = lambda n: n * 2

print(dobrar_lambda(2))

# Função para classificar números

classificar_lambda = lambda n: "Negativo" if n < 0 else("Zero" if n == 0 else "Positivo")

print(classificar_lambda(20))

# função lambda 
# para especificar que queremos ordenar as tuplas pela idade (índice 1).

pessoas = [("João", 35), ("Maria", 25), ("Pedro", 40)]

# Usando lambda com sorted
pessoas_ordenadas = sorted(pessoas, key=lambda x : x[1])
print(pessoas_ordenadas)