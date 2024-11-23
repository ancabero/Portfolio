"""
Se importan 2 librerías(1 para poder leer la base de datos y otra para una interfaz gráfica). En caso que la edicón consultada no exista en la base de datos, se muestra que esos datos
no están disponibles. En caso de que esos datos existan, muestra una interfaz gráfica con algunas estadísticas de esa edición.
"""

from tkinter import *

def estadisticas():
    import sqlite3
 
    root = Tk()
    root.title("Estadísticas UEFA Champions League")
    root.resizable(FALSE,FALSE)
    root.config(bd = 15, relief="groove", bg = "DeepSkyBlue2")

    conexion = sqlite3.connect("ChampionsLeague.db")
    cursor = conexion.cursor()
    
    edicion = input("Hola, de que edición deseas conocer las estadísticas? ")

    cursor.execute("SELECT * FROM partidos WHERE anio = {}".format(edicion))

    estadisticas = cursor.fetchall()
    
    if estadisticas == []:
        Label(root, text = "Lo sentimos, no tenemos las estadísticas para esta edición",
             fg = "black", font = ("Calibri", 15)).pack()
    else:
        for estadistica in estadisticas:
            Label(root, text ="Año: {}\nSede: {}\nCampeón: {}\nSubcampeón: {}\nResultado: {}".format(estadistica[0],
                                                                                                     estadistica[1],
                                                                                                     estadistica[2],
                                                                                                     estadistica[3],
                                                                                                     estadistica[4]),
                  fg = "black", font = ("Calibri, 15")).pack()
    
    conexion.close()
    root.mainloop()