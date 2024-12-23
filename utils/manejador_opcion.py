import os
from utils.constantes import (GESTION_PACIENTES, OPERACIONES_PACIENTES, GESTION_HOSPITALES, GESTION_DIAGNOSTICOS, SALIR)
from src.menus import (menu_gestion_pacientes, menu_operaciones_pacientes, menu_gestion_hospitales, menu_gestion_diagnosticos)

def manejar_opcion(opcion, sistema_gestion, grafo, grafo_diagnostico):
    if opcion == GESTION_PACIENTES:
        menu_gestion_pacientes(sistema_gestion)
    elif opcion == OPERACIONES_PACIENTES:
        menu_operaciones_pacientes(sistema_gestion)
    elif opcion == GESTION_HOSPITALES:
        menu_gestion_hospitales(grafo)
    elif opcion == GESTION_DIAGNOSTICOS:
        menu_gestion_diagnosticos(grafo_diagnostico)
    elif opcion == SALIR:
        print("Saliendo del programa...")
        input("\nPresione Enter para continuar...")
        os.system('clear')
    else:
        print("Opción no válida. Intente de nuevo.")