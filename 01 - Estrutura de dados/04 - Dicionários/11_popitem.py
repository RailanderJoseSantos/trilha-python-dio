""" Não se informa chave, elimina na sequencia todos os registros por linha a cada pop """
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError
