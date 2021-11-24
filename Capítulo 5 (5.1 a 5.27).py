""" Programa:
x = 0
while x<= 3:
    print(x)
    x=x+1 """


# 5.1) Modifique o exemplo acima para exibir números de 1 a 100.

x = 1
while x <=100:
    print(x)
    x = x + 1 


# 5.2) Modifique o exemplo para exibir números de 50 a 100.

x = 50
while x<=100:
    print(x)
    x=x+1 


# 5.3) Faça um programa para escrever a contagem regressiva do lançamento de um foguete. Imprimir: 10,9,8,7,6,5,4,3,2,1,0 e Fogo!

x = 10
while x<=10:
    print(x)
    x = x - 1
    if x<0:
        break
print("e fogo!") 


# 5.4)  Escreva um programa para imprimir os números ímpares de 1 até o número digitado pelo usuário.

número = int(input("Digite um número: "))
x = 1
while x <= número:
    print(x)
    x = x + 2 

# 5.5) Reescreva o programa anterior para imprimir os 10 primeiros múltiplos de 3.
x = 3
while x <=30:
    if x % 3 == 0:
        print(x)
        x = x + 3 

 # Exemplo do livro: para imprimir a tabuada de adição para um número digitado pelo usuário. Deve ser impressa de 1 a 10:
n = int(input("Digite a tabuada que você quer: "))
x = 1
while x<=10:
    print(n+x)
    x=x+1 


# 5.6) Repita o exemplo anterior para exibir resultados da tabuada: 2x1 = 2, 2x2=4 ...
n = 2
x = 1
while x <=10:
    print(x*n)
    x=x+1 


# 5.7) Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez de começar com 1 e 10.
a = int(input("Digite a partir de Digite número a tabuada do 2 deve começar: "))
b = int(input("Digite até Digite número você quer que a tabuada do 2 vá: "))
x=a
while x<=b:
    print(x*2)
    x=x+1 


# 5.8) Escreva um programa que leia 2 números solicitados ao usuário. Imprima o resultado da múltiplicação dos 2 números. Utilize apenas os operadores de soma e subtração.
# ex: 4x3 = 4+4+4 = 12
                    #para (4+4+4+4+4)
a = int(input("Escreva um número que deseja multiplicar: "))
b = int(input("Escreva outro número para multiplicar com o primeiro: "))
x=a
while x<=a*b:
    print(x)
    x=x+a 
                    #ou (5+5+5+5)
a = int(input("Escreva um número que deseja multiplicar: "))
b = int(input("Escreva outro número para multiplicar com o primeiro: "))
x=b
while x<=a*b:
    print(x)
    x=x+b 


# 5.9) Solicite 2 números. Leia a divisão inteira do primeiro pelo segundo, assim como o resto. Utilize apenas soma e subtração para calcular o resultado.
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a>b:
    resto = a%b
    x=a
    while x<=a:
        print(x)
        x=x-b
        if x<0:
            break
    print(f"O resto da divisão é: {resto}")
else:
    resto = a%b
    x=0
    while x<=b:
        print(x)
        x=a-b
        if x<0:
            break
print(f"O resto da divisão é: {resto}") 

# Exemplo para a questão 5.10:
# Veja um programa para corrigir um teste de múltipla escolha. A resposta da primeiro é "b", segunda "a" e terceira "d". Conte 1 ponto para cada resposta certa:
pontos = 0
questão = 1
while questão<=3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and resposta == "b":
        pontos = pontos + 1
    if questão == 2 and resposta == "a":
        pontos = pontos + 1
    if questão == 3 and resposta == "d":
        pontos = pontos + 1
    questão = questão + 1
print(f"O aluno fez {pontos} ponto(s)") 

# 5.10) Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as questões
pontos = 0
questão = 1
while questão<=3:
    resposta = input(f"Resposta da questão {questão}: ")
    if questão == 1 and resposta == "b" or resposta == "B":
        pontos = pontos + 1
    if questão == 2 and resposta == "a" or resposta == "A":
        pontos = pontos + 1
    if questão == 3 and resposta == "d" or resposta == "D":
        pontos = pontos + 1
    questão = questão + 1
print(f"O aluno fez {pontos} ponto(s)") 


# 5.11) Escreva um programa que pergunte o depósito inicial e a taxa de juros da poupança. Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho no período.

depósito = float(input("Digite quanto deseja depositar: R$ "))
taxa = float(input("Digite a taxa que deseja para o investimento: "))
x = 1
soma = 0
while x<=23:
    soma = (soma + depósito)*taxa + soma
    x = x + 1
    print(f"O rendimento no {x}° mês é de: R$ {soma:.2}")
print(f"O valor total é de: R$ {soma+depósito:.2f}") 


# 5.12) Altere o programa anterior de forma a perguntar também o valor a ser depositado mensalmente.

