# DESAFIO

# 1) Solicite ao usuário que digite seu nome

# 2) Solicite ao usuário que digite o valor do seu salário. Converta a entrada para número de ponto flutuante

# 3) Solicite ao usuário que digite o valor de bônus recebido. Converta a entrada para número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# RESPOSTA

CONSTANTE_BONUS = 1000   # Evitar deixar números em hardcode.
nome = input('Digite o seu nome: ')
salario = float(input('Informe o valor do seu salário: '))
bonus = float(input('Informe o valor do bônus: '))
kpi = (CONSTANTE_BONUS + (salario * bonus))


print(f'O cálculo do KPI de 2024 é de {CONSTANTE_BONUS} + {salario} * {bonus}.')

print(f'Olá {nome}! O seu salário é de R$ {salario} e o bônus recebido foi de {bonus}%. O valor total de KPI ficou em R$ {kpi}.')