"""
Exercício: Fábrica de Funções de Operações Matemáticas

Imagine que você está construindo uma calculadora. Porém, ao invés de 
implementar cada operação matemática (soma, subtração, multiplicação e divisão) 
diretamente, você decide criar uma "fábrica de funções". Esta fábrica, quando fornecida 
com o nome de uma operação, deve retornar uma função que realiza a operação desejada.

Instruções:

    - Escreva uma função chamada fábrica_de_operacoes que aceite uma 
    string: 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.
    
    - Dependendo do argumento fornecido, sua função deve retornar uma das 
    operações matemáticas. Por exemplo, se o argumento for 'soma', a função 
    retornada deve ser capaz de somar dois números.
    
    - Se a operação não for reconhecida, retorne uma função que 
    imprima "Operação não suportada.".
    
    
Desafio Extra:
Adapte a fábrica para aceitar operações com 
mais de dois números. Por exemplo, a operação de soma deve 
ser capaz de somar três, quatro ou mais números de uma só vez.

Dica: Utilize argumentos variáveis (*args) para essa adaptação.
"""

def calculadora(opera: str):
    def soma(*n):
        return sum(n)

    def sub(*n):
        result = n[0]
        for num in n[1:]:
            result -= num

        return result 

    def mult(*n):
        result = 1
        for num in n:
            result *= num
        return result

    def div(*n):
        result = n[0]

        for num in n:

            if num == 0:
                raise ValueError("Divisão por zero não existe.")
        result /= num
        return result

    if opera == "somar":
        return soma

    elif opera == "subtrair":
        return sub

    elif opera == "multiplicar":
        return mult

    elif opera == "dividir":
        return div

    else:

        def opera_nao_suportada(*n):
            return "Operação não suportada"

        return opera_nao_suportada

add = calculadora("dividir")
print(add(10,2))