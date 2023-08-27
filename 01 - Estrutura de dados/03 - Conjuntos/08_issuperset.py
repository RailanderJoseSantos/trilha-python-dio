""" 
VERIFICA NÃO É UM CONJUNTO É SUBCONJUNTO DE OUTRO - Tds elementos de um subconjunto não pode estar no conjunto
"""
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
