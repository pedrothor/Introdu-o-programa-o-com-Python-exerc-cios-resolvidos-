# 8.1) Escreva uma função que retorne o maior de dois números.

a=int(input("Digite o 1º número: "))
b=int(input("Digite o 2º número: "))
def maior_ou_menor(a,b):
    if a>b:
        return "O primeiro número é maior."
    else:
        return "O segundo número é maior."
print(maior_ou_menor(a,b))


# 8.2) Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.

a=int(input("Digite o 1º número: "))
b=int(input("Digite o 2º número: "))
def émúltiplo(a,b):
    if a%b==0:
        return "True"
    else:
        return "False"
print(émúltiplo(a,b))


# 8.3) Escreva uma função que receba o lado de uma quadrado e retorne sua área (A=lado²)

a=float(input("Digite a medida do lado do quadrado: "))
def área_quadrado(a):
    b=a**2
    return b
print(f"A área do quadrado é: {área_quadrado(a)}")


# 8.4) Escreva uma função que receba a base e a altura de um triângulo e retorne sua área (A=(base x altura)/2)

b=float(input("Digite o valor da base do triângulo: "))
a=float(input("Digite o valor da altura do triângulo: "))
def área_triângulo(a,b):
    area=(b*a)/2
    return area
print(f"A área do triângulo é: {área_triângulo(a,b)}")


# Programa 8.1:
def pesquise(lista,valor):
    for x, e in lista:
        if e==valor:
            return x
    return None
L=[10,20,25,30]
print(pesquise(L,25))
print(pesquise(L,27))

# 8.5) Reescreva a função do Programa 8.1 de forma a utilizar os métodos de pesquisa em lista, vistos no Capítulo 7.
valor=int(input("Digite o valor que deseja pesquisar: "))
L=[10,15,20,23,37,45,59]
def pesquise(L,valor):
    if valor in L:
        return L.index(valor)
    return None
print(pesquise(L,valor))


# Programa 8.2:
def soma(L):
    total=0
    x=0
    while x<5:
        total+=L[x]
        x+=1
    return total
L=[1,7,2,9,15]
print(soma(L))
print(soma([7,9,12,3,100,20,4]))


# 8.6) Reescreva o Programa 8.2 de forma a utilizar for em vez de while.

def soma(L):
    total=0
    for e in L:
        total+=e
    return total
L=[10,27,35,65,42,14,13]
print(soma(L))


# 8.7) Defina uma função mdc recursiva que calcule o maior divisor comum (M.D.C) entre dois números a e b, em que a>b.

a=int(input("Digite o 1º número: "))
b=int(input("Digite o 2º número: "))
def mdc(a,b):
    if b==0:
        return a
    return mdc(b,a%b)
print(f"MDC de {a} e {b} é {mdc(a,b)}")


# 8.8) Usando a função mdc definida no exercício anterior, defina uma função para calcular o menor múltiplo comum (M.M.C) entre dois números.

a=int(input("Digite o 1º número: "))
b=int(input("Digite o 2º número: "))
def mdc(a,b):
    if b==0:
        return a
    return mdc(b,a%b)
def mmc(a,b):
    if b==0:
        return a
    return abs(a*b)/mdc(a,b)
print(mmc(a,b))


# 8.9) Rastreie o Programa 8.6 e compare o seu resultado com o apresentado.
# Programa 8.6:
def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n==0 or n==1:
        return 1
    else:
        fat=n*fatorial(n-1)
        print(f"Fatorial de {n} = {fat}")
    return fat
fatorial(4)

# 1ª rodada:
#calculando fatorial de 4
fat=4*fatorial(3)
# 2º rodada:
#calculando fatorial de 3
fat=3*fatorial(2)
# 3º rodada:
#calculando fatorial de 2
fat=2*1
# linhas:
# 1º Fatorial de 2=2
# 2º Fatorial de 3=6
# 3º Fatorial de 4=24


# 8.10) Reescreva a função para o cálculo da sequência de Fibonacci, sem utilizar recursão.
    
def fibonacci(n):
    x=0
    p=1
    while n>0:
        x,p=p,x+p
        n-=1
    return x
for y in range(11):
    print(f"Fibonacci({y})={fibonacci(y)}")
    
    
# 8.11) Escreva uma função para validar uma variável string. Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres. Retorne Verdadeiro
#       se o tamanho da string estiver entre os valores de máximo e mínimo, e Falso, caso contrário.
string=input("Escreva uma palavra: ")
máximo=6
mínimo=1
def tamanho(string,máximo,mínimo):
    if len(string)>máximo or len(string)<mínimo:
        return "Falso"
    else:
        return "Verdadeiro"
print(tamanho(string,máximo,mínimo))


# 8.12) Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista,
#       também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.

string=input("Escreva uma palavra que deseja pesquisar: ")
lista=["banana","maçã","nescau","chico","mariana","thor","natal"]
def procurar(string,lista):
        if string in lista:
            return "Verdadeiro"
        else:
            return "Falso"
print(procurar(string,lista))


# 8.13) Escreva uma função que receba uma string com as opções válidas a aceitar (cada opção é uma letra). Converta as opções válidas
#       para letras minúsculas. Utilize input para ler uma opção, converter o valor para letras minúsculas e verificar se a opção
#       é válida. Em caso de opção inválida, a função deve pedir ao usuário que digite novamente outra opção.

print("\n\na) Trânsito, Comida, Neve\nb) Cabelo, Tênis, Judô\nc) Maquete, Torta, Viagem")
a=["Trânsito","Comida","Neve"]
b=["Cabelo","Tênis","Judô"]
c=["Maquete","Torta","Viagem"]
opções=["a","b","c"]
", ".join(a).lower()
", ".join(b).lower()
", ".join(c).lower()
def escolhida(opções):
    while True:
        opção=input("\nEscolha uma das opções acima: ")
        if opção not in opções:
            print("\nPor favor, digite uma opção válida.")
        else:
            return "\nOpção válida. Muito obrigado!"
