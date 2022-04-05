"""
operadores relacionais
== igual
> maior que
>= maior ou igual
< menor
<= menor ou igual
!= diferente de
"""

nome = input('qual seu nome? ')
idade = input('Qual sua idade? ')

#limite para pegar imprestimo
idade_menor = 20 #  jovem
idade_maior = 30 #  velho

if int(idade) >= idade_menor and int(idade) <= idade_maior:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} nao pode pegar o EMPRESTIMO')