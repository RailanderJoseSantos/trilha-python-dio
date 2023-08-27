""" 
Dicionario: Conjunto não ordenado de pares: chave:valor , chaves são unicas e imutavel , possivel mudar valor 
mas não chave
"""

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)
#dict = construtor dicionario
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