depósito_inicial = float(input("Digite quanto deseja depositar: R$ "))
taxa = float(input("Digite a taxa que deseja para o investimento: "))
depósito_mensal = float(input("Digite valor a ser depositado mensalmente? "))
x = 1
soma = 0
while x<=23:
    soma = (soma + depósito_inicial)*taxa + soma + depósito_mensal
    x = x + 1
    print(f"O acumulado no {x}° mês é de: R$ {soma:.2f}")
print(f"O valor total é de: R$ {soma+depósito_inicial:.2f}") 


# 5.13) Pergunte o valor inicial de uma dívida e o juro mensal. Pergunte o valor mensal que será pago. Exiba o número de meses que a dívida será paga, o total pago e o total de juros.

dívida = float(input("Digite o valor da sua dívida inicial? R$ "))
taxa_mensal = float(input("Digite o valor da taxa mensal? "))
pagar_mensal = float(input("Digite o valor que você pagará mensalmente? R$ "))
mês = 1
if (dívida*taxa_mensal) > pagar_mensal:
    print("A sua dívida não será paga nunca. Pois os juros são superiores ao pagamento.")
else:
    juros_pago = 0
    while dívida>pagar_mensal:
        juros = dívida*taxa_mensal
        dívida = dívida + juros - pagar_mensal
        juros_pago = juros_pago + juros
        mês = mês + 1 
    print(f"O número de meses para pagar a dívida é de: {mês}.")
    print(f"Você pagaria um total de R$ {juros_pago:.2f} de juros.")
    print(f"No ultimo mês, você teria uma saldo residual de R$ {dívida:.2f} a pagar") 


# 5.14) Ler números inteiros do teclado. Se o número digitado for 0, imprima quantos números foram digitados, assim como a soma e a média aritmética.
x=1
soma=0
while x:
    n=int(input(f"Digite o {x}° número: "))
    if n == 0:
        x=x-1
        break
    soma=soma+n
    x=x+1
print(f"A quantidade de números digitados foi de: {x}")
print(f"A soma dos números digitados é: {soma}")
print(f"A média aritmética dos números digitados é: {soma/x}") 


# 5.15) Solicitar o código do produto e a quantidade comprada. Exibir o total das compras quando o usuário digitar 0. Para código inválido, exibir: "Código inválido."
lista=[1,2,3,5,9]
total_a_pagar=0
while x:
    código = int(input("Digite o código do produto: "))
    if código not in lista:
        print("Código inválido. Digite um código válido [1, 2, 3, 5 ou 9.]")
    else:
        if código == 1:
            preço=0.5
            quantidade = int(input(f"Digite a quantidade comprada do código {código}: "))
        if código == 2:
            preço=1
            quantidade = int(input(f"Digite a quantidade comprada do código {código}: "))
        if código == 3:
            preço=4
            quantidade = int(input(f"Digite a quantidade comprada do código {código}: "))
        if código == 5:
            preço=7
            quantidade = int(input(f"Digite a quantidade comprada do código {código}: "))
        if código == 9:
            preço=8
            quantidade = int(input(f"Digite a quantidade comprada do código {código}: "))
        total_a_pagar=total_a_pagar+(quantidade*preço)
    if código == 0:
        print(f"O total a pagar é: R$ {total_a_pagar:.2f}")
        break 

# Exemplo Programa 5.1) 
valor = int(input("Digite o valor a pagar:"))
cédulas = 0
atual = 50
apagar = valor
while x:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         print("%d cédula(s) de R$%d" % (cédulas, atual))
         if apagar == 0:
               break
         if atual == 50:
               atual = 20
         elif atual == 20:
               atual = 10
         elif atual == 10:
               atual = 5
         elif atual == 5:
               atual = 1
         cédulas = 0 


# 5.16) Execute o Programa 5.1 para os seguintes valores: 501, 745, 384, 2, 7 e 1.

valor = float(input("Digite o valor que quer sacar: R$ "))
cédulas=0
atual_cédula = 50 # Esse atual é a nota que o sistema vai começar a distribuir o dinheiro, no caso a maior nota disponível (R$ 50)
pagar = valor # Esse é o valor que a máquina vai ter que te pagar, conforme foi solicitado em "valor"
while x:
    if atual_cédula<=pagar:
        cédulas += 1
        pagar -= atual_cédula
    else:
        print(f"{cédulas} de R$ {atual:d}")
        if pagar == 0:
            break
        if atual_cédula == 50:
            atual_cédula = 20
        elif atual_cédula == 20:
            atual_cédula = 10
        elif atual_cédula == 10:
            atual_cédula = 5
        elif atual_cédula == 5:
            atual_cédula = 2
        elif atual_cédula == 2:
            atual_cédula = 1
        cédulas = 0 


