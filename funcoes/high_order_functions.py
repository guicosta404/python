# Funções que podem recer e/ou retornar outras funções
import subprocess

def saudacao(msg,nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

texto = executa(saudacao, 'Bom dia', 'Luiz')
print(texto)