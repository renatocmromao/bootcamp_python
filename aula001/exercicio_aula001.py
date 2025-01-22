# Exercício 1 - Crie um programa que o usuário digita o seu nome e retorna o número de caractére.

# Minha solução

nome = input('Digite o seu nome: ')
print(f'Olá {nome}! O seu nome tem {len(nome)} letras!')

print('\n')
# Solução do curso

print(len(input('Digite o seu nome: ')))


print('\n')
# Exercício  - Peça para o usuário informar 2 números e some eles.

# Minha solução

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

soma = (num1 + num2)

print(f'A soma do número {num1} e {num2} será {soma}.')
print('\n')
# Solução do curso

print(int(input('Digite o primeiro número: ')) + int(input('Digite o segundo número: ')))
print('\n')