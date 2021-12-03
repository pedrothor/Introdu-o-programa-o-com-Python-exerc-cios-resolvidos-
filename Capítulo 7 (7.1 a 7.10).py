# Programa 7.1 - pesquisa de todas as ocorrências.
"""s="um tigre, dois tigres, três tigres"
p=0
while(p>-1):
    p=s.find("tigre",p)
    if p>=0:
        print(f"Posição: {p}")
        p+=1"""
        
        
# 7.1) Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
#      1ª string: AABBEFAAT
#      2ª string: BE
# Resultado: BE encontrado na posição 3 de AABBEFAATT

s1="AABBEFTAATT"
s2="BE"
contador=0
while contador>-1:
    contador=s1.find(s2,contador)
    if contador>-1:
        print(f"Posição: {contador}")
        contador+=1
        
        
# 7.2) Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
#      1ª string = AAACTBF
#      2ª string = CBT
# Resultado: CBT

s1="AAACTBF"
s2="CBT"
s3=""
s1_set=set(s1)
s2_set=set(s2)
s3_set=set(s3)
x=0
while x<len(s2_set):
    if s2_set[x] in s1_set:
        s3_set.append(s2_set[x])
        x+=1
        s3=", ".join(s3_set)
        print(s3)
        
        
# 7.3) Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
#      1ª string: CTA
#      2ª string: ABC
# Resultado = 3ª string: BT
# A ordem dos caracteres da 3ª string não é importante.

s1="CTA"
s2="ABC"
s3=""
for letra in s1:
    if letra not in s2:
        s3+=letra
for letra in s2:
    if letra not in s1:
        s3+=letra
print(s3)
    
    
# 7.4) Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string
#      string: TTAAC
# Resultado: T:2x       A:2x        C:1x

s="TTAAC"
s_set=set(s)
x={}
repetição=1
for letra in s:
    if letra in x:
        x[letra]+=1
    else:
        x[letra]=1
print(x)


# 7.5) Escreva um programa que leia 2 strings e gere uma terceira, na qual os caracteres da segunda foram retirados pelos da primeira.
#      1ª string: AATTGGAA
#      2ª string: TG
# Resultado = 3ª string: AAAA

s1="AATTGGAA"
s2="TG"
s3=""
for letra in s1:
    if letra not in s2:
        s3+=letra
print(s3)


# 7.6) Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda 
#      pelos da terceira.
#      1ª string: AATTCGAA
#      2ª string: TG
#      3ª string: AC
# Resultado: AAAACCAA

s1="AATTCGAA"
s2="TG"
s3="AC"
s4="" #s4 vai ser a string gerada após a substituição
if len(s2)==len(s3):
    s4=""
    for letra in s1:
        posição=s2.find(letra)
        if posição!=-1:
            s4+=s3[posição]
        else:
            s4+=letra
    print(f"{s2[0]} e {s2[1]} foram substituídos por {s3[0]} e {s3[1]}, respectivamente, em {s1}. s4 = {s4}")
else:
    print("A segunda e a terceira string devem ter o mesmo tamanho")
    
    
#Programa 7.2 - Jogo da forca
"""palavra=input("Digite a palavra secreta: ").lower().strip()
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
            break"""
            
            
# 7.7) Moifique o jogo da forca (Programa 7.2) de forma a escrever a palavra secreta caso o jogador perca.

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
            print(f"A palavra correta é: {palavra}")
            break
            
            
# 7.8) Modifique o Programa 7.2 de forma a utilizar uma lista de palavras. No início, pergunte um número e calcule o índice da
#      palavra a utilizar pela fórmula: índice=(número*776) % len(lista_de_palavras)

palavras="chico","mariana","thor","cachorro","papagaio","alicate","comida","dormir","pão"
lista_de_palavras=list(palavras)
número=int(input("Digite um número: "))
índice=(número*776)%len(lista_de_palavras)
palavra=palavras[índice].lower().strip()
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
            print(f"A palavra correta é: {palavra}")
            break
            
            
# 7.9) Modifique o Programa 7.2 para utiizar listas de strings para desenhar o boneco da forca. Você pode utilizar uma lista para
#      linha e organizá-las em uma lista de listas. Em vez de controlar quando imprimir cada parte, desenhe nessas listas, 
#      substituindo o elemento a desenhar.

"""Exemplo:
linha=list("X------")
linha[6]="|"
linha="".join(linha)
print(linha)"""

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
        linha2=list("X------")
        if erros==2:
            linha2[2]="|"
        elif erros==3:
            linha2[2]="\|"
        elif erros>=4:
            linha2[2]="\|/ "
        linha2="".join(linha2)
        print(f"X{linha2}")
        linha3=list("X------")
        if erros==5:
            linha3[2]="/"
        elif erros>=6:
            linha3[2]="/ \ "
        linha3="".join(linha3)
        print(f"X{linha3}")
        print("X\n===========")
        if erros ==6:
            print("Enforcado!")
            break
            
            
# 7.10) Escreva um jogo da velha para dois jogadores. O jogo deve perguntar onde você quer jogar e alternar entre os jogadores.
#       A cada jogada, verifique se a posição está livre. Verifique também quando um jogador venceu a partida. Um jogo da velha pode 
#       ser visto como uma lista de 3 elementos, na qual cada elemento é outra lista. Também com 3 elementos.

