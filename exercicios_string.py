#11 Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
palavra = input("Escreva uma palavra: ")

maiusculo = palavra.upper()

print(maiusculo)

#12 Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Escreva seu nome completo: ")

nome_minusc = nome.lower()

print(nome_minusc)

#13 Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Escreva uma frase: ")

frase = frase.strip()

print(frase)

#14 Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = str(input("Informe uma data no formato dd/mm/aaaa: "))

dia, mes, ano = data.split('/')

print("dia:", dia)
print("mês", mes)
print("ano:", ano)

#15 Escreva um programa que concatene duas strings fornecidas pelo usuário.
str1 = input("Informe a primeira palavra: ")
str2 = input("Escreva a segunda palavra: ")

print(str1 + str2)