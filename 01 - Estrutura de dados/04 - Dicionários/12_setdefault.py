""" Se ao setar uma chave e valor, aquela chave ja existir nada é alterado, do caso a chave não existe
o novo valor é setado - Util para se adicionar valor apenas se não existe, não precisando de uma verificação
previa """
contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
