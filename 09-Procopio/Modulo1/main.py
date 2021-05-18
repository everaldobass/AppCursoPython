from Smartphone import *
# Instanciando a class celular

# Aula 05 - Precisa passar todos os parametros declarados
celular = Smartphone(4, 64, 6.8)

# Aula 04 - Métodos
print(celular.instalar_app())
print(celular.enviar_mensagem())
# Aula 06 - Método str.- Imprime os parametros
celular.__str__()