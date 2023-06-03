# texto_variado = "palabra 123 +- ^*"
# print(type(texto_variado))

# # podermos utilizar comilas triples para la cadena de texto que hemos escrito
# print("""
# Funcionamiento de \
# programa: (opciones)
#     -1 para acceder a opciones
#         -2 para salir
# """)

###########################################################
# Suscripting e indexado

texto = "python"
# print(texto)
# print(texto[1])
# print(texto[3])
# print(texto[-1])
# print(texto[6]) # error no podemos ecceder a una posicion que no existe

# letra = texto[0]
# print(letra)

# # texto[0] = "P" # una cadena de texto es inmutable

# # redefinir una varriable
# letra = "P"
# print(letra)

# #sumar las partes de una cadena con otras variables
# texto_compuesto = letra + texto[1] # concatenacion
# print(texto_compuesto)

####################################################

# slicing o subtringing
texto = 'Python'

# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:])
# print(texto[:3])
# print(texto[-3::-1]) # para cambiar el orden conforme a No final que son los saltos
print(texto[::-1])