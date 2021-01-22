"""

Estruturas de Repetição
Já o segundo conjunto de estruturas, as estruturas de repetição, são responsáveis por criar
laços que repetem os procedimentos a eles subordinados. A cada repetição é dada o nome
de iteração.

while
O primeiro é o while. While avalia a condição a ele exposta a cada iteração, e enquanto ela
for verdadeira, o laço é mantido. Quando a condição é falsa, o laço é terminado.


Neste exemplo, o i começa valendo 0. O while avalia a condição que é, inicialmente,
verdadeira, então a primeira iteração é realizada, que imprimirá 0 e incremetará o i. Isto
acontecerá até que i seja igual a nove, pois assim será impresso 10, o i será incrementado
para 11 e a condição para o while será falsa, assim o laço irá terminar.

"""
i = 0
while i <= 10:
    print("Valor de I: ", i)
    i += 1

