""" Cria chaves com valores none ou valores padrões """
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)
