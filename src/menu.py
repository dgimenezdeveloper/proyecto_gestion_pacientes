import os
from src.inicializador import inicializar, inicializar_datos
from utils.interfaz_usuario import mostrar_menu_principal
from utils.constantes import SALIR
from utils.manejador_opcion import manejar_opcion

def menu_principal():
    sistema_gestion, grafo, grafo_diagnostico = inicializar()
    inicializar_datos(sistema_gestion, grafo, grafo_diagnostico)

    opcion = None
    while opcion != SALIR:
        os.system("clear")
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion(opcion, sistema_gestion, grafo, grafo_diagnostico)