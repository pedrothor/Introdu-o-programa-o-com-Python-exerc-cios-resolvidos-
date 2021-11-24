# 4.1)O que aconteceria se a=b? 
# o sistema não emitira nenhuma resposta, pois não foi programado para tal.

"""  a = float(input("Digite um valor para A: "))
b = float(input("Digite um valor para B: "))
if a>b:
    print("A é maior que B")
if b>a:
    print("B é maior que A") """

# 4.2) Perguntar a velocidade do carro (km/h). Caso velocidade > 80km/h, exibir "você foi multado". Além disso, exibir o valor da multa. Sabe-se que é cobra R$ 5 de multa a cada...
#...km/h a cima do permitido

""" print("Olá! irei te mostrar qual o valor da sua multa em caso de excesso de velocidade.")
velocidade = int(input("Digite a velocidade do carro (km/h): "))   
if velocidade>80:
    multa = ((velocidade - 80)*5)
    print(f"O valor da sua multa é de R$: {multa}")
if velocidade<80:
    print("Você não foi multado, boa viagem!") """


# 4.3) Solicitar 3 números ao usuário. Exibir o maior e o menor número.
""" print("Oi, hoje irei mostrar qual o maior e o menor número de uma sequência escolhida por você.")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))
if a>b>c:
    print("O primeiro número é o maior.")
    print("O terceiro número é o menor.")
if a>c>b:
    print("O primeiro número é o maior.")
    print("O segundo número é o menor.")
if b>a>c:
    print("O segundo número é o maior.")
    print("O terceiro número é o menor.")
if b>c>a:
    print("O segundo número é o maior.")
    print("O primeiro número é o menor.")
if c>a>b:
    print("O terceiro número é o maior.")
    print("O segundo número é menor.")
if c>b>a:
    print("O terceiro número é o maior.")
    print("O primeiro número é o menor.") """


# 4.4) Solicitar o salário do funcionário para um aumento. Calcular o valor do aumento. salario > R$ 1250, calcular um aumento de 10%. salario <= R$ 1250, aumento de 15%.
        # Calculei um imposto de 20% para novos salários > R$ 1250. Para novos salários < R$ 1250 não cobrei imposto.
"""print("Olá, tudo bem? Irei te ajudar a calcular o imposto de renda a ser pago com base no seu salário com o aumento.")
salário = float(input("Informe o valor em Reais (R$) do seu salário: "))
if salário>1250:
    novo_salário = (salário*1.10)
    base = novo_salário - salário
    imposto = base*0.20
    print(f"Seu novo salário é de R$: {novo_salário:6.2f}")
    print(f"O imposto a ser pago é de R$:{imposto:6.2f}")
if salário<1250:
    novo_salário = (salário*1.15)
    if novo_salário>1250:
        base = novo_salário - 1250
        imposto = base*0.20
        print(f"Seu novo salário é de R$: {novo_salário:7.2f}")
        print(f"O imposto a ser pago é de R$: {imposto:5.2f}")
    if novo_salário<1250:
        print("Você não tem que pagar imposto!")
if salário == 1250:
    print("Você não tem que pagar imposto!") """



# 4.5) escrever um programa parecido com o Programa 4.4 (carro novo ou velho) só que usando o "else".

""" print("Olá, hoje vamos averiguar se o seu carro está novo ou velho!")
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("O seu carro está novo!")
else:
    print("O seu carro está velho!") """


# 4.6) Pergunte a distância que o passageiro deseja percorrer (km).Calcule o preço da passagem. R$ 0.50 por km para viagens até 200km. R$ 0.45 para viagens superiores.

""" print("Oi, irei te ajudar a calcular o valor da sua passagem de ônibus pela nossa companhia.")
percurso = float(input("Digite quantos km tem o seu percurso: "))
if percurso <= 200:
    passagem = percurso*0.5
    print(f"O preço da sua passagem é de R$: {passagem:5.2f}")
else:
    passagem = percurso*0.45
    print(f"O preço da sua passagem é de R$: {passagem:5.2f}") """


# 4.7) Esse exercício era apenas para rastrear um exemplo de problema no livro. foi feito em folha avulsa. Siga para o próximo (4.8).

# 4.8) Escreva um programa que leia 2 números e pergunte qual o operação você deseja realizar. Exiba o resultado da operação.

