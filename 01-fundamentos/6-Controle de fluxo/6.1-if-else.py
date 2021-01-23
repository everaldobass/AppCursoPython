"""
if-else
A estrutura if avalia uma expressão, caso a expressão seja verdadeira, os procedimentos
subordinados são executados. Não é obrigatório, mas em seguida, pode-se adicionar apenas
o else, com outros procedimentos subordinados, que serão executados caso a condição do
if seja falsa.

"""

x =  int(input("Digite um valor:"))
if x < 10:
    print("X e menor ou igual que 10: ", x<10, "Valor de X", x)
else:
        print("X e maior ou igual a 10: ", x>=10, "Valor de X", x)
