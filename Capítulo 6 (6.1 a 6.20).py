
#6.1) Modifique o programa 6.2 para ler 7 notas ao invés de apenas 5.

notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x<7:
    notas[x]=float(input(f" Digite a nota do {x}° elemento:"))
    soma +=notas[x]
    x+=1
print(f"Média: {soma/x:.2f}") 


#6.2) Faça um programa que leia 2 listas e que gere uma terceira lista com os elementos das duas primeiras.

A=[]
x=0
while x<3:
    númeroA=int(input(f"Digite o {x+1}° elemento de A:"))
    x+=1
    A.append(númeroA)
B=[]
x=0
while x<3:
    númeroB=int(input(f"Digite o {x+1}° elemento de B:"))
    x+=1
    B.append(númeroB)
C=[]
C.extend(A)
C.extend(B)
print(f"O conjunto A é: {A}")
print(f"O conjunto B é: {B}")
print(f"O conjunto C é: {C}") 


#6.3) Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
A=[]
B=[]
while x:
    e=int(input("Digite um valor para a lista A (0 para terminar):"))
    if e==0:
        break
    A.append(e)
while x:
    e=int(input("Digite um valor para a lista B (0 para terminar):"))
    if e==0:
        break
    B.append(e)
C=[]
duas_listas=A[:]
duas_listas.extend(B)
x=0
while x<len(duas_listas):
    y=0
    while y<len(C):
        if duas_listas[x]==C[y]:
            break
        y+=1
    if y==len(C):
        C.append(duas_listas[x])
    x+=1
x=0
while x<len(C):
    x+=1
print(f"C={C}") 


#6.4) O que acontece quando não verificamos se a lista está vazia antes de chamarmos o método pop?
# R: Se a lista estiver vazia, ele não irá puxar ninguém e uma mensagem aparecerá na tela informando que a pilha está va
# zia.


#6.5) Altere o programa 6.7 de forma a poder travalhar com vários comandos digitados de uma só vez. Atualmente, apenas um comando
#     pode ser inserido por vez. Altere-o de forma a considerar operação[x] como uma string.

"""programa 6.7:
último=10
pilha=list(range(1,último+1))
while True:
        print(f"\nExistem {len(pilha)} clientes na pilha")     
        print(f"Fila atual: {pilha}")    
        print("Digite F para adiocionar um cliente ao fim da pilha")     
        print("ou A para realizar o atendimento. S para sair.")
        operação=input("operação(F, A ou S)")
        if operação == "A" or operação == "a":
            if len(pilha)>0:
                atendido=pilha.pop(0)
                print(f"Cliente {atendido} em atendimento.")
            else:
                print("Fila vazia. Não há ninguém para atender.")
        elif operação == "F" or operação == "f":
            último+=1 #Incrementa o ticket do novo cliente na pilha
            pilha.append(último)
        elif operação == "S" or operação == "s":
            break
        else:
            print("Comando inexistente. Digite apenas A, F ou S")"""


último=10
pilha=list(range(1,último+1))
x=0
while True:
    print(f"\nExistem {len(pilha)} clientes na pilha")
    print(f"Fila atual: {pilha}")
    print("Digite F para adicionar um cliente ao fim da pilha")
    print("A para realizar o atendimento.")
    print("S para sair.")
    operação=input("O que deseja fazer? (F, A ou S):")
    x=0
    sair = False
    while x<len(operação):
        if operação[x][x]=="A" or operação[x][x]=="a":
            if len(pilha)>0:
                atendido=pilha.pop(0)
                print(f"Cliente {atendido} em atendimento.")
            else:
                print("Fila vazia. Não há ninguém para atender.")
        elif operação[x][x]=="F" or operação[x][x] == "f":
            último+=1 #Incrementa o ticket do novo cliente na pilha
       
            pilha.append(
                último)
        elif operação[x] [x]=="S" or operação[x][x]=="s":
            sair=x
            break
        else:
            print("\nComando inexistente. Digite apenas A, F ou S")
        x+=1
    if sair:
        break
        
        
# 6.6) Modifique o programa para trabalhar com duas filas. Para facilitar seu trabalho, considere o comando A para atendimento da pilha 1; B pa
# ra atendimento da pilha 2.
#   
#    O mesmo para a chegada de clientes: F para pilha 1, G pa
# ra pilha 2.


