nome = 'Yuri Scorsolino'
idade = 22
altura = 1.80
peso = 80
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2
print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg \no IMC de {nome} é {imc:.2f} \n{nome} nasceu e"
      f" {nascimento} ")
