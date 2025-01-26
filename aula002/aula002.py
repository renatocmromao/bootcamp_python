# Tipos de dados

# INTEIROS (int)
print('INTEIROS (int)')
print('Métodos e Operações')
# Métodos e Operações
# Adição                 (+)
num1 = 10
num2 = 5
soma = num1 + num2
print('Adição')
print(f'{num1} + {num2} = {soma}')
print(f'O resultado da SOMA do número {num1} mais o número {num2} será igual a {soma}.\n')

# Subtração              (-)
num1 = 10
num2 = 5
subtra = num1 - num2
print('Subtração')
print(f'{num1} - {num2} = {subtra}')
print(f'O resultado da SUBTRAÇÃO do número {num1} menos o número {num2} será igual a {subtra}.\n')

# Multiplicação          (*)
num1 = 10
num2 = 5
multi = num1 * num2
print('Multiplicação')
print(f'{num1} * {num2} = {multi}')
print(f'O resultado da MULTIPLICAÇÃO do número {num1} multiplicado pelo número {num2} será igual a {multi}.\n')

# Divisão inteira        (//)
num1 = 10
num2 = 5
divint = num1 // num2
print('Divisão inteira')
print(f'{num1} // {num2} = {divint}')
print(f'O resultado da DIVISÃO INTEIRA do número {num1} dividido pelo número {num2} será igual a {divint}.\n')

# Módulo da divisão      (%)
num1 = 10
num2 = 5
div = num1 % num2
print('Módulo da divisão')
print(f'{num1} % {num2} = {div}')
print(f'O resultado do RESTO DA DIVISÃO entre os números {num1} dividido pelo número {num2} será igual a {div}.\n')



# PONTO FLUTUANTE (float)
print('PONTO FLUTUANTE (float)')
print('Métodos e Operações')
# Métodos e Operações
# Adição                 (+)
num1 = 100
num2 = 10
soma = num1 + num2
print('Adição')
print(f'{num1} + {num2} = {soma}')
print(f'O resultado da SOMA do número {num1} mais o número {num2} será igual a {soma}.\n')

# Subtração              (-)
num1 = 100
num2 = 10
subtra = num1 - num2
print('Subtração')
print(f'{num1} - {num2} = {subtra}')
print(f'O resultado da SUBTRAÇÃO do número {num1} menos o número {num2} será igual a {subtra}.\n')

# Multiplicação          (*)
num1 = 100
num2 = 10
multi = num1 * num2
print('Multiplicação')
print(f'{num1} * {num2} = {multi}')
print(f'O resultado da MULTIPLICAÇÃO do número {num1} multiplicado pelo número {num2} será igual a {multi}.\n')

# Divisão                (/)
num1 = 100
num2 = 10
div = num1 // num2
print('Divisão')
print(f'{num1} // {num2} = {div}')
print(f'O resultado da DIVISÃO INTEIRA do número {num1} dividido pelo número {num2} será igual a {div}.\n')

# Potenciação            (**)
num1 = 100
num2 = 10
poten= num1 ** num2
print('Potenciação')
print(f'{num1} ** {num2} = {div}')
print(f'O resultado da POTENCIAÇÃO do número {num1} elevado ao número {num2} será igual a {poten}\n')


# STRING (str)
print('STRING (str)')
print('Métodos e Operações')
# Métodos e Operações
# .upper()                 (Converte todas as letras para maiúscula)
frase1= 'A casa é bela.'
maiuscula = frase1.upper()
print('.upper()')
print(f'O método para deixar todas as letras maiúsculas é o .upper(). Exemplo:')
print(frase1)
print(f'Convertando a frase usando o método .upper(), ficará: {maiuscula}\n')

# .lower()                 (Converte todas as letras para minúscula)
frase1= 'O MUNDO É GRANDE.'
minuscula = frase1.lower()
print('.lower()')
print(f'O método para deixar todas as letras minúsculas é o .lower(). Exemplo:')
print(frase1)
print(f'Convertando a frase usando o método .lower(), ficará: {minuscula}\n')

# .strip()                 (Remove os espaços em branco no início e no final)
frase1= '    O jardim da vida.     '
sem_espaco = frase1.strip()
print('.strip()')
print(f'O método para retirar os espaços na frente e atrás é o .strip(). Exemplo:')
print(frase1)
print(f'Convertando a frase usando o método .strip(), ficará: {sem_espaco}\n')

# D.split(sep)             (Divide a string em uma lista, utilizando [sep] como delimitador)
email1= 'renatocarvalho@tiranic.com.br'
separado = email1.split("@")  #lembrar de colocar o separador entre aspas.
print('.split("sep")')
print(f'O método para dividir a string em uma lista delimitado pelo separador ([sep]) é o .split([sep]). Exemplo:')
print(email1)
print(f'Convertando a frase usando o método .strip(), ficará: {separado}\n')

# +                        (Concatenação de strings)
frase1 = 'Viajar é bom.'
frase2 = 'E eu gosto muito.'
juntos = frase1 + frase2
print('Concatenação - "+"')
print(f'O método para concatenar as strings é utilizando o operador [+]. Exemplo:')
print(f'A frase {frase1}, concatenada a frase {frase2} será a frase {juntos}\n')


# BOOLEANOS (bool)
print('BOOLEANOS (bol)')
print('Operações Lógicas')
#Operações Lógicas
# and   ('E' lógico) 
valor1 = True
valor2 = True
print('valor1 = True')
print('valor2 = True')
print('valor1 AND valor2')
print(f'Resultado será {valor1 and valor2}')
print('===================================')
valor1 = True
valor2 = False
print('valor1 = True')
print('valor2 = False')
print('valor1 AND valor2')
print(f'Resultado será {valor1 and valor2}\n')
print('No operador lógico AND, quando algum valor for FALSE, o resultado será FALSE. Somente quando ambos forem TRUE, o resultado será TRUE.')

# or    ('OU' lógico)
valor1 = True
valor2 = True
print('valor1 = True')
print('valor2 = True')
print('valor1 OR valor2')
print(f'Resultado será {valor1 or valor2}')
print('===================================')
valor1 = True
valor2 = False
print('valor1 = True')
print('valor2 = False')
print('valor1 OR valor2')
print(f'Resultado será {valor1 or valor2}\n')
print('No operador lógico OR, quando algum valor for TRUE, o resultado será TRUE. Somente quando ambos forem FALSE, o resultado será FALSE.')

# not   ('NÃO' lógico)

valor1 = True
valor2 = False
print('valor1 = True')
print('valor2 = False')
print('not valor1')
print(f'O resultado será {not valor1}')
print('not valor2')
print(f'O resultado será {not valor2}')
print('No operador lógico NOT, irá inverter o valor lógico de um operando.')

# ==    (Igualdade)
valor1 = False
valor2 = False
print('valor1 = False')
print('valor2 = False')
print('valor1 == valor2')
print(f'O resultado será {valor1 == valor2}')
print('No operador lógico de IGUALDADE, será TRUE quandos os valores forem IGUAIS.')

# !=    (Diferença)
valor1 = True
valor2 = False
print('valor1 = True')
print('valor2 = False')
print('valor1 != valor2')
print(f'O resultado será {valor1 != valor2}')
print('No operador lógico de DIFERENÇA, será TRUE quandos os valores forem DIFERENTES.')
