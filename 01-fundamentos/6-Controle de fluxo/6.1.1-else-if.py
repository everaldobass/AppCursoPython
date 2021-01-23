"""
Pode haver também um tipo de else if, no caso de haver mais de uma condição senão.
Neste caso, deve-se usar a palavra reservada elif.
"""

x = int(input("Digite um valor: "))
if x > 10:
    print(" Valor é X maior que 10: ","você digitou o número: ", x)
elif x <= 10 and x >= 5:
    print(" Valor de X é entre 5 e 10: ","você digitou o número:",x)
else:
    print(" Valor de X é  menor que 5: ","você digitou o número:", x)
