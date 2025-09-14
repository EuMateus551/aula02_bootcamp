#Exercício 21: Conversor de Temperatura
#Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.
try:
  tem_celcius = float(input("Informe a temperatura em celcius: "))
  temp_farenheit = (tem_celcius * 9/5) + 32
  print(temp_farenheit)
except ValueError:
  print("Erro: Digite apenas um valor numérico")

#Exercício 22: Verificador de Palíndromo
#Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
import string
try:
  frase = input("Digite uma palavra ou frase: ")
  
  if not isinstance(frase, str):
    raise ValueError("Erro: Você não digitou uma palavra ou frase")
  
  frase_limpa = frase.lower()
  frase_limpa = frase_limpa.replace()
  frase_limpa = frase_limpa.translate()

  frase_invertida = frase_limpa[::-1]

  if frase_limpa == frase_invertida:
    print("É um palíndromo")
  else:
    print("Não é um palíndromo")
except ValueError as e:
  print(f"Erro: {e}")
  
#Exercício 23: Calculadora Simples
#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
  entrada_1 = float(input("Digite o primeiro número: "))
  entrada_2 = float(input("Digite o segundo número: "))
  operador = input("Digite o operador entre +, -, * e /: ")

  if operador == "+":
    print(entrada_1+entrada_2)
  elif operador == "-":
    print(entrada_1-entrada_2)
  elif operador == "*":
    print(entrada_1*entrada_2)
  elif operador == "/":
    try:
      print(entrada_1/entrada_2)
    except ZeroDivisionError as e:
      print("Erro: Não é possível dividir por 0.")
  else:
    print("Erro! Digite um dos operadores matematicos definidos")
except ValueError as e:
  print("Erro:", e)


#Exercício 24: Classificador de Números
#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".
Tipo_de_numero = ""
impar_ou_par= ""

try: 
  numero = float(input("Digite um número: "))

  if numero > 0:
    Tipo_de_numero = "Positivo"
  elif numero==0 :
    Tipo_de_numero = "Neutro"
  else:
    Tipo_de_numero = "Negativo"
  
  if numero%2 == 0:
    impar_ou_par = "Par"
  else:
    impar_ou_par = "Ímpar"

  print(f"O número é {impar_ou_par} e {Tipo_de_numero}")

except ValueError:
  print("Erro: Você não dogitou um número")

#Exercício 25: Conversão de Tipo com Validação
#Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
entrada = input("Digite uma lista de números separado por vírgula: ")

quebrar_entrada = entrada.split(",")
lista_de_numeros=[]
try:
  for elemento in quebrar_entrada:
    numero = int(elemento.strip())
    lista_de_numeros.append(numero)
  
  print(f"Esses são os números: {lista_de_numeros}")
except ValueError:
  print("Erro: Digite apenas números inteiros")