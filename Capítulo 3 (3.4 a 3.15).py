# Os exercícios 3.1 a 3.3 resolvi marcando "x" no próprio livro.


# 3.4) Escreva uma expressão para determinar se uma pessoa paga ou não imposto. Paga imposto se salário>1200

salario=2000
salario>1200 or salario<1200
True


# 3.5) Calcular o resultado de A>B and C or D.
#   A       B       C       D       RESULTADO
#   1       2       True    False    False
#   10      3       False   False    False
#   5       1       True    True     True


# 3.6) Escreva uma expressão para saber se um aluno foi ou não aprovado.
#     aprovado = media > 7
#     media=(materia1 + materia2 + materia3)/3

materia1=5
materia2=9
materia3=8
media = (materia1 + materia2 + materia3)/3
aprovado = media > 7
print(aprovado)
True


#3.7) pedir 2 números inteiros e exibir na tela a soma dos dois.

A=int(input("Digite o valor de A: "))
B=int(input("Digite o valor de B: "))
F= A+B
print(f"A + B = {F}")
   

#3.8) pedir um número em metros e exiba a conversão em milímetros

# C = x metros
# D = C * 1000 milímetros
C = float(input("Digite um número inteiro: "))
D = 1000
E = (C * D)
print(f"{C} equivale a {E} milímetros")


#3.9) escreva um programa que leia a quantidade de dias, horas, minutos e segundos imposta pelo usuário. Calcule o total em segundos.

dia=int(input("Dia(s): "))
hora=int(input("Hora(s): "))
minuto=int(input("Minuto(s): "))
segundo=int(input("Segundo(s): "))
valor_em_segundos=dia*24*3600 + hora*3600 + minuto*60 + segundo
print("Total convertido em segundos equivale a %d segundos." % valor_em_segundos)
                            
                        # ou
print(f"Total convertido em segundos equivale a {valor_em_segundos} segundos.")


#3.10) calcular o aumento de um salário. Solicitar o salário e o aumento. Exibir o valor do aumento e o novo salário.

salário = float(input("Digite o seu salário (somente número): "))
aumento = float(input("Digite a % do aumento (somente número): "))
valor_aumento = salário*aumento/100
print(f"O valor do seu aumento é de R$ {valor_aumento}")
novo_salário = salário + valor_aumento
print(f"Parabéns! O seu novo salário é R$ {novo_salário}")


#3.11) solicitar o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

A = float(input("Informe o preço do produto: "))
print("Que maravilha! Esse produto está com 15% de desconto!")
valor_a_pagar = A - A*15/100
print(f"Valor total a pagar: R$ {valor_a_pagar}")
#obs: o exercício original solicitava ao usuário para colocar a % de desconto. Nesse exercício eu fiz melhor. o usuário não precisa colocar a % de desconto. A máquina já sabe o desconto.


#3.12) Calcular o tempo de uma viagem de carro. Pergunte a distância e velocidade média esperada para viagem.

print("Olá! irei te ajudar a calcular o tempo da sua viagem!")
distância = float(input("Digite a distância a ser percorrida em km: "))
velocidade = int(input("Digite a velocidade que espera manter na viagem (km/h): "))
tempo = distância/velocidade
print("A sua viagem levará %4.1f hora(s) até o destino." % tempo)
                            
                        # ou
print(f"A sua viagem levará {tempo:4.1f} hora(s) até o destino.")


#3.13) Converter a temperatuda de °C para °F
# fórmula: F = [(9*C)/5]+32

print("Olá! irei te ajudar a converter a temperatura de °C para °F")
temperatura_C = float(input("Digite a temperatura em °C: "))
temperatura_F =((temperatura_C * 9)/5)+32
print(f"{temperatura_C}°C equivale a {temperatura_F}°F")


#3.14) indagar quantos km o usuário percorreu com o carro alugado e quantos dias ficou com o automóvel. Calcular o preço a pagar.
# R$ 60 por dia e R$ 0,15 por km rodado.

print("A Localiza agradece a preferência! por favor, complete as lacunas abaixo.")
km_inicial = int(input("Qual a quilometragem INICIAL do carro? "))
km_final = int(input("Qual a quilometragem FINAL do carro? "))
km_total = (km_final - km_inicial)
dias_alugado = int(input("Quandos dias o carro ficou alugado?"))
total_a_pagar = (dias_alugado*60 + km_total*15/100)
print(f"O total a pagar é de R$: {total_a_pagar}")


#3.15) calcular a redução do tempo de vida de um fumante. Questionar quantos cigarros fuma por dia e por quantos anos já fumou.
    # um fumante perde 10min de vida a cada cigarro.
    # calcular quantos dias de vida o fumante já perdeu.

print("Olá! Irei te ajudar a calcular quantos dias de vida você já perdeu para os cigarros.")
quantidade = int(input("Quantos cigarros você costuma fumar por dia? "))
tempo_de_fumante = int(input("Por quantos anos você já fuma? "))
tempo_de_fumante = (tempo_de_fumante*365)
tempo_perdido_de_vida = ((quantidade*10*tempo_de_fumante)/1440)
print("Infelizmente você já perdeu %d dias de vida. Sentimos muito." % tempo_perdido_de_vida)



                   


















