### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

try: 
    nome = input("Digite seu nome: ")

    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio")
        exit()
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números")
        exit()
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)
    exit()

    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Por favor, Digite um valor positivo para seu salário")
    except ValueError:
        print("Entrada inválida para o salário. Por favor, digite um número")
        exit()
    
    try:
        bonus = float(input("Digite o valor do seu bônus: "))
        if bonus < 0:
            print("Por favor, Digite um valor positivo para o bônus")
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número")
        exit()
    bonus_recebido = 1000 + salario*bonus

    print(f"{nome}, seu salário é de R${salario:.2f} e seu bõnus final é R${bonus_recebido:.2f}")