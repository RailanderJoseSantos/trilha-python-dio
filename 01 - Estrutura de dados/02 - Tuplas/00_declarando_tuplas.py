#tuplas devem ser finalizadas por "," uma boa pratica pra evitar que python interprete o parentese ou colchetes
#como precedencia

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
