BONUS_2024 = 1000
ANO = 2024

# 1) Solicita o nome do usuário
nome_usuario = input("Digite seu nome:")

# 2) Solicita ao usuário que digite o valor do seu salário e converte a entrada para float
valor_salario = float(input("Digite o valor do seu salário?:"))

# 3) Solicita ao usuário o valor do bônus final
valor_bonus = float(input("Qual o valor do bônus?:"))

# 4) Cálculo do KPI do bônus 2024
kpi = BONUS_2024 + valor_salario*valor_bonus

# 5) Imprima a mensangem personalizada com o nome do usuário, salário e o valor do bônus
print(f"Olá {nome_usuario}, o valor do seu bônus em {ANO} foi de {kpi}")
