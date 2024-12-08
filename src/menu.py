# src/menu.py
import os, csv
from gestion import SistemaGestionPacientes, Paciente, gestion_pacientes
from estructuras import ArbolGeneral, ColaPrioridades, Grafo
from datos import obtener_datos_diagnosticos, cargar_datos_hospitales
from datos.datos_pacientes import cargar_datos_csv
from utils import solicitar_dni, solicitar_nombre, solicitar_fecha_nacimiento, solicitar_lista

def menu_principal():
    sistema_gestion = SistemaGestionPacientes()
    arbol_general = ArbolGeneral("Evento Raíz")
    cola_prioridades = ColaPrioridades()
    grafo = Grafo()
    grafo_diagnostico = Grafo()
    
    vertices, aristas = obtener_datos_diagnosticos()
    grafo_diagnostico.cargar_datos(vertices, aristas)
    
    cargar_datos_hospitales(grafo)
    #Cargar datos de pacientes
    cargar_datos_csv(sistema_gestion, '../datos/pacientes.csv')

    os.system('clear')
    opcion = None
    while opcion != "5":
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_gestion_pacientes(sistema_gestion)
        elif opcion == "2":
            menu_operaciones_pacientes(sistema_gestion)
        elif opcion == "3":
            menu_gestion_hospitales(grafo)
        elif opcion == "4":
            menu_gestion_diagnosticos(grafo_diagnostico)
        elif opcion == "5":
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_principal():
    print("\nMenú Principal")
    print("1. Gestión de Pacientes")
    print("2. Operaciones con Pacientes")
    print("3. Gestión de Hospitales")
    print("4. Gestión de Diagnósticos")
    print("5. Salir")

def menu_gestion_pacientes(sistema_gestion):
    opcion = None
    while opcion != "5":
        os.system('clear')
        mostrar_menu_gestion_pacientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dni = solicitar_dni()
            nombre = solicitar_nombre()
            fecha_nac = solicitar_fecha_nacimiento()
            historial_enfermedades = solicitar_lista("Ingrese historial de enfermedades (separadas por comas): ")
            medicamentos = solicitar_lista("Ingrese medicamentos (separados por comas): ")
            paciente = Paciente(dni, nombre, fecha_nac, historial_enfermedades, medicamentos)
            sistema_gestion.agregar_paciente(paciente)
            os.system('clear')
            print(f"Paciente agregado con éxito.")
            input("Presione Enter para continuar...")
        elif opcion == "2":
            dni = solicitar_dni()
            paciente = sistema_gestion.obtener_paciente(dni)
            if paciente:
                print(f"Datos del paciente:\n{paciente}")
                confirmacion = input("¿Está seguro que desea eliminar este paciente? (s/n): ").strip().lower()
                if confirmacion == 's':
                    if sistema_gestion.eliminar_paciente(dni):
                        print("Paciente eliminado con éxito.")
                    else:
                        print("Error al eliminar el paciente.")
                else:
                    print("Eliminación cancelada.")
            else:
                print("El paciente no existe.")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            dni = solicitar_dni()
            paciente = sistema_gestion.obtener_paciente(dni)
            print(paciente)
            input("Presione Enter para continuar...")
        elif opcion == "4":
            dni = solicitar_dni()
            paciente = sistema_gestion.obtener_paciente(dni)
            if paciente:
                sub_opcion = None
                while sub_opcion != "5":
                    os.system('clear')
                    print("\nActualizar Información del Paciente")
                    mostrar_submenu_actualizar_paciente()
                    sub_opcion = input("Seleccione una opción: ")

                    if sub_opcion == "1":
                        nombre = solicitar_nombre()
                        sistema_gestion.actualizar_paciente(dni, nombre=nombre)
                    elif sub_opcion == "2":
                        fecha_nac = solicitar_fecha_nacimiento()
                        sistema_gestion.actualizar_paciente(dni, fecha_nac=fecha_nac)
                    elif sub_opcion == "3":
                        historial_enfermedades = solicitar_lista("Ingrese historial de enfermedades (separadas por comas): ")
                        sistema_gestion.actualizar_paciente(dni, historial_enfermedades=historial_enfermedades)
                    elif sub_opcion == "4":
                        medicamentos = solicitar_lista("Ingrese medicamentos (separados por comas): ")
                        sistema_gestion.actualizar_paciente(dni, medicamentos=medicamentos)
                    elif sub_opcion == "5":
                        print("Volviendo al menú anterior...")
                    else:
                        print("Opción no válida. Intente de nuevo.")
                    input("Presione Enter para continuar...")
        elif opcion == "5":
            print("Volviendo al Menú Principal...")
        else:
            print("Opción no válida. Intente de nuevo.")
        input("Presione Enter para continuar...")
        os.system('clear')

