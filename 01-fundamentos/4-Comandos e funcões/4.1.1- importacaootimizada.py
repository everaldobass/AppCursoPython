"""
4.1.1
Importação Otimizada
O comando import importa a biblioteca com todas as suas funcionalidades. As vezes,
apenas algumas funcionalidades são de interesse, como no exemplo acima, apenas a sqrt.
Há a opção de importar apenas o que se deseja para economizar memória e para não


precisar especificar a biblioteca da qual foi importado. Para isso, em conjunto com o
comando import, utiliza-se o comando from, de forma a ficar como: from <biblioteca>
import <funcionalidade1>, <funcionalidade2>,...

Dessa forma, os métodos são importados diretamente para a pasta, por isso não é ne-
cessário explicitar a biblioteca de origem.
"""

from math import cos, pi
cos(pi)

