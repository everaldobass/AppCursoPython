"""
8.1.1  Escopo
No caso das definições de funções, alguns conceitos devem ser esclarecidos. Ainda no
exemplo de minhaprimeirafunc.py, na chamada da função, linha 12, não foram usados a
e b, foram usados x e y. Isso porque a e b são os parâmetros da função, isto é, ela comporta
ser chamada com diferentes valores sendo passados no lugar de a e b.
Após a chamada, ao entrar na função, isto é, dentro do escopo da função, os valores
passados no lugar de a e b são copiados para elas, que serão usadas para os procedimentos
da função. No entanto, essas variáveis só existem no escopo da função, isto é, no resto do
código, a e b ainda não foram declarados. Outro exemplo:
"""

def exemplo1():
    A = 10
    print (A)

exemplo1()
print(A)