def mostrar_menu_gestion_pacientes():
    print("\nGestión de Pacientes")
    print("1. Agregar.")
    print("2. Eliminar.")
    print("3. Obtener información.")
    print("4. Actualizar información.")
    print("5. Volver al Menú Principal.")

def mostrar_submenu_actualizar_paciente():
    print("1. Actualizar nombre")
    print("2. Actualizar fecha de nacimiento")
    print("3. Actualizar historial de enfermedades")
    print("4. Actualizar medicamentos")
    print("5. Volver al menú anterior")

def menu_operaciones_pacientes(sistema_gestion):
    opcion = None
    os.system('clear')
    while opcion != "4":
        mostrar_menu_operaciones_pacientes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            dni = solicitar_dni()
            nombre = solicitar_nombre()
            fecha_nac = solicitar_fecha_nacimiento()
            historial_enfermedades = solicitar_lista("Ingrese historial de enfermedades (separadas por comas): ")
            medicamentos = solicitar_lista("Ingrese medicamentos (separados por comas): ")
            paciente = Paciente(dni, nombre, fecha_nac, historial_enfermedades, medicamentos)
            sistema_gestion.agregar_paciente(paciente)
        elif opcion == "2":
            dni = solicitar_dni()
            paciente = sistema_gestion.obtener_paciente(dni)
            print(paciente)
        elif opcion == "3":
            dni = solicitar_dni()
            sistema_gestion.eliminar_paciente(dni)
        elif opcion == "4":
            print("Volviendo al Menú Principal...")
            os.system('clear')
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_operaciones_pacientes():
    print("\nOperaciones con Pacientes")
    print("1. Registrar un nuevo paciente")
    print("2. Buscar un paciente por DNI")
    print("3. Eliminar un paciente por DNI")
    print("4. Volver al Menú Principal")

def menu_gestion_hospitales(grafo):
    opcion = None
    os.system('clear')
    while opcion != "6":
        mostrar_menu_gestion_hospitales()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hospital = input("Ingrese el nombre del hospital: ")
            grafo.agregar_vertice(hospital)
        elif opcion == "2":
            hospital1 = input("Ingrese el nombre del primer hospital: ")
            hospital2 = input("Ingrese el nombre del segundo hospital: ")
            peso = int(input("Ingrese el peso de la conexión: "))
            grafo.agregar_arista(hospital1, hospital2, peso)
        elif opcion == "3":
            hospital1 = input("Ingrese el nombre del hospital de inicio: ")
            if hospital1 in grafo.vertices:
                hospital2 = input("Ingrese el nombre del hospital de destino: ")
                ruta = grafo.dfs(hospital1, hospital2)
                if ruta is None:
                    print("No se encontró una ruta entre los hospitales.")
                else:
                    print("Ruta encontrada:", ruta)
            print(f"Ruta: {ruta}")
        elif opcion == "4":
            hospital1 = input("Ingrese el nombre del hospital de inicio: ")
            if hospital1 in grafo.vertices:
                hospital2 = input("Ingrese el nombre del hospital de destino: ")
                ruta = grafo.bfs(hospital1, hospital2)
                if ruta is None:
                    print("No se encontró una ruta entre los hospitales.")
                else:
                    print("Ruta más corta:", ruta)
        elif opcion == "5":
            hospital = input("Ingrese el nombre del hospital: ")
            grafo.imprimir_dijkstra(hospital)
        elif opcion == "6":
            print("Volviendo al Menú Principal...")
            os.system('clear')
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_gestion_hospitales():
    print("\nGestión de Hospitales")
    print("1. Agregar un nuevo hospital")
    print("2. Agregar una conexión entre hospitales")
    print("3. Buscar una ruta entre hospitales")
    print("4. Buscar una ruta más corta entre hospitales")
    print("5. Calcular distancias desde un hospital")
    print("6. Volver al Menú Principal")

def menu_gestion_diagnosticos(grafo_diagnostico):
    continuar = True
    while continuar:
        os.system('clear')
        mostrar_menu_gestion_diagnosticos()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system('clear')
            sintoma = input("Ingrese el síntoma inicial: ").lower()
            diagnostico = input("Ingrese el diagnóstico: ").lower()
            camino = grafo_diagnostico.dfs(sintoma, diagnostico)
            if camino:
                print(f"Pasos necesarios para {diagnostico}: {' -> '.join(camino)}")
            else:
                print("No se encontraron pasos para este diagnóstico.")
            input("\nPresione Enter para continuar...")
        elif opcion == "2":
            continuar = False
            os.system('clear')
        else:
            print("Opción no válida. Intente de nuevo.")
            input("\nPresione Enter para continuar...")

def mostrar_menu_gestion_diagnosticos():
    print("\nGestión de Diagnósticos")
    print("1. Encontrar pasos para un diagnóstico")
    print("2. Volver al Menú Principal")