último1=10
último2=10
fila1=list(range(1,último1+1))
fila2=list(range(1,último2+1))
while x:
    print(f"Fila 1: {fila1}")
    print(f"Fila 2: {fila2}")
    print("Digite 'F' para adicionar paciente na pilha 1.\n   'A' para chamar paciente na pilha 1.")
  
    print("Digite 'G' para adicionar na pilha 2.\n   'B' para chamar na pilha 2.")
  
    print("'S' para sair.")
    operação[x]=input("Digite operação[x] deseja fazer?")
    x=0
    sair = False
    while x<len(operação[x]):
        if operação[x][x]=="A" or operação[x][x]=="a":
            if len(fila1)>0:
                atendido=fila1.pop(0)
            else:
                print("Não há mais ninguém na pilha 1.")
  
        elif operação[x][x] =="B" or operação[x][x]=="b":
            if len(fila2)>0:
                atendido=fila2.pop(0)
            else:
                print("Não há mais ninguém na pilha 2.")
  
        elif operação[x] [x]=="F" or operação[x][x]=="f":
            último1+=1
            fila1.append(último1)
        elif operação[x] [x]=="G" or operação[x] [x]=="g":
            último2+=1
            fila2.append(último2)
        elif operação[x] [x]== "S" or operação[x] [x]== "s":
            sair=x
            break
        
        else:
            print("Comando inexistente. Digite apenas 'A', 'B', 'F' ou 'G'")
            print("'S' sair")
        x+=1
    if sair:
        break 
        
        
# Um exemplo de sistema para adicionar e retirar pratos:
último_prato=10
pilha=(list(range(1,último_prato+1)))
while x:
    print("Digite 'A' para adicionar um prato.\n       'B' para retirar um prato.\n       'S' para sair.")
    print(f"Existem {len(pilha)} pratos na pilha.")
    print(f"Elementos da pilha = {pilha}")
    operação=input("\nO que deseja fazer? (A ou B): ")
    x=0
    sair=False
    while x<len(operação):
        if operação[x] == "B" or operação[x] == "b":
            if len(pilha)>0:
                lavado=pilha.pop(-1)
                print(f"\n{lavado}° prato lavado.")
            else:
                print("\nPilha vazia! Não há nenhum prato para lavar!")
        elif operação[x] == "A" or operação[x] == "a":
            último_prato+=1
            pilha.append(último_prato)
        elif operação[x] == "S" or operação[x] == "s":
            sair=x
            break
        else:
            print("\nOperação inválida! Digite apenas 'A', 'B' ou 'S'.")
        x+=1
    if sair:
        break 

#   -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   

# 6.7) Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parênteses foram abertos e fechados na ordem correta. Exemplo:
#       (())       OK
#       ()()(()()) OK
#       ())        Erro

#      Você pode adicionar elementos à pilha sempre que encontrar abre parênteses e desempilhá-la a cada fecha parênteses. Ao desempilhar, verifique se o topo da pilha é um abre
#      Parênteses. Se a expressão estiver correta, sua pilha estará varia no final.


pilha=[]
print("Olá! Hoje irei te ajudar a ler expressões que representam pilha de pratos.")       
expressão=input("Digite a expressão: ")
x=0
while x<len(expressão):
    if expressão[x]=="(":
        pilha.append("(")
    if expressão[x]==")":
        if len(pilha)>0:
            pilha.pop(-1)
    x+=1
if len(pilha)==0:
    print("Todos os pratos foram lavados!")
else:
    print("Há pratos para lavar!") 
    

# Programa 6.9:
L=[15,7,27,39]
p=int(input("Digite o valor que deseja procurar: "))
achou = False
x=0
while x<len(L):
    if L[x]==p:
        achou = x
        break
    x+=1
if achou:
    print(f"{p} achado na posição {x}.")
else:
    print(f"{p} não está na lista.") 
    
    
# 6.8) Modifique o primeiro exemplo (Programa 6.9) de forma a realizar a mesma tarefa, mas sem utilizar a variável "achou".
#      Dica: observe a condição de saída do "while"

L=[15,7,27,39]
p=int(input("Digite o valor que deseja procurar: "))
x=0
while x<len(L):
    if L[x]==p:
        print(f"{p} achado na posição {x}.")
        break
    x+=1
