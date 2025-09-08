import math

#6 Escreva um programa que receba dois números flutuantes e realize sua adição.
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

soma = num1 + num2

print(soma)

#7 Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

soma = num1 + num2
media = soma/2

print(media)

#8 Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Informe qual é a base da potência: "))
expoente = float(input("Informe qual é o expoente da potência: "))

potencia = pow(base, expoente)

print(potencia)

#9 Faça um programa que converta a temperatura de Celsius para Fahrenheit.
tem_celcius = float(input("Informe a temperatura em celcius: "))
temp_farenheit = (tem_celcius * 9/5) + 32

print(temp_farenheit)

#10 Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("informe o raio do círculo: "))

area = math.pi * (raio ** 2)

print(area)