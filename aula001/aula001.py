# PRINT - Utilizamos para exibir alguma informação na tela.
print('Hello world!')

# Conseguimos imprimir números também.
print(3+5)


# INPUT - Utilizamos quando queremos capturar alguma informação do usuário. Podemos fazer isso ao mesmo tempo que imprimimos na tela.
print(input('Digite o seu nome: '))

# Exemplo 1
print( 'Olá, ' + input('Digite o seu nome: ') + '!')

# Exercício 1 - Crie um programa que o usuário digita o seu nome e retorna o número de caractére.

quantidade_caracter = print(input('Digite o seu nome: '))
len(quantidade_caracter)
print('O seu nome tem ' + len(quantidade_caracter) + 'letras!')