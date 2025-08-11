import random


a = (''.join(str(random.randint(0, 9)) for _ in range(5))) + '-' + str(random.randint(0, 9))

b = ''

c = a + b

print(c)