"""
4.2
Entrada e Saída de Dados
Para se criar rotinas e procedimentos mais sofisticados, por vezes, é necessário programar
para coletar dados do usuário e imprimir os resultados. Isto é chamado de entrada e saída
de dados.


4.2.1
Entrada
A função canônica de entrada de dados, isto é, para pedir informações do usuário é a
função input.
Nela, o argumento é uma mensagem impressa e o retorno é o que o usuário digitar.

"""

#Nesta função, mesmo que o usuário digite valores numéricos, os dados serão armazenados como strings. 
frase = input("Digite uma frase \n")

#Para usá-los como outros tipos de dados, deve convertê-los.
numero = int(input("Digite sua idade: "))

"""

4.2.2
Saída
Para a saída de dados há a função print. Pode imprimir mais de uma string e também
valores, separados por vírgulas.

"""

print("A Frase é: ", frase)
print("Número digitado é: ", numero )

