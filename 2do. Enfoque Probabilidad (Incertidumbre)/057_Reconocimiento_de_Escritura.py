# Lista de objetos para el reconocimiento
objetos = ['Laptop', 'Teléfono', 'Tableta', 'Proyector']

# Función para simular el reconocimiento de objetos
def reconocimiento_objetos(lista_objetos):
    # Conjunto de objetos que podemos reconocer
    objetos_reconocidos = ['Laptop', 'Proyector']  # Objetos que podemos identificar
    identificados = []  # Lista para almacenar los objetos reconocidos
    no_identificados = []  # Lista para almacenar los objetos no reconocidos

    # Iteramos sobre la lista de objetos
    for objeto in lista_objetos:
        if objeto in objetos_reconocidos:  # Verificamos si el objeto es reconocido
            identificados.append(objeto)  # Agregamos a la lista de identificados
        else:
            no_identificados.append(objeto)  # Agregamos a la lista de no identificados

    return identificados, no_identificados  # Retornamos ambas listas

# Aplicamos el reconocimiento de objetos a la lista
objetos_identificados, objetos_no_identificados = reconocimiento_objetos(objetos)

# Imprimimos los resultados
print("Objetos reconocidos:", objetos_identificados)  # Mostramos los objetos que fueron reconocidos
print("Objetos no reconocidos:", objetos_no_identificados)  # Mostramos los objetos que no fueron reconocidos
