"""
continue
O segundo desvio é o continue. Ele serve para, a partir do momento que é atingindo, pular
para a próxima iteração do laço, ignorando os procedimentos abaixo dele. Exemplos:

Neste exemplo, o for irá iterar a variável x de 0 a 9 e imprimir seu valor. No entanto, caso a
x tenha o valor de 5, irá pular para a próxima iteração, ignorando os procedimentos abaixo,
ou seja, não o imprimindo. Neste caso, então, serão impressos todos os valores de 0 a 9,
exceto o 5.

"""

for x in range (0, 10):
    if x == 5:
        continue
    print(x)