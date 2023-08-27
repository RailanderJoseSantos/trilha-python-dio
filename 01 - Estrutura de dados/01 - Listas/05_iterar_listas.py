carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

#Enumerate cria indice para cada elemento da lista
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
