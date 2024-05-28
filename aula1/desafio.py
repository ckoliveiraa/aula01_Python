BONUS_2024 = 1000
ANO = 2024


"""Função para buscar o nome do usuário"""
# 1) Solicita o nome do usuário
nome_usuario = input("Digite seu nome:")

if nome_usuario.isdigit():
    print("Favor digite seu nome sem número")
    exit()
elif nome_usuario.isspace():
    print("Você digitou apenas espaço")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou seu nome ")
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário e converte a entrada para float
try:
    valor_salario = float(input("Digite o valor do seu salário?:"))
except ValueError:
    print("Digite um valor numérico")

# 3) Solicita ao usuário o valor do bônus final
try:
    valor_bonus = float(input("Qual o valor do bônus?:"))
except ValueError:
    print("Digite um valor numérico")
    exit()
# 4) Cálculo do KPI do bônus 2024
kpi = BONUS_2024 + valor_salario*valor_bonus

# 5) Imprima a mensangem personalizada com o nome do usuário, salário e o valor do bônus
print(f"Olá {nome_usuario}, o valor do seu bônus em {ANO} foi de {kpi}")
