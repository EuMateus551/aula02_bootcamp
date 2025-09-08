#16 Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
entrada1 = input('Digite "Verdadeiro" ou "Falso": ')
entrada2 = input('Digite "Verdadeiro" ou "Falso": ')

valor1 = entrada1.upper().strip() == "VERDADEIRO"
valor2 = entrada2.upper().strip() == "VERDADEIRO"

resultado = valor1 and valor2

print(resultado)

#17 Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
entrada1 = input('Digite "Verdadeiro" ou "Falso": ')
entrada2 = input('Digite "Verdadeiro" ou "Falso": ')

valor1 = entrada1.capitalize().strip() == "True"
valor2 = entrada1.capitalize().strip() == "True"

resultado = valor1 or valor2

print(resultado)

#18 Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
entrada = input('Digite "Verdadeiro" ou "Falso": ')

valor = entrada.lower().strip() == "true"
valor = not valor

print(valor)

#19 Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = int(input("DIgite um número: "))
num2 = int(input("DIgite um número: "))

if num1 == num2:
    resultado = "True"
else:
    resultado = "False"
print(resultado)

#20 Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = int(input("DIgite um número: "))
num2 = int(input("DIgite um número: "))

if num1 != num2:
    resultado = "False"
else:
    resultado = "True"
print(resultado)