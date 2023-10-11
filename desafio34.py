salario = float(input('Digite seu salario: '))
if salario>=1.250:
    novo =  salario + (salario * 10/100)
    print('seu aumento é de {}'.format(novo))
else:
    salario<=1.250
    novo = salario + (salario * 15/100)
    print('seu aumento e de {:.2f}'.format(novo))
    
