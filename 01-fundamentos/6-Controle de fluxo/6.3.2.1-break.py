
"""
Neste exemplo, while True indica um loop infinito, isto é, nunca sairá dele. No entanto,
caso x seja igual a 5, o loop é quebrado pelo comando break. Sendo assim, este laço irá
atribuir valores aleatórios e inteiros entre 0 e 10 para x até que seja atribuído o valor 5.
Todos os valores atribuídos, até chegar no 5 serão impressos.

"""

from random import randint
while True:
    x = randint(0, 10)
    print(x)
    if x == 5:
        break

