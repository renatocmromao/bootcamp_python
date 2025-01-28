'''
# INT

# 1) Escreva um programa que some dois números inteiros inseridos pelo usuário.
print('1) Escreva um programa que some dois números inteiros inseridos pelo usuário.')
print('RESPOSTA:')
print('*** Programa de ADIÇÃO ***')
num_1 = int(input('Insira um número, para ser o valor 1: '))
num_2 = int(input('Insira um número, para ser o valor 2: '))
print(f'A soma dos números {num_1} e {num_2} será {num_1 + num_2}.')


# 2) Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print('2) Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.')
print('RESPOSTA:')
print('*** Programa de DIVISÃO POR 5 ***')
num_1 = int(input('Insira um número: '))
print(f'O resultado do resto da divisão, do número {num_1} dividido por 5 será {num_1 % 5}.')


# 3)Desenvolva um programa que multiplique dois números fornecidos pleo usuário e mostre o resultado.
print('3)Desenvolva um programa que multiplique dois números fornecidos pleo usuário e mostre o resultado.')
print('RESPOSTA:')
print('*** Programa de MULTIPLICAÇÃO ***')
num_1 = int(input('Insira um número, para ser o valor 1: '))
num_2 = int(input('Insira um número, para ser o valor 2: '))
print(f'O resultado da operação {num_1} * {num_2} será {num_1 * num_2}.')


# 4) Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print('4) Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.')
print('RESPOSTA:')
print('*** Programa de DIVISÃO INTEIRA ***')
num_1 = int(input('Insira um número INTEIRO, para ser o valor 1: '))
num_2 = int(input('Insira um número INTEIRO, para ser o valor 2: '))
print(f'O resultado da operação {num_1} // {num_2} será {num_1 // num_2}.')


# 5) Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
print('5) Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.')
print('RESPOSTA:')
print('*** Programa de POTENCIAÇÃO ***')
num_1 = int(input('Insira um número INTEIRO, para ser o valor 1: '))
num_2 = int(input('Insira um número INTEIRO, para ser o valor 2: '))
print(f'O resultado da operação {num_1} ** {num_2} será {num_1 ** num_2}.')


# FLOAT

# 6) Escreva um programa que receba dois números flutuantes e realize a sua adição.
print('6) Escreva um programa que receba dois números flutuantes e realize a sua adição.')
print('RESPOSTA:')
print('*** Programa de ADIÇÃO DE NÚMEROS FLUTUANTES ***')
num_1 = float(input('Insira um número FLUTUANTE, para ser o valor 1: '))
num_2 = float(input('Insira um número FLUTUANTE, para ser o valor 2: '))
print(f'O resultado da operação {num_1} + {num_2} será {num_1 + num_2}.\n')

# 7) Crie um programa que clacule a média de dois números flutuantes fornecidos pelo usuário.
print('7) Crie um programa que clacule a média de dois números flutuantes fornecidos pelo usuário.')
print('RESPOSTA:')
print('*** Programa de CÁLCULO DE MÉDIAS ***')
num_1 = float(input('Insira um número FLUTUANTE, para ser o valor 1: '))
num_2 = float(input('Insira um número FLUTUANTE, para ser o valor 2: '))
print(f'O resultado da operação {num_1} + {num_2} / 2, será {num_1 + num_2 / 2}.\n')

# 8) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print('8) Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).')
print('RESPOSTA:')
print('*** Programa de CÁLCULO DE POTENCIAS ***')
num_1 = float(input('Insira um número FLUTUANTE, para ser a BASE: '))
num_2 = float(input('Insira um número FLUTUANTE, para ser a POTÊNCIA: '))
print(f'O resultado da operação {num_1} ** {num_2}, será {num_1 ** num_2}.\n')


# 9) Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print('9) Faça um programa que converta a temperatura de Celsius para Fahrenheit.')
print('RESPOSTA:')
print('*** Programa CONVERSOR DE CELSIUS PARA FAHRENHEIT ***')
num_1 = float(input('Insira o valor em CELCIUS: '))
conv_far = (num_1 * 1.8) + 32
print(f'O valor de {num_1} graus Celcius será {conv_far} graus Fahrenheit.\n')


# 10) Escreva um programa que calcule a área de círculo, recebendo o raio como entrada.
print('10) Escreva um programa que calcule a área de círculo, recebendo o raio como entrada.')
print('RESPOSTA:')
print('*** Programa CALCULAR A ÁREA DE UM CÍRCULO***')
raio = float(input('Insira o valor do RAIO: '))
area_circ = (raio ** 2) * 3.14
print(f'Com o raio medindo {raio}, o valor da área do círculo será de {area_circ}.\n')


# STRING

# 11) Escreva um programa que receba uma string do usuário e a converta para maiúscula.
print('11) Escreva um programa que receba uma string do usuário e a converta para maiúscula.')
print('RESPOSTA:')
print('*** Programa de CONVERTE STRING PARA LETRAS MAIÚSCULA***')
valor = input('Insira uma palavra ou uma frase: ')
print(f'A frase é: {valor}.\n')
print(f'Convertendo as letras para Maiúscula ficará da seguinte forma: {valor.upper()}.\n')


# 12) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
print('12) Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.')
print('RESPOSTA:')
print('*** Programa de CONVERTE STRING PARA LETRAS MINÚSCULA***')
valor = input('Insira o seu nome completo (EM CAIXA ALTA): ')
print(f'A frase é: {valor}.\n')
print(f'Convertendo as letras para Minúscula ficará da seguinte forma: {valor.lower()}.\n')


# 13) Desenvolva um programa que peça ao usuário para inserir uma frase e em seguida, imprima esta frase sem espaços em branco no início e no final.
print('13) Desenvolva um programa que peça ao usuário para inserir uma frase e em seguida, imprima esta frase sem espaços em branco no início e no final.')
print('RESPOSTA:')
print('*** Programa de RETIRA OS ESPAÇOS EM BRANCO DO COMEÇO E DO FINAL ***')
valor = input('Insira uma frase pequena (COM ESPAÇOS EM BRANCO NO COMEÇO E FINAL): ')
print(f'A frase é: {valor}.\n')
print(f'Retirando os espaços em branco do começo e do final ficará: {valor.strip()}.\n')


# 14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaa" e em seguida, imprima o dia, o mês e o ano separadamente.
print('14) Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaa" e em seguida, imprima o dia, o mês e o ano separadamente.')
print('RESPOSTA:')
print('*** Programa PARA RETIRAR SEPARADOR ***')
valor = input('Insira uma data (NO FORMATO DD/MM/AAAA): ')
print(f'A data é: {valor}.\n')
print(f'Retirando o separador "/", teremos os seguintes valores: {valor.split("/")}.\n')


# 15) Escreva um programa que concatene duas strings fornecidas pelo usuário.
print('15) Escreva um programa que concatene duas strings fornecidas pelo usuário.')
print('RESPOSTA:')
print('*** Programa de CONCATENAÇÃO DE STRINGS ***')
val1 = input('Insira uma pequena frase: ')
val2 = input('Insira outra uma pequena frase: ')
print(f'O resultado da concatenação das frases será: {val1 +  " e " + val2}.\n')

# BOOLEANOS

# 16) Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
print('16) Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.')
print('RESPOSTA:')
print('*** Programa de Avaliação AND ***')
val1 = input('Digite True ou False, para o primeiro valor: ')
val_2 = input('Digite True ou False, para o segundo valor: ')
print(f'O primeiro valor é {val1} e o segundo valor é {val_2}, logo o resultado da operação lógica AND será {val1 and val_2}.\n')


# 17) Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
print('17) Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.')
print('RESPOSTA:')
print('*** Programa de Avaliação OR ***')
val1 = input('Digite True ou False, para o primeiro valor: ')
val_2 = input('Digite True ou False, para o segundo valor: ')
print(f'O primeiro valor é {val1} e o segundo valor é {val_2}, logo o resultado da operação lógica OR será {val1 or val_2}.\n')


# 18) Desenvolva um programa que peça ao usuário para inserir um valor booleano e em seguida, inverta esse valor.
print('18) Desenvolva um programa que peça ao usuário para inserir um valor booleano e em seguida, inverta esse valor.')
print('RESPOSTA:')
print('*** Programa de Avaliação NOT ***')
val1 = input('Digite True ou False, para o primeiro valor: ')
val_2 = input('Digite True ou False, para o segundo valor: ')
print(f'O primeiro valor é {val1} e o segundo valor é {val_2}, logo o resultado da operação lógica NOT será: ')
print(f'Primeiro Valor {not val1}.')
print(f'Segundo Valor {not val_2}.\n')


# 19) Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print('19) Faça um programa que compare se dois números fornecidos pelo usuário são iguais.')
print('RESPOSTA:')
print('*** Programa de Avaliação Números Iguais ***')
val1 = input('Digite um número, para o primeiro valor: ')
val_2 = input('Digite um número, para o segundo valor: ')
print(f'O primeiro valor é {val1} e o segundo valor é {val_2}.')
print(f'Eles são iguais: {val1 == val_2}')
'''

# 20) Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#print('19) Faça um programa que compare se dois números fornecidos pelo usuário são iguais.')
print('RESPOSTA:')
print('*** Programa de Avaliação Números Diferentes ***')
val1 = input('Digite um número, para o primeiro valor: ')
val_2 = input('Digite um número, para o segundo valor: ')
print(f'O primeiro valor é {val1} e o segundo valor é {val_2}.')
print(f'Eles são diferentes: {val1 != val_2}')
#
#
#
#
#
