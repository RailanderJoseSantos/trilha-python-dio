lista = ["p", "y", "t", "h", "o", "n"]

# No fatiamento o campo ocutado origem:fim interpretador considera do inicio ou do fim (o que for ocutado)
# **Posição final é sempre o valor -1
# step z (saltos) x:y:z
print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]
