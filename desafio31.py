km = float(input('digite sua viagem: '))
if km<200:
    preço = km * 0.50
    print('sua viagem custaR${:.2f}'.format(preço))
else:
    preço = km * 0.45
    print('sua viagem custaR${:.2f}'.format(preço))
