ano = int(input(' que ano quer analisar? ' ))
if ano % 4 == 0:
    print(' o ano {} é BISSEXTO' .format(ano))
else:
    print('o ano {} nao é BISSEXTO' .format(ano))