""" print("Olá!! Sou uma calculadora simples. Irei ajudá-lo a fazer operações como: Somar, Subtrair, Dividir e Multiplicar.")
número1 = float(input("Digite o primeiro número: "))
número2 = float(input("Digite o segundo número: "))
operação = input("Digite qual operação você deseja efetuar: (+), (-), (/) ou (*): ")
if operação == "+":
    resultado = número1 + número2
    print(resultado)
elif operação == "-":
    resultado = número1 - número2
    print(resultado)
elif operação == "/":
    resultado = número1/número2
    print(resultado)
elif operação == "*":
    resultado = número1*número2
    print(resultado) """

# FAZENDO O EXERCÍCIO 4.8 SEM O "ELIF" APENAS PARA TREINAR.

""" print("Olá!! Sou uma calculadora simples. Irei ajudá-lo a fazer operações como: Somar, Subtrair, Dividir e Multiplicar.")
número1 = float(input("Digite o primeiro número: "))
número2 = float(input("Digite o segundo número: "))
operação = input("Digite qual operação você deseja efetuar: (+), (-), (/) ou (*): ")
if operação == "+":
    resultado = número1+número2
    print(resultado)
else:
    if operação == "-":
        resultado = número1-número2
        print(resultado)
    else:
        if operação == "/":
            resultado = número1/número2
            print(resultado)
        else:
            if operação == "*":
                resultado = número1*número2
                print(resultado)
            else:
                if operação != "+" "-" "/" "*":
                    print("Isso não é um símbolo de operação. Digite um síbomlo de operação matemática (+), (-), (/) ou (*)") """


# 4.9) Imagine que uma pessoa quer comprar uma casa. Pergunte o valor da casa a comprar, o salário do comprador e a quantidade de anos para pagar a casa.
#       A prestação não pode ser superior a 30% do salário. prestação = valor da casa dividido pelo número de meses a pagar.

""" print("Boa tarde!! Estamos muito felizes pela preferência. Iremos consultar se o senhor pode pegar o empréstimo conosco.")
valor_casa = float(input("Digite o valor da casa que o senhor quer comprar (apenas números): "))
salário = float(input("Digite o seu salário (apenas números): "))
quantos_anos = int(input("Informe em quantos anos o senhor pretende parcelar a casa: "))
prestação = valor_casa/(quantos_anos*12)
if prestação > 0.3*salário:
    print("Infelizmente o seu empréstimo não foi aprovado.")
elif prestação <= 0.3*salário:
    print("Parabéns!! O seu empréstimo foi aprovado.")
    print(f"O valor da mensalidade é de R$: {prestação:f}") """


# 4.10) Calcule o preço a pagar pelo fornecimento de energia. Pergunte quantos kwh que foi consumida e o tipo de instalação (R, I ou C). ver a tabela na página 83 caso dúvidas.

""" print("Bom dia!! irei te ajudar a calcular o valor da mensalidade pelo fornecimento de energia elétrica.")
lista = ["R","r","C","c","I","i"]
while True:
    tipo = input("Informe o tipo de instalação (R), (I) ou (C): ")
    if tipo not in lista:
        print("Tipo digitado é desconhecido.")
    else:
        break
kwh = float(input("Informa a quantidade de kWh consumida: "))
if tipo == "R"or"r":
    if kwh <= 500:
        valor_a_pagar = kwh*0.4
        print(f"O valor a ser pago é de R$: {valor_a_pagar:f}")
    else:
        if kwh>500:
            valor_a_pagar = kwh*0.65
            print(f"O valor a ser pago é de R$: {valor_a_pagar:f}")
elif tipo == "I"or"i":
    if kwh <= 5000:
        valor_a_pagar = kwh*0.55
        print(f"O valor a ser pago é de R$: {valor_a_pagar:f}")   
    else:
        if kwh > 5000:
            valor_a_pagar = kwh*0.6
            print(f"O valor a ser pago é de R$: {valor_a_pagar:f}")
elif tipo == "C"or"c":
    if kwh <= 1000:
        valor_a_pagar = kwh*0.55
        print(f"O valor a ser pago é de R$: {valor_a_pagar:f}")
    else:
        if kwh > 1000:
            valor_a_pagar = kwh*0.60 """


    





               










