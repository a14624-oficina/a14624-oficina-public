#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("Insira a sua idade:")
nome = input("Insira o seu nome:")
print(f"0 meu nome é{nome} e tenho {idade} anos.")
#EX0.2
"""
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("Olá mundo!");
fruta = "maçá"
print("Eu gosto de {maçã}")
#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input("Insira o seu nome:")
print(f"bom dia,{nome} desejo um otimo dia :")
valor =int(input("Insira um numero:"))
dobro = valor * 2
print(f"0dobro de {valor} é {dobro}")

#EX1.1
""""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""
print("\nBem-vindo ao python!")

#EX1.2
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
print("\nBe-vindo José Miguel ao Python!")

#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
mensagem= 
 ____                    ____  _       
| __ )  ___  _ __ ___   |  _ \(_) __ _ 
|  _ \ / _ \| '_ ` _ \  | | | | |/ _` |
| |_) | (_) | | | | | | | |_| | | (_| |
|____/ \___/|_| |_| |_| |____/|_|\__,_|
print("mensagem")
"""Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis."""
nome = " José Miguel"
idade = int("15")
localidade = ("trofa")
print(nome, idade,localidade)
#EX1.5
"""Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem"""
liguagemProg= "Python"
nome = "José"
print(f"0 {nome} sabe programar em {linguagemProg}")

#EX1.6
"""Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres."""
print(f'{'bem-VINDOS aopython!': <50}')
print(f'bem-VINDOS ao python': ^50}')
print(f'{'bem-vindo ao python':>50}')
#EX1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""
from types import MemberDescriptorType


raio = float(input("Insira  o raio do círcunferencia:")
 circunferecia = 2*3.14*raio 
area = 3.14*(raio)**2
print("Uma circunferencia do raio " raio"unidade: ")
print("Perimetro:"circunferencia"unidade")
print("Area"area"unidade")

#EX1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20
"""
from dataclasses import make dataclasse
import datetime 
x = diatetime.datetime.now
Dia = x.strftime("%d2")
Mes = x.strftime("%m2")
Ano = x.stritime("%y2")
hora = x.stritime("%h")
minuto = x.stritime("%S")
print(f"{dia}---{mes}---{ano}")
print(f"{dia}---{mes}---{ano}---{hora}:{minuto}:{segundos}")
print(f"{mes}/---{dia}/---{ano}")

#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""
print("digite o numero do ateleta 12304")
print("digite a pontuaçao final 7.89")
print("o ateleta numero 12345 obteve 7.89 pontos")

nome = str(input('Qual é seu nome? '))
if nome == 'José':
  print('Que nome lindo tu tens!')
else:
  print('O teu nome é tão comum')
print('Bom dia, {}!'.format(nome))

#autonomia
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    m = (n1 + n2 )/2
    print('A tua média foi {:.1f}'.format(m))
    if m >= 6.0:
      print('A tua média foi boa! PARABÉNS!')
    else:
      print('A tua média foi má! ESTUDA MAIS!')
     import random

     segredo = int (random.randint(0,5))
     #print(f" o número secreto é: {segredo}")
     numeroescolhido = int(input(" Insira um valor entre (0 e 5) :"))

     if  numeroescolhido > segredo:
       print("O numero inserido maior que o meu!")
     elif numeroescolhido < segredo:
       print("O numero insirido é menor que o meu!")
     else:
       print("Acertates")
     #029
  """ escreva um programa que leia a velocidade de um carro
   se ele ultrapssar 80 km/h mostre uma mensagem dizendo que ele foi multado
  a multa vai custar 7,00€ por cada km acima do limite """
    velocidade = int(input("Insira a velocidade em que estava:"))
  multa = (velocidade)-80
   valor= (multa)*7
  if velocidade > 80: 


                    #2. Exercícios
   """
 Exercício FP1: Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.                                                  Dica: Usa as estruturas condicionais if, elif e else.
  """
  """
   [consola]
   Introduza um número: 10
   O número é positivo.
      """
    numero = int(input("Insira um número:"))
  if numero == 0:
   print("O número é zero.")
  elif numero < 0:
    print("O número é negativo")
  elif numero > 0:
  print(" O numero é positivo"

#2. Exercícios
"""
Exercício FP2:Verificar se um número é par ou ímpar. Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %


 [consola]
                           
            
Introduza um número:                                               
O número é ímpar.
"""
x = int(input("Insira o numero"))
resultado= x % 2 
 if resultado == 0:
  print(" O numero é par")
 else:
  print("O numero é impar")

#Exercicio FP3
 """
Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:
Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"
  """


 """
 Introduza a nota final: 16
 Classificação: Bom
"""
   notafinal = int(input("Insira a Nota final do aluno: "))

 if notafinal < 10:
   print("Reprovado")
elif notafinal >= 10 and notafinal <= 14:
  print("suficiente")
 elif notafinal >= 15 and notafinal < 17:
  print("bom")
else:
  print("muito bom")

   #Exercício FP4
   """
    Conversor de temperaturas.
    Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

    Fórmulas:

    Fahrenheit = Celsius * 9/5 + 32
    Kelvin = Celsius + 273.15
    """
   celsius = float(input(" Insira a temperarura em graus celsius"))
   Fahrenhit = (celsius * 9/5) + 32
   Kelvin = celsius + 273.15
   opcao = str(input( " Escolha a conversão para Fahrenheit (F) kelvin (K) ou Ambas (A)"))
   if opcao == "F" :
       print(f" O valor em fahrenheit é  {Fahrenhit} ")
   elif opcao == "K":
       print(f"O valor em Kalvin é  {Kelvin}  ")
   if  opcao == "A":
       print(f" O valor em fahrenheit é {Fahrenhit} e em kelvin é { Kelvin}")
   else:
       print("Opeção invalida")

   #Exercício FP5:
  """
   Cálculo de impostos
   Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

   Salário até 1000: isento de impostos
   Salário entre 1001 e 2000: 10% de imposto
   Salário superior a 2000: 20% de imposto
   O programa deve exibir o salário após a dedução do imposto.

   [consola]
   Introduza o seu salário: 2500
   Salário após impostos: 2000.0
   """
  salario = float(input("Insere o seu sálario mensal: "))
if salario <= 1000 : 
       print("o seu imposto é zero ésta isento de imposto")
elif salario > 1000 and salario < 2000 :
       imposto1 = salario * 0.10
       salarioImposto = salario - imposto
       print(f"o seu salário mensal com imposto de 10% é de : {salarioImposto}")
elif salario >= 2000:
       imposto = salario *0.20
       salarioImposto = salario - imposto
       print(f"o seu salário mensal com imposto de 20% é de: {salarioImposto:2f}€")


       #Exercício FP6

"""
Imprimir números de 1 a 10.
 Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.

 [consola]
1
2
3
...
10
"""

for  x in range(1,11):
   print(x)


   #Exercício FP7:
   """
   Soma de números de 1 a 100.
   Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.

   [consola]
   A soma de 1 a 100 é: 5050
   """
   soma = 0
   contador = 1
   # Usar ciclo while para somar de 1 a 100
   while contador <=100:
     soma+= contador
     contador+=1
     # Mostrar resultado na consola
   print(f" A soma de 1 a 100 é:{soma}")


   #Exercício FP8:
   """
   Contagem de vogais numa string.
   Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.

   [consola]
   Introduza uma frase: Programação em Python
   Número de vogais: 7
   """

   frase = input("Insira uma frase ")
   vogais = 0 
   for letra in frase:
          if letra  == "a" or letra == "e" or letra == "i "or letra == "o" or letra == "u":
           vogais += 1

   print(f"A frase tem {vogais} vogais")


 #Exercício FP9
 """
  Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.

[consola]
5
10
15
...
 50
 """
   
temporario = 0
   for i in range (1,51):
   if temporario <= 49:
    temporario = i * 5
    print(temporario)

   #Exercício FP10: 
   """
   Média de uma lista de números
   Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.

   [consola]
   Introduza o número 1: 10
   Introduza o número 2: 20
   Introduza o número 3: 30
   Introduza o número 4: 40
   Introduza o número 5: 50
   A média é: 30.0
   """
   notas=[]

   for i in range (0,5):
     numeros = int(input(" escreva um numero inteiro: "))
     notas.append(numeros)
     soma = sum (notas)
     valor1 = notas [0]
   x = len (notas)
   media = (soma/x)
   print(x)
   print(media)

        : 
        #Exercício FP11: 
 """
  Verificar se um número é primo.
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.

[consola]
 Introduza um número: 13
13 é um número print
 """
numero = int(input('Numero: '))
    divisores = 0
        if numero >= 1:
            for i in range(1, numero + 1):
                if numero % i == 0: #verfica se o resultado é divisão é 0 
                    divisores += 1 #incrementa o contador de divisores
        if divisores == 2:
                    print(f"o {numero}, é um numero primo")
        else:
                  print(f"o {numero}, não é um numero primo")
   #Exercício FP12:
   """
   Gerar uma lista de números pares.
   Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.

   [consola]
   Lista de números pares: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
   """
   lista = []
   for i in range(1,21):
    if i % 2 == 0: 
        lista.append(i)
   print(f" Lista  de numeros pares: {lista}")

   #Exercício FP13  Inverter uma string.
   """
   Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.

   [consola]
   Introduza uma palavra: Python
   A palavra invertida é: nohtyP
   """
   texto = str(input ( "Insira um texto: ")) #pedir o texto ao utilizador
   textoinv = texto [::-1] # scrip para inverter o texto
   print(textoinv) # Printar o texto invertido

           #Exercício FP14 
           """

           Tabuada de multiplicação
           Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.

           [consola]
           Introduza um número: 6
           Tabuada de 6:
           6 x 1 = 6
           6 x 2 = 12
           ...
           6 x 10 = 60
           """
           """
           num = int(input(" Intuduza um numero: "))
           for i in range(1,11):
            mult = num * i
            print(f"{num} x {i} = {mult}")
            """
           num = int(input("Introduza um numero: "))
           i = 1
           while i <11:
             mult = num * i
             print(f"{num} x {i} = {mult}")
             i += 1