print(escolhida(opções))


#   Programa 8.20 - Adivinhando o número
import random
n=random.randint(1,10)
x=int(input("Escolha um número entre 1 e 10: "))
if x==n:
    print("Você acertou!")
else:
    print("Você errou.")
# No livro, existem 2 exercícios 8.13 (diferentes)
# 8.13) Altere o Programa 8.20 de forma que o usuário tenha três chances de acertar o número. O programa termina se o usuário acertar ou errar três vezes.

import random
for tentativa in range(3):
    n=random.randint(1,10)
    x=int(input("Escolha um número entre 1 e 10: "))
    if x==n:
        print("Você acertou!")
        break
    else:
        print("Você errou.")
    print(f"Tentativa {tentativa+1}")
    
    
#   Programa 7.2 - jogo da forca
palavra=input("Digite a palavra secreta: ").lower().strip()
for x in range(100):
    print()
digitadas=[]
acertos=[]
erros=0
while True:
    senha=""
    for letra in palavra:
        senha+=letra if letra in acertos else "."
    print(senha)
    if senha==palavra:
        print("Você acertou!")
        break
    tentativa=input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas+=tentativa
        if tentativa in palavra:
            acertos+=tentativa
        else:
            erros+=1
            print("Você errou.")
        print("X===:===\nX   :  ")
        print("X   0  "if erros>=1 else "X")
        linha2=""
        if erros==2:
            linha2="  |  "
        elif erros==3:
            linha2="  \|  "
        elif erros>=4:
            linha2="  \|/  "
        print(f"X{linha2}")
        linha3=""
        if erros==5:
            linha3+="  /  "
        elif erros>=6:
            linha3+="  / \ "
        print(f"X{linha3}")
        print("X\n===========")
        if erros ==6:
            print("Enforcado!")
            break

# 8.4) Altere o Programa 7.2, o jogo da forca. Escolha a palavra a adivinhar utilizando números aleatórios.

palavras = ["cabelo","inter","chico","cachorro","leoa"]
import random
n=random.randint(0,4)
palavra=palavras[n].lower().strip()
for x in range(100):
    print()
digitadas=[]
acertos=[]
erros=0
while True:
    senha=""
    for letra in palavra:
        senha+=letra if letra in acertos else "."
    print(senha)
    if senha==palavra:
        print("Você acertou!")
        break
    tentativa=input("\nDigite uma letra: ").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas+=tentativa
        if tentativa in palavra:
            acertos+=tentativa
        else:
            erros+=1
            print("Você errou.")
        print("X===:===\nX   :  ")
        print("X   0  "if erros>=1 else "X")
        linha2=""
        if erros==2:
            linha2="  |  "
        elif erros==3:
            linha2="  \|  "
        elif erros>=4:
            linha2="  \|/  "
        print(f"X{linha2}")
        linha3=""
        if erros==5:
            linha3+="  /  "
        elif erros>=6:
            linha3+="  / \ "
        print(f"X{linha3}")
        print("X\n===========")
        if erros ==6:
            print("Enforcado!")
            break
            
            
# 8.15) Utilizando a função type, escreva uma função recursiva que imprima os elementos de uma lista. Cada elemento deve ser impresso separadamento, um por linha.
#       Considere o caso de listas dentro de listas, como L=[1,[2,3,4[5,6,7]]]. A cada nível, imprima a lista mais à direita, como fazemos ao indentar blocos em Python.
#       Dica: envie o nível atual como parâmetro e utilize-o para calcular a quantidade de espaços em branco à esquerda de cada elemento.

espaços_nivel=4
L = [1, [2, 3, 4, [5, 6, 7]]]
def imprime_elementos(l, nivel=0):
    espacos = ' '*espaços_nivel*nivel
    if type(l) == list:
        print(espacos,"[")
        for e in l:
            imprime_elementos(e,nivel + 1)
        print(espacos,"]")
    else:
        print(espacos,l)
imprime_elementos(L)


# 8.16) Escreva um generator capaz de gerar a série dos números primos
#       Neste caso, irei determinar um limite para a série de números primos.


def números_primos(x):
    a=1 #vamos começar com o número 1, já que o 0 não é primo.
    yield 2 #é o único número par que é primo, retornamos ele.
    b=3 #o número que será verificado se é primo ou não (dividendo).
    c=3 #vamos começar a dividir por 3, já que se for por 2, o número será par.
    while a<x: #limite para parar com o looping
        if b%c==0:
            if c==b:
                yield c
                a+=1
            b+=2 #somamos 2 pois se somássemos "1", o próximo número seria par, e o único número primo que é par é o 2.
            c=3 #ainda mantendo a divisão por 3
        elif b<c:
            b+=2 #caso o número ímpar seja menor que o seu divisor (o que daria número decimal), somamos 2 para pularmos para o próximo número ímpar.
        else:
            c+=2 #incrementamos o divisor para começar a testar outros (ímpares).
for primo in números_primos(15):
    print(primo, end=" ")
    
    
# 8.17) Escreva um generator capaz de gerar a série Fibannoci.0,1,1,2,3,5,8


def finabocci(n):
    x=0
    y=1
    while n>0:
        yield x
        x,y=y,x+y # x=y (pulando para o próximo valor de x.), y=x+y (o próximo valor é a soma dos 2 atuais).
        n-=1 # diminui o finabocci, para que chegue até finabocci(1).
for f in finabocci(10): #um exemplo para finabocci(10),
    print(f, end=" ") # end=" " para que os valores sejam impressos separados e na mesma linha
    

    

