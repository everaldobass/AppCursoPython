"""
Desvio Incondicional
Os desvios incondicionais são mudanças da execução do programa para outra linha, isto é,
desviar o código para outra parte. Há dois comandos de desvio, break e continue.
"""

#break
"""
Neste caso, o for estará preparado para iterar a variável i de 0 até 199999, no entanto, caso
i seja igual a 5, haverá um break, isto é, sairá do laço, Assim, só serão impressos os valores
0, 1, 2, 3, 4 e 5.

"""
for i in range(0,20000):
    print("Valor de I ", i)
    if i == 100:
        break

    """LinuxPro"""