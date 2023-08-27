""" 
VERIFICA SE UM CONJUNTO É SUBCONJUNTO DE OUTRO (TODOS ELEMENTOS DE 1 SUBCONJUNTOTEM QUE ESTAR CONTIDO NO CONJUNTO)
"""
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)
