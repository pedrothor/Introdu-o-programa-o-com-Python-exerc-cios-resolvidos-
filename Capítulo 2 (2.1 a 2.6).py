# 2.1) Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python
# a) 10 + 20 x 30
# b) 4^2 / 30
# c) (9^4 + 2) x 6 - 1

# a) 10 + 20 x 30
"""r=10+(20*30)"""

# b) 4^2 / 30
"""r=(4**2)/30"""

# c) (9^4 + 2) x 6 - 1
"""r=(9**4+2)*6-1"""


# 2.2) Digite a seguinte expressão no interpretador:
#      10%3*10**2+1-10*4/2
# Tente resolver o mesmo cálculo, usando apenas lápis e papel. Observe como a prioridade das operações é importante.

"""r=10%3*10**2+1-10*4/2
r=81 #prioridades = (**), (*),(/) ou (//), (%), (+) e (-)
print(r)"""


# 2.3) Faça um programa que exiva seu nome na tela.
"""nome=input("Digite o seu nome: ")
print(nome)"""


# 2.4) Escreva um programa que exiba o resultado de 2a x 3b, em que a=3 e b=5

"""a=3
b=5
r=3*a+2*b
print(r)

ou 

print(f"2a x 3b = {r}") # essa metodologia será ensinada mais a frente do livro."""


# 2.5) Escreva um programa que calcula a soma de três variáveis e imprima o resultado na tela.
"""a=int(input("Digite o valor da 1ª variável: "))
b=int(input("Digite o valor da 2ª variável: "))
c=int(input("Digite o valor da 3ª variável: "))
r=a+b+c
print(r)"""


# 2.6) Modifique o Programa 2.2, de forma que ele calcule um aumento de 15% para um salário de R$ 750.

"""Programa 2.2 - Cálculo de aumento de salário
salário=1500
aumento=5
print(salário + (salário*aumento/100))"""

"""salário=750
aumento=15
print(salário + (salário*15/100))"""