else:
    print(f"{p} não está na lista.") 
    
    
# 6.9) Modifique o exemplo para pesquisar 2 valores ("p" e "v"). Na impressão, indique quais dos dois valores foi achado primeiro.

L = [1,2,3,4,5]
p = int(input("Digite o valor a procurar (p): "))
v = int(input("Digite o outro valor a procurar (v): "))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = x
        if not achouV:
            primeiro = 1
    if L[x] == v:
        achouV = x
        if not achouP:
            primeiro = 2
    x += 1
if achouP:
    print(f"{p} foi encontrado na posição {x}")
else:
    print(f"{p} não foi encontrado")
if achouV:
    print(f"{v} foi encontrado na posição {x}")
else:
    print(f"{v} não foi encontrado")
if primeiro == 1:
    print("'p' foi achado antes de 'v'")
elif primeiro == 2:
    print("'v' foi achado antes de 'p'") 
    
    
# 6.10) Modifique o programa do Exercício 6.9 de forma a pesquisar p e v em toda a lista e informando o usuário a posição onde p e v foram encontrados.

L=[1,2,3,4,5]
p = int(input("Digite o valor a procurar (p): "))
v = int(input("Digite o outro valor a procurar (v): "))
x=0
achouP=False
achouV=False
while x<len(L):
    if L[x]==p:
        achouP=x
    if L[x]==v:
        achouV=x
    x+=1
if achouP:
    print(f"P foi encontrado na posição {achouP}.")
else:
    print("P não foi encontrado.")
if achouV:
    print(f"V foi encontrado na posição {achouV}.")
else:
    print("V não foi encontrado.") 
    
    
# Programa 6.6:
L=[] 
while True:
    n=int(input("Digite um número: "))
    if n==0:
        break
    L.append(n)
x=0
while x<len(L):
    print(L[x])
    x+=1 
    
    
# 6.11) Modifique o Programa 6.6 usando 'for'. Explique por que nem todos os 'while' podem ser transformados em 'for'.
L=[]
p=int(input("Digite um número: "))
L.append(p)
for e in L:
    if e==p:
        print(e)
        break 
# R: nem todos 'while' podem ser transformados em 'for' pois, nesse caso, a lista inicia vazia.


# Programa 6.11:
L=[1,7,2,4]
máximo=L[0]
for e in L:
    if e>máximo:
        máximo=e
print(máximo) 

# 6.12) Altere o Programa 6.11 de forma a imprimir o menor valor da lista.

L=[7,2,4,1]
mínimo=L[0]
for e in L:
    if e<mínimo:
        mínimo=e
print(mínimo) 


# 6.13) A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T=[-10,-8,0,1,2,5,-2,-4]. Faça um programa
#       que imprima a menor e a maior temperatura, assim como a temperatura média.

T=[-10,-8,0,1,2,5,-2,-4]
maior=T[0]
for e in T:
    if e>maior:
        maior=e
print(f"{maior} é a maior temperatura.")   
menor=T[0]
for z in T:
    if z<menor:
        menor=z
print(f"{menor} é a menor temperatura.")
x=0
soma=0
while x<len(T):
    soma=soma+T.pop(0)
    x+=1
temp_média=soma/len(T)
print(f"A temperatura média é: {temp_média}") 


# 6.14) O que acontece quando a lista já está ordenada? Rastreie o Programa 6.20, mas com a lista L=[1,2,3,4,5]

#       R: Se a lista já estiver ordenada, o programa pula direto para a linha "if not trocou". E printa a lista na tela.
L=list(range(1,6))
fim=5
while fim>1:
    trocou=False
    x=0
    while x<(fim-1):
        if L[x]>L[x+1]:
            trocou=True
            y=L[x]
            L[x]=L[x+1]
            L[x+1]=y
        x+=1
    if not trocou:
        break
    fim-=1
for e in L:
    print(e,end=" ") 
    
    
# 6.15) O que acontece quando dois valores são iguais? L=[3,3,1,5,4]

#       R: Eles são repetidos. Mas mesmo assim, são enumerados conforme os outros números.

L=[3,3,1,5,4]
fim=5
while fim>1:
    trocou=False
    x=0
    while x<(fim-1):
        if L[x]>L[x+1]:
            trocou=True
            y=L[x]
            L[x]=L[x+1]
            L[x+1]=y
        x+=1
    if not trocou:
        break
    fim-=1
