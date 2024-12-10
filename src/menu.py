# src/menu.py
import os, csv
from gestion import SistemaGestionPacientes, Paciente, gestion_pacientes
from estructuras import ArbolGeneral, ColaPrioridades, Grafo
from datos import obtener_datos_diagnosticos, cargar_datos_hospitales
from datos.datos_pacientes import cargar_datos_csv
from utils import solicitar_dni, solicitar_nombre, solicitar_fecha_nacimiento, solicitar_lista, solcitar_rango_dni

# Constantes Menú Principal
GESTION_PACIENTES = 1
OPERACIONES_PACIENTES = 2
GESTION_HOSPITALES = 3
GESTION_DIAGNOSTICOS = 4
SALIR = 5

# Constantes Menú Gestion Pacientes
AGREGAR_PACIENTE = 1
ELIMINAR_PACIENTE = 2
OBTENER_PACIENTE = 3
ACTUALIZAR_PACIENTE = 4
VOLVER_MENU_PRINCIPAL = 5

def menu_principal():
    sistema_gestion = SistemaGestionPacientes()
    arbol_general = ArbolGeneral("Evento Raíz")
    cola_prioridades = ColaPrioridades()
    grafo = Grafo()
    grafo_diagnostico = Grafo()
    
    # Carga de datos iniciales
    inicializar_datos(sistema_gestion, grafo, grafo_diagnostico)

    opcion = None
    while opcion != SALIR:
        os.system('clear')
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion(opcion, sistema_gestion, grafo, grafo_diagnostico)
    

def inicializar_datos(sistema_gestion, grafo, grafo_diagnostico):
    vertices, aristas = obtener_datos_diagnosticos()
    grafo_diagnostico.cargar_datos(vertices, aristas)
    cargar_datos_hospitales(grafo)
    cargar_datos_csv(sistema_gestion, 'datos/pacientes.csv')

def mostrar_menu_principal():
    print("\nMenú Principal")
    print("1. Gestión de Pacientes")
    print("2. Operaciones con Pacientes")
    print("3. Gestión de Hospitales")
    print("4. Gestión de Diagnósticos")
    print("5. Salir")

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

def menu_gestion_pacientes(sistema_gestion):
    opcion = None
    while opcion != 5:
        os.system('clear')
        mostrar_menu_gestion_pacientes()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion_gestion_pacientes(opcion, sistema_gestion)
        input("\nPresione Enter para continuar...")

def mostrar_menu_gestion_pacientes():
    print("\nGestión de Pacientes")
    print("1. Agregar.")
    print("2. Eliminar.")
    print("3. Obtener información.")
    print("4. Actualizar información.")
    print("5. Volver al Menú Principal.")

def manejar_opcion_gestion_pacientes(opcion, sistema_gestion):
    if opcion == AGREGAR_PACIENTE:
        agregar_paciente(sistema_gestion)
    elif opcion == ELIMINAR_PACIENTE:
        eliminar_paciente(sistema_gestion)
    elif opcion == OBTENER_PACIENTE:
        obtener_paciente(sistema_gestion)
    elif opcion == ACTUALIZAR_PACIENTE:
        actualizar_paciente(sistema_gestion)
    elif opcion == VOLVER_MENU_PRINCIPAL:
        print("Volviendo al Menú Principal...")
    else:
        print("Opción no válida. Intente de nuevo.")

def agregar_paciente(sistema_gestion):
    os.system('clear')
    dni = solicitar_dni()
    nombre = solicitar_nombre()
    fecha_nac = solicitar_fecha_nacimiento()
    historial_enfermedades = solicitar_lista("Ingrese historial de enfermedades (separadas por comas): ")
    medicamentos = solicitar_lista("Ingrese medicamentos (separados por comas): ")
    paciente = Paciente(dni, nombre, fecha_nac, historial_enfermedades, medicamentos)
    sistema_gestion.agregar_paciente(paciente)
    print(f"Paciente agregado con éxito.")

def eliminar_paciente(sistema_gestion):
    dni = solicitar_dni()
    paciente = sistema_gestion.obtener_paciente(dni)
    if paciente:
        sistema_gestion.eliminar_paciente(dni)
        os.system('clear')
        print(f"Paciente con DNI {dni} eliminado con éxito.")
    else:
        os.system('clear')
        print(f"El paciente con DNI {dni} no existe.")
    input("Presione Enter para continuar...")

