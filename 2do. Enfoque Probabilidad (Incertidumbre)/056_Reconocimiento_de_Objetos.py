# Lista de objetos a evaluar
objetos = ['Mesa', 'Silla', 'Computadora', 'Lámpara']

# Clase para gestionar la identificación de objetos
class GestorObjetos:
    def __init__(self, objetos_conocidos):
        self.objetos_conocidos = set(objetos_conocidos)  # Usamos un conjunto para una búsqueda más rápida

    def clasificar_objetos(self, lista_a_clasificar):
        conocidos = []
        desconocidos = []
        
        for objeto in lista_a_clasificar:
            if objeto in self.objetos_conocidos:
                conocidos.append(objeto)
            else:
                desconocidos.append(objeto)

        return conocidos, desconocidos

# Creamos una instancia de GestorObjetos con los objetos que conocemos
modelo_identificacion = GestorObjetos(['Mesa', 'Computadora'])

# Clasificamos los objetos en la lista de objetos
objetos_reconocidos, objetos_no_reconocidos = modelo_identificacion.clasificar_objetos(objetos)

print("Objetos reconocidos:", objetos_reconocidos)
print("Objetos no reconocidos:", objetos_no_reconocidos)
