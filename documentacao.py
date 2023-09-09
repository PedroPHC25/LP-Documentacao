import numpy as np
import numpy.random as npr

### Princípio da proximidade
### Princípio da simplicidade

# Sorteando valores inteiros entre 0 e 10
a = npr.randint(0, 10, 5)
b = npr.randint(0, 10, 5)


### Princípio da não redundância

# Sorteando valores inteiros entre 0 e 10  => COMENTÁRIO RUIM!!!
a = npr.randint(0, 10, 5)
b = npr.randint(0, 10, 5)


### Princípio do código limpo
# Um código simples e bem escrito nem precisa ser comentado


### LER A PEP 8


import documentacao_modulo as dm

print(dm.juros_simples(10000, 15.18, 12))

print(dm.juros_compostos(10000, 15.18, 12))

help(dm)