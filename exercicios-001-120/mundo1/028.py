import random

num = random.randint(0, 5)

num_user = int(input('Tente acertar qual número escolhi entre 0 e 5: '))

if num_user == num:
    print('Você acertou o número!')

else:
    print('Você errou o número!')
