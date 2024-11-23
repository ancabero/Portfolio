"""
En este módulo se importan las distintas funciones definidas en otro módulos. En primer lugar se crea la base de datos y se muestra la bienvenida y las estadísticas que se pueden
consultar. Despúes, según la opción escogida se llama a una función, se cierra o se muestra que esa acción no está disponible. En el caso de la opción 2, se crea una clase, se instancia el
objeto y se crea una lista para guardar los atributos de ese objeto. Posteriormente, se añaden esos atributos como registros a la base de datos.
"""

from crearBBDD import crear_bd
from estadisticas import estadisticas

crear_bd()

print("Bienvenido/a a la consola de la Champions League. Aquí podrás consultar las siguientes estadísticas des de la edición del 2000:")
print("Año, sede, campeón, subcampéon y resultado. ")

while True:
    print("1) Consultar estadísticas\n2) Añadir una edición\n3) Salir de la consola")
    accion = input("Por favor, indica con el número correspondiente la acción que deseas realizar: ")

    match(accion):
        case "1":
            estadisticas()
        
        case "2":
            class Edicion:  
                def __init__(self):
                    self.anio = input("Hola, qué edición deseas añadir? ")
                    self.sede = input("Cuál fue la sede? ")
                    self.campeon = input("Quién fue el campeón? ")
                    self.subcampeon = input("Quién fue el subcampeón? ")
                    self.resultado = input("Cuál fue el resultado? ")

            edicion1 = Edicion()
        
            lista = [getattr(edicion1,"anio"), getattr(edicion1,"sede"), getattr(edicion1,"campeon"), 
                    getattr(edicion1,"subcampeon"), getattr(edicion1,"resultado")]   

            def nuevos_registros():
    
                import sqlite3
    
                conexion = sqlite3.connect("ChampionsLeague.db")
                cursor = conexion.cursor()

                try:
                    cursor.execute("INSERT INTO partidos VALUES ('{}','{}','{}','{}','{}')".format(lista[0], lista[1], lista[2],
                                                                                      lista[3], lista[4]))
                    print("Datos añadidos.")
                                                                                        
    
                except sqlite3.IntegrityError:
                    print("Lo sentimos, no puedes añadir está edición debido a que ya existe en la consola.")
                           
                conexion.commit()
                conexion.close()
    
            nuevos_registros()        
       
        case "3":
            print("Esperamos verte pronto de nuevo!")
            break
        
        case _:
            print("Está opción no esta contemplada en la consola.")