from random import randint
pc = randint(0, 5)
print('vou pensar em um numero entre 0 e 5.  Adivinha ai...')
jg = int(input('em que numero eu pensei? '))
if jg == pc:
    print('voce acertou')
else:
    print('voce errou')