for e in L:
    print(e,end=" ") 
    
    
# 6.16) Modifique o Programa 6.20 para ordenar a lista em ordem decrescente. L=[1,2,3,4,5] deve ser ordenada como L=[5,4,3,2,1]

L=list(range(1,6))
fim=5
while fim>1:
    trocou=False
    x=0
    while x<(fim-1):
        if L[x]<L[x+1]:
            trocou=True
            y=L[x]
            L[x]=L[x+1]
            L[x+1]=y
        x+=1
    if not trocou:
        break
    fim-=1
for e in L:
    print(e,end=" ") 
    
    
# Programa 6.22
"""estoque={"tomate":[1000,2.30],
         "alface":[500,0.45],
         "batata":[2001,1.20],
         "feijão":[100,1.50]
         }
venda=[["tomate",5],["batata",10],["alface",5]]
total=0
print("Vendas:\n")
for operação in venda:
    produto,quantidade=operação
    preço=estoque[produto][1]
    custo=preço*quantidade
    print(f"{produto}: {quantidade} x {preço:.2f} = {custo:.2f}")
    estoque[produto][0]-=quantidade
    total+=custo
    print(f"Custo total = R$ {total:.2f}\n")
    print(f"Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ",chave)
        print("Quantidade", dados)
        print(f"Preço: {dados[1]:.2f}\n")"""
        
        
# 6.17) Altere o Programa 6.22 para a solicitar ao usuário o produto e a quantidade vendida. Veja se o nome do produto digitado existe no dicionário, só então efetue a baixa.

estoque={"tomate":[1000,2.30],
         "alface":[500,0.45],
         "batata":[2001,1.20],
         "feijão":[100,1.50]
         }
produtovendido=input("Digite o produto que foi vendido , '0' para terminar: ")
while True:
    if produtovendido == "0":
        break
    if produtovendido not in estoque:
        print("Produto não encontrado no estoque!")
        break
    quantidade=int(input("Digite a quantidade do produto vendido: "))
    venda=[["tomate",quantidade],["batata",quantidade],["alface",quantidade], ["feijão",quantidade]]
    total=0
    print("Vendas:\n")
    for operação in venda:
        produto,quantidade=operação
        preço=estoque[produtovendido][1]
        custo=preço*quantidade
        print(f"{produtovendido}: {quantidade} x {preço:.2f} = {custo:.2f}")
        estoque[produtovendido][0]-=quantidade
        total+=custo
        break
    print(f"Vendas totais de {produtovendido} = R$ {total:.2f}\n")
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ",chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:.2f}\n") 
        
        
# 6.18) Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja o número desse caractere encontrando em uma frase lida.
#       Exemplo: O rato -> {"O":1, "r":1, "a":1, "t":1, "o":1}
while True:
    frase=input("Digite uma frase ou uma palavra, '0' para sair: ")
    if frase=="0":
        break
    dicionário={
    }
    for x in frase: # x = caractere da string gerada em "frase"
        if x in dicionário:
            dicionário[x]+=1
        else:
            dicionário[x]=1
    print(dicionário)
    
    
# 6.19) Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
#       - os valores comuns às duas listas
#       - os valores que só existem na primeira
#       - os valores que existem apenas na segunda
#       - uma lista com os elementos não repetidos das duas listas
#       - a primeira lista sem os elementos repetidos na segunda

a=[10,20,30]
b=[20,40,60]
conj_A=set(a)
conj_B=set(b)
x1=conj_A&conj_B
print(x1)
x2=conj_A-conj_B
print(x2)
x3=conj_B-conj_A
print(x3)
c=(conj_A|conj_B)-(conj_A&conj_B)
print(c)
a=conj_A-conj_B
print(a)


# 6.20) Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações. Utilizando operações com
#       Conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
#       - os elementos que não mudaram
#       - os novos elementos
#       - os elementos que foram removidos

L1=["a","b","c"]
L2=["a","d"]
lista1=set(L1)
lista2=set(L2)
não_mudaram=lista1&lista2
novos_elementos=lista2-lista1
elementos_removidos=lista1-lista2
print(f"Elementos que não mudaram = {não_mudaram}")
print(f"Novos elementos = {novos_elementos}")
print(f"Elementos removidos = {elementos_removidos}")