# 5.17) O que acontece se digitarmos 0 no valor a pagar?

valor = float(input("Digite o valor que quer sacar: R$ "))
if valor == 0:
    print("Valor incoerente. Tente novamente")
cédulas=0
atual_cédula = 50 # Esse atual é a nota que o sistema vai começar a distribuir o dinheiro, no caso a maior nota disponível (R$ 50)
pagar = valor # Esse é o valor que a máquina vai ter que te pagar, conforme foi solicitado em "valor"
while x:
    if atual_cédula<=pagar:
        cédulas += 1
        pagar -= atual_cédula
    else:
        print(f"{cédulas} de R$ {atual_cédula:d}")
        if pagar == 0:
            break
        if atual_cédula == 50:
            atual_cédula = 20
        elif atual_cédula == 20:
            atual_cédula = 10
        elif atual_cédula == 10:
            atual_cédula = 5
        elif atual_cédula == 5:
            atual_cédula = 2
        elif atual_cédula == 2:
            atual_cédula = 1
        cédulas = 0 

        # Resposta: Programei para aparecer um erro e tentar novamente. (provavelmente a pessoa teria de colocar o cartão e senha novamente no caixa eletrônico.)


# 5.18) Modifique o programa para também trabalhar com notas de R$ 100.

valor = float(input("Digite o valor que quer sacar: R$ "))
if valor == 0:
    print("Valor incoerente. Tente novamente")
cédulas=0
atual_cédula = 100 # Esse atual é a nota que o sistema vai começar a distribuir o dinheiro, no caso a maior nota disponível (R$ 50)
pagar = valor # Esse é o valor que a máquina vai ter que te pagar, conforme foi solicitado em "valor"
while x:
    if atual_cédula<=pagar:
        cédulas += 1
        pagar -= atual_cédula
    else:
        print(f"{cédulas} de R$ {atual_cédula:d}")
        if pagar == 0:
            break
        if atual_cédula == 100:
            atual_cédula = 50
        elif atual_cédula == 50:
            atual_cédula = 20
        elif atual_cédula == 20:
            atual_cédula = 10
        elif atual_cédula == 10:
            atual_cédula = 5
        elif atual_cédula == 5:
            atual_cédula = 2
        elif atual_cédula == 2:
            atual_cédula = 1
        cédulas = 0 


# 5.19) Modifique o programa para aceitar valores decimais (moedas) de 0.01, 0.02, 0.05, 0.10 e 0.50

valor = float(input("Digite o valor que quer sacar: R$ "))
if valor == 0:
    print("Valor incoerente. Tente novamente")
cédulas=0
atual = 100 # Esse atual é a nota que o sistema vai começar a distribuir o dinheiro, no caso a maior nota disponível (R$ 50)
pagar = valor # Esse é o valor que a máquina vai ter que te pagar, conforme foi solicitado em "valor"
while x:
    if atual<=pagar:
        pagar -= atual
        cédulas += 1
    else:
        if atual>=1:
            print(f"{cédulas} nota(s) de R$ {atual}")
        else:
            print(f"{cédulas} moeda(s) de {atual} centavo(s)")
        if pagar < 0.01:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cédulas = 0 


# 5.20) O que acontece se digitarmos 0.001 no programa anterior? Caso não funcione, altere-o de forma a corrigir o problema.

valor = float(input("Digite o valor que quer sacar: R$ "))
cédulas=0
atual = 100 # Esse atual é a nota que o sistema vai começar a distribuir o dinheiro, no caso a maior nota disponível (R$ 50)
pagar = valor # Esse é o valor que a máquina vai ter que te pagar, conforme foi solicitado em "valor"
while x:
    if valor<0.01:
        print("Valor indisponível. Tente novamente")
        break
    if atual<=pagar:
        pagar -= atual
        cédulas += 1
    else:
        if atual>=1:
            print(f"{cédulas} nota(s) de R$ {atual}")
        else:
            print(f"{cédulas} moeda(s) de {atual} centavo(s)")
        if pagar < 0.01:
            break
        elif atual == 100:
            atual = 50
        elif atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 2
        elif atual == 2:
            atual = 1
        elif atual == 1:
            atual = 0.50
        elif atual == 0.50:
            atual = 0.10
        elif atual == 0.10:
            atual = 0.05
        elif atual == 0.05:
            atual = 0.02
        elif atual == 0.02:
            atual = 0.01
        cédulas = 0 

# Resposta: o programa parava. Ajustei para aparecer a mensagem "Valor indisponível. Tente novamente" toda vez que o valor < 0.01 (que é a menor moeda disponível).

# Exemplo para + de 1 while:

tabuada = 1
while tabuada <=10:
    número = 1
    while número <=10:
        print(f"{tabuada} x {número} = {tabuada*número}")
        número +=1
    tabuada +=1 

