"""
Se define una función para crear la base de datos. Se importan 2 librerías, se crea una tabla y se leen los regitros de un CSV para posteriormente introducirlos en la base de datos.
Con las 2 excepciones, se busca evitar los errores de integridad (campos únicos) y operacional (base de datos ya existente) en caso que se ejecute más de una vez el script principal.
"""

def crear_bd():

    import sqlite3
    import csv

    conexion = sqlite3.connect("ChampionsLeague.db")
    cursor = conexion.cursor()
    
    try: 
        cursor.execute( """
                        CREATE TABLE partidos(
                        anio VARCHAR (4) PRIMARY KEY UNIQUE NOT NULL,
                        sede VARCHAR (30) NOT NULL,
                        campeon VARCHAR (30) NOT NULL,
                        subcampeon VARCHAR (30) NOT NULL,
                        resultado VARCHAR (30) NOT NULL
                        )
        """)
    
    except sqlite3.OperationalError:
        pass
    
    try: 
        fichero = open(r"C:\Users\Alumne_tarda1\Desktop\BBDD.csv", "r")
        registros = csv.reader(fichero)
    
        insertar_registros = "INSERT INTO partidos (anio, sede, campeon, subcampeon, resultado) VALUES (?,?,?,?,?)"
    
        cursor.executemany(insertar_registros, registros)
    
    except sqlite3.IntegrityError:
        pass
    
    conexion.commit()
    conexion.close()