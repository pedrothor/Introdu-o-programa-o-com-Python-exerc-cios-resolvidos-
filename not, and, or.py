a=True
b=False
c=True

a and a
True

b and b
False

not c
False

not b
True

not a
False

a and b
False

b and c
False

a or c
True

b or c
True

c or a
True

c or b
True

c or c
True

b or b
False

# quando temos mais de 1 operador lógico, resolvemos a expressão pela ordem:
# 1) not        2) and          3) or
# ex: True or False and not True
#       True or False and False
#           True or False
#               True

#   Também pode-se juntar operadores relacionais com operadores lógicos, sendo assim,os operadores relacionais devem ser resolvidos primeiro:
#       salário>1000 and idade>18
#           salário = 100 e idade = 20
#       False and True
#           False

