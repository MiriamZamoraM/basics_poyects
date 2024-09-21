def contar_letras(palabra):
    return len(palabra)


palabra = input(str("¿Qué palabra deseas saber su numero de caracteres?  "))
numero_de_letras = contar_letras(palabra)
print(f"La palabra '{palabra}' tiene {numero_de_letras} letras.")
