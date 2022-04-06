nome = input('Digite seu primeiro nome')
tamanho = len(nome)

if tamanho <= 4:
    print('seu nome é muito pequeno')
elif tamanho <= 6:

    print('seu nome é normal')
else:
    print('Seu nome é muito grande')
