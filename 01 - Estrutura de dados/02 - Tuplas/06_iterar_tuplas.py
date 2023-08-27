carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)

#mostra iterador
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