# O mesmo exemplo do de cima, só que sem usar repetições aninhadas.

tabuada = 1
número = 1
while tabuada <=10:
    print(f"{tabuada} x {número} = {tabuada*número}")
    número += 1
    if número == 11:
        número = 1
        tabuada += 1 

# 5.21) Reescreva o Programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas.
while x:
    valor = int(input("Digite o valor a pagar:"))
    if valor == 0:
        break
print("Valor não faz sentido.")
cédulas = 0
atual = 50
apagar = valor
while x:
     if atual <= apagar:
         apagar -= atual
         cédulas += 1
     else:
         print("%d cédula(s) de R$%d" % (cédulas, atual))
         if apagar == 0:
               break
         if atual == 50:
               atual = 20
         elif atual == 20:
               atual = 10
         elif atual == 10:
               atual = 5
         elif atual == 5:
               atual = 1
         cédulas = 0 


# 5.22) Escreva um programa que exiba uma lista de opções: Adição, subtração, divisão, multiplicação e sair. Exiba a tabuada da operação[x] escolhida. Repita até escolher "sair".

print("Olá! Hoje irei te ajudar com tabuada. escolha uma das opções:")
opção = int(input("(1) Soma, (2) Subtração, (3) Divisão, (4) Multiplicação, (5) Sair: "))
if opção == 1:
    número1 = 1
    tabuada = 1
    while tabuada<=10:
        print(f"{número1} + {tabuada} = {número1+tabuada}")
        número1 += 1
        if número1 == 11:
            número1 = 1
            tabuada += 1
elif opção == 2:
    número1 = 1
    tabuada = 1
    while tabuada<=10:
        print(f"{número1} - {tabuada} = {número1-tabuada}")
        número1 += 1
        if número1 == 11:
            número1 = 1
            tabuada += 1
elif opção == 3:
    número1 = 1
    tabuada = 1
    while tabuada<=10:
        print(f"{número1} / {tabuada} = {número1/tabuada:.2f}")
        número1 += 1
        if número1 == 11:
            número1 = 1
            tabuada += 1
elif opção == 4:
    número1 = 1
    tabuada = 1
    while tabuada<=10:
        print(f"{número1} * {tabuada} = {número1*tabuada}")
        número1 += 1
        if número1 == 11:
            número1 = 1
            tabuada += 1
while x:
    opção == 5
    print("Você digitou (5) Sair.")
    break 


# 5.23) Leia um número e verifique se é ou não um número primo. Calcule o resto da divisão por 2 e depois por todos os números ímpares até o número lido. Se o resto da divisão 
#       for igual a zero, o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.

print("Olá, vamos verificar se o número que você digitar é ou não um número primo")
número = int(input("Digite um número inteiro: "))
n = 1
while n <= número:
    x = número % 2
    x = número % (n+2)
    n +=2
if x == 0:
    print("O número não é primo.")
else:
    print("O número é primo.") 


# 5.24) Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

print("Olá, vamos verificar quantos e quais números primos existem até o número que você digitar.")
n = int(input("Digite um número inteiro: "))
if n >= 1:
        print("2")
        p = 1
        y = 3
        while p < n:
            x = 3
            while(x < y):
                if y % x == 0:
                    break
                x = x + 2
            if x == y:
                print(x)
                p = p + 1
            y = y + 2
            if y > n:
                break 


# 5.25) Calcule a raiz quadrada de um número. Utilize o método de Newton para obter um resultado aproximado. Sendo "n" o número a obter a raiz, considere b=2. Calcule "p" usando
#       a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule "p" usando a fórmula apresentada. Pare quando a diferença absoluta entre "n" e 
#       o quadrado de "p" for menor que 0.0001

b=2
n=float(input("Digite um número: "))
p=(b+(n/b))/2
quadradoP=p**2
while abs(n-(b**2))>0.0001:
    p=(b+(n/b))/2
    b=p
print(f"A raiz quadrada de {n:f} é aproximadamente {p:f}") 
# a função "abs" retira o sinal de Digitequer número. É como se colocasse o número em módulo.


# 5.26) Escreva um programa que calcule o resto da divisão inteira de 2 números. Utilize apenas as operações de soma e subtração para calcular o resultado.

a=float(input("Escreva o primeiro número: "))
b=float(input("Escreva o segundo número: "))
while a-b>0:
    r=a-b
    a=r
else: 
    print(f"o resto da divisão é: {r}") 
    
    
#5.27) Escreva um programa que verifique se um número é palídromo. Um número é palíndromo se continua o mesmo caso seus dígitos sejam invertidos. Ex: 454.10501
n=(input("Digite um número inteiro: "))
m=((n)[::-1])
if n==m:
    print(f"O número {n} é palíndromo.")
else:
    print(f"O número {n} NÃO é palíndromo.") 
    