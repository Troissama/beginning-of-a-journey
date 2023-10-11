km = int(input('digite sua velocidade '))
if  km>80:
    print('voce esta correndo muito')
    multa = (km-80) * 7
    print('voce tem que pagar uma multa de R${:.2f}'.format(multa))
else:
    print('ta suave dirija com seguraça ai man')