"""Exemplo de jogo

X | O |  
  | X | X
  |   | O 
  
Em que cada posição pode ser vista como um número. Confira a seguir um exemplo das posições mapeadas para a mesma posição
De seu teclado numérico.
  
1 | 2 | 3 
4 | 5 | 6
7 | 8 | 9 

"""
print("jogador 1 = X")
print("jogador 2 = O")
velha="| | | |\n| | | |\n| | | |"
print("Olá! Vamos jogar jogo da velha? Abaixo está as posições das casas que você pode jogar!\n|1|2|3|\n|4|5|6|\n|7|8|9| ")
tabuleiro=list(velha)
jogadas=0
jogando=True
while True:
    if jogadas==9:
        print("Deu velha! Ninguém ganhou.")
        break
    jogada1=int(input("Jogador 1 - Digite qual casa você quer jogar: "))
    jogada2=int(input("Jogador 2 - Digite qual casa você quer jogar: "))
    #if tabuleiro[linha]
    if jogada1<1 or jogada1>9 or jogada2<1 or jogada2>9:
        print("Essa casa não existe!")
        continue 
    if jogada1==1:
        if tabuleiro[1]==" ":
            tabuleiro[1]="X"
        else:
            print("Casa já ocupada!")
    elif jogada1==2:
        if tabuleiro[3]==" ":
            tabuleiro[3]="X"
        else:
            print("Casa já ocupada!")
    elif jogada1==3:
        if tabuleiro[5]==" ":
            tabuleiro[5]="X"
        else:
            print("Casa já ocupada!")
    elif jogada1==4:
        if tabuleiro[9]==" ":
            tabuleiro[9]="X"
        else:
            print("Casa já ocupada!")
    elif jogada1==5:
        if tabuleiro[11]==" ":
            tabuleiro[11]="X"
        else:
            print("Casa já ocupada!")
    elif jogada1==6:
        if tabuleiro[13]==" ":
            tabuleiro[13]="X" 
        else:
            print("Casa já ocupada!")
    elif jogada1==7:
        if tabuleiro[17]==" ":
            tabuleiro[17]="X"
        else:
            print("Casa já ocupada!")
    elif jogada1==8:
        if tabuleiro[19]==" ":
            tabuleiro[19]="X"
        else:
            print("Casa já ocupada!")
    elif jogada1==9:
        if tabuleiro[21]==" ":
            tabuleiro[21]="X"
        else:
            print("Casa já ocupada!")
    if tabuleiro[1]=="X" and tabuleiro[3]=="X" and tabuleiro[5]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if tabuleiro[9]=="X" and tabuleiro[11]=="X" and tabuleiro[13]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if tabuleiro[17]=="X" and tabuleiro[19]=="X" and tabuleiro[21]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if tabuleiro[1]=="X" and tabuleiro[9]=="X" and tabuleiro[17]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if tabuleiro[3]=="X" and tabuleiro[11]=="X" and tabuleiro[19]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if tabuleiro[5]=="X" and tabuleiro[13]=="X" and tabuleiro[21]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if tabuleiro[1]=="X" and tabuleiro[11]=="X" and tabuleiro[21]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if tabuleiro[5]=="X" and tabuleiro[11]=="X" and tabuleiro[17]=="X":
        print("O Jogador 1 venceu!")
        jogando=False
        break
    if jogada2==1:
        if tabuleiro[1]==" ":
            tabuleiro[1]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==2:
        if tabuleiro[3]==" ":
            tabuleiro[3]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==3: 
        if tabuleiro[5]==" ":
            tabuleiro[5]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==4:
        if tabuleiro[9]==" ":
            tabuleiro[9]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==5:
        if tabuleiro[11]==" ":
            tabuleiro[11]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==6:
        if tabuleiro[13]==" ":
            tabuleiro[13]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==7:
        if tabuleiro[17]==" ":
            tabuleiro[17]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==8:
        if tabuleiro[19]==" ":
            tabuleiro[19]="O"
        else:
            print("Casa já ocupada!")
    elif jogada2==9:
        if tabuleiro[21]==" ":
            tabuleiro[21]="O"
        else:
            print("Casa já ocupada!")
    if tabuleiro[1]=="O" and tabuleiro[3]=="O" and tabuleiro[5]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    if tabuleiro[9]=="O" and tabuleiro[11]=="O" and tabuleiro[13]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    if tabuleiro[17]=="O" and tabuleiro[19]=="O" and tabuleiro[21]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    if tabuleiro[1]=="O" and tabuleiro[9]=="O" and tabuleiro[17]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    if tabuleiro[3]=="O" and tabuleiro[11]=="O" and tabuleiro[19]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    if tabuleiro[5]=="O" and tabuleiro[13]=="O" and tabuleiro[21]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    if tabuleiro[1]=="O" and tabuleiro[11]=="O" and tabuleiro[21]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    if tabuleiro[5]=="O" and tabuleiro[11]=="O" and tabuleiro[17]=="O":
        print("O Jogador 2 venceu!")
        jogando=False
        break
    print("".join(tabuleiro))
    jogadas+=1
        


