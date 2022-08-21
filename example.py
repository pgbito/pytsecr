from pytsecr import tseclient
cliente = tseclient(proxylist={}) 
resultados = cliente.consulta_nombres('Carlos', 'Alvarado','Quesada',limite=3)
# Ejemplo de resultados:
#  [{"nombre_completo": "juanito mora", "cedula": 938},
# {"nombre_completo":"fernandito", "cedula": cualquiernumerodecedula}]
print('Encontramos {} resultados'.format(len(resultados)))


# Consulta acerca de alguien en especifico
# Con cedula

# Con alguien de los resultados de consulta_nombres
seleccion = resultados[0] # El primer resultado

datos=cliente.consulta_cedula(seleccion['cedula'])

print(datos)
print(datos.edad_str)
print(datos.cedula)
print(datos.datos_raw)
