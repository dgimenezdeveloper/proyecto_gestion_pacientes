import os
from utils.interfaz_usuario import (mostrar_menu_gestion_pacientes, mostrar_menu_operaciones_pacientes, mostrar_menu_gestion_hospitales, mostrar_menu_gestion_diagnosticos, mostrar_menu_operaciones_diagnosticos)
from utils.opciones import (manejar_opcion_gestion_pacientes, manejar_opcion_operaciones_pacientes, manejar_opcion_gestion_hospitales, manejar_opcion_gestion_diagnosticos, manejar_opcion_operaciones_diagnosticos)

def menu_gestion_pacientes(sistema_gestion):
    opcion = None
    while opcion != 5:
        os.system("clear")
        mostrar_menu_gestion_pacientes()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion_gestion_pacientes(opcion, sistema_gestion)
        input("\nPresione Enter para continuar...")


def menu_operaciones_pacientes(sistema_gestion):
    opcion = None
    while opcion != 5:
        os.system("clear")
        mostrar_menu_operaciones_pacientes()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion_operaciones_pacientes(opcion, sistema_gestion)
        input("\nPresione Enter para continuar...")


def menu_gestion_hospitales(grafo):
    opcion = None
    os.system("clear")
    while opcion != "6":
        mostrar_menu_gestion_hospitales()
        opcion = input("Seleccione una opción: ")
        manejar_opcion_gestion_hospitales(opcion, grafo)
        input("\nPresione Enter para continuar...")


def menu_gestion_diagnosticos(grafo_diagnostico):
    opcion = None
    while opcion != 3:
        os.system("clear")
        mostrar_menu_gestion_diagnosticos()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion_gestion_diagnosticos(opcion, grafo_diagnostico, menu_operaciones_diagnosticos)
        input("\nPresione Enter para continuar...")


def menu_operaciones_diagnosticos(grafo_diagnostico):
    opcion = None
    while opcion != 6:
        os.system('clear')
        mostrar_menu_operaciones_diagnosticos()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion_operaciones_diagnosticos(opcion, grafo_diagnostico)
        input("\nPresione Enter para continuar...")
