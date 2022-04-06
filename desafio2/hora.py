hora = input('Digite a hora')

if hora.isdigit():
   hora = int(hora)
   if hora < 0 or hora > 23:
       print('horario deve estar entre 0 e 23 ')
   else:
       if hora <= 11:
           print('Bomdia')
       elif hora <= 17:
           print('Boa tarde')
       else:
           print('Boa noite')
else:
    print('por favor digite um horario entra 0 e 23')


