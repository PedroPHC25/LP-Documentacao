"""Documentação do módulo

Blá-blá-blá
"""

# Função que calcula montante e juros em um regime de juros simples
# Type Hint: MyPy
def juros_simples(capital: int, taxa: float, tempo: int) -> tuple:
    juros = capital * taxa/100 * tempo
    montante = capital + juros
    
    # TODO: Alterar estrutura de dados de retorno para lista
    # BUG
    # FIXME
    
    # TODO: Limitar montante e capital a dois dígitos decimais
    return (montante, juros)


"""

"""

def juros_compostos(capital, taxa, tempo):
    """Cálculo de juros compostos
    Parameters
    ----------
    capital : int
        xxxxxx.
    taxa : float
        yyyyyy.
    tempo : int
        zzzzzz.

    Returns
    -------
    tuple
        ttttttt.
    """
    assert isinstance(taxa, float), "Taxa não é decimal."
    montante = capital * (pow((1 + taxa/100), tempo))
    juros = montante - capital
    
    return (round(montante, 2), round(juros, 2))

print(help(juros_simples))