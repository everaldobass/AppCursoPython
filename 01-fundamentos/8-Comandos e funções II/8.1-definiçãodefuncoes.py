
"""
8.1 Definição de Funções
Definições de funções auxiliam para automatizar procedimentos que são recorrentes no
código, evitando a necessidade de escrevê-los várias vezes. Bem como as outras estruturas
do Python, a estrutura de definição de funções também segue as regras da indentação e dos
dois pontos.
Para definir a função, usa-se a palavra reservada def, seguida do nome da função, dos
parâmetros entre parenteses e dos dois pontos. Os procedimentos devem ficar abaixo desta
linha e indentados. Para retornar valores, ou apenas para indicar o término da função,
deve-se usar a palavra return. Quaisquer estruturas de dados já vistas até agora podem ser
retornadas.

"""
# Um simples exemplo que soma dois números deve se parecer com:
def minhafuncsoma(a,b):
    s = a + b
    return s
   

    x = 2, y = 3
    z = minhafuncsoma(x, y)
  
   