def obtener_paciente(sistema_gestion):
    dni = solicitar_dni()
    paciente = sistema_gestion.obtener_paciente(dni)
    os.system('clear')
    if paciente:
        print(f"Información del Paciente: {paciente}")
    else:
        print(f"El paciente con DNI {dni} no existe.")

def actualizar_paciente(sistema_gestion):
    dni = solicitar_dni()
    paciente = sistema_gestion.obtener_paciente(dni)
    if paciente:
        print(f"Información del Paciente: {paciente}")
        sub_opcion = None
        while sub_opcion != 5:
            os.system('clear')
            mostrar_submenu_actualizar_paciente()
            sub_opcion = int(input("Seleccione una opción: "))
            manejar_opcion_actualizar_paciente(sub_opcion, sistema_gestion, dni)
    else:
        print(f"El paciente con DNI {dni} no existe.")

def manejar_opcion_actualizar_paciente(opcion, sistema_gestion, dni):
    if opcion == 1:
        nombre = solicitar_nombre()
        sistema_gestion.actualizar_paciente(dni, nombre=nombre)
    elif opcion == 2:
        fecha_nac = solicitar_fecha_nacimiento()
        sistema_gestion.actualizar_paciente(dni, fecha_nac=fecha_nac)
    elif opcion == 3:
        historial_enfermedades = solicitar_lista("Ingrese historial de enfermedades (separadas por comas): ")
        sistema_gestion.actualizar_paciente(dni, historial_enfermedades=historial_enfermedades)
    elif opcion == 4:
        medicamentos = solicitar_lista("Ingrese medicamentos (separados por comas): ")
        sistema_gestion.actualizar_paciente(dni, medicamentos=medicamentos)
    elif opcion == 5:
        print("Volviendo al menú anterior...")
    else:
        print("Opción no válida. Intente de nuevo.")

def mostrar_submenu_actualizar_paciente():
    print("1. Actualizar nombre")
    print("2. Actualizar fecha de nacimiento")
    print("3. Actualizar historial de enfermedades")
    print("4. Actualizar medicamentos")
    print("5. Volver al menú anterior")

def menu_operaciones_pacientes(sistema_gestion):
    opcion = None
    while opcion != 5:
        os.system('clear')
        mostrar_menu_operaciones_pacientes()
        opcion = int(input("Seleccione una opción: "))
        manejar_opcion_operaciones_pacientes(opcion, sistema_gestion)
        input("\nPresione Enter para continuar...")

def manejar_opcion_operaciones_pacientes(opcion, sistema_gestion):
    if opcion == 1:
        dni_min, dni_max = solcitar_rango_dni()
        pacientes = sistema_gestion.obtener_pacientes_rango(dni_min, dni_max)
        if pacientes:
            print("Pacientes encontrados:")
            for paciente in pacientes:
                print(paciente)
        else:
            print("No se encontraron pacientes en el rango de DNI especificado.")
    elif opcion == 2:
        clave = input("Ingrese enfermedad: ").lower()
        pacientes = sistema_gestion.buscar_por_enfermedad(clave)
        if pacientes:
            print("Pacientes encontrados:")
            for paciente in pacientes:
                print(paciente)
        else:
            print(f"No se encontraron pacientes con {clave} en su historial.")
    elif opcion == 3:
        clave = input("Ingrese medicamento: ").lower()
        pacientes = sistema_gestion.buscar_por_medicamento(clave)
        if pacientes:
            print("Pacientes encontrados:")
            for paciente in pacientes:
                print(paciente)
    elif opcion == 4:
        pacientes = sistema_gestion.listar_pacientes_ordenados()
        if pacientes:
            print("Pacientes ordenados por DNI:")
            for paciente in pacientes:
                print(paciente)
        else:
            print("No hay pacientes registrados.")
    elif opcion == 5:
        print("Volviendo al Menú Principal...")
    else:
        print("Opción no válida. Intente de nuevo.")

def mostrar_menu_operaciones_pacientes():
    print("\nOperaciones con Pacientes")
    print("1. Búsqueda de Pacientes por Rango DNI")
    print("2. Buscar Pacientes por Enfermedad")
    print("3. Buscar Pacientes por Medicamento")
    print("4. Listar Pacientes en Orden")
    print("5. Volver al Menú Principal")

#TODO: REFACTORIZAR MENU GESTION HOSPITALES
#TODO: CREAR CONSTANTES PARA LOS MENUS
#TODO: CREAR FUNCIONES PARA CADA OPCION DE LOS MENUS

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
                    print("Ruta más corta encontrada (Dijkstra):", " -> ".join(ruta))
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