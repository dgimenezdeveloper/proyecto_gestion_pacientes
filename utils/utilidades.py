import os
from datos.datos_diagnosticos import obtener_datos_diagnosticos
from datos.datos_hospitales import cargar_datos_hospitales
from datos.datos_pacientes import cargar_datos_csv
from gestion.paciente import Paciente
from utils.inputs import (solicitar_dni, solicitar_nombre, solicitar_fecha_nacimiento, solicitar_lista, solicitar_hospitales, solcitar_rango_dni)
from utils.interfaz_usuario import mostrar_submenu_actualizar_paciente


# Gestion Pacientes
def inicializar_datos(sistema_gestion, grafo, grafo_diagnostico):
    vertices, aristas = obtener_datos_diagnosticos()
    grafo_diagnostico.cargar_datos(vertices, aristas)
    cargar_datos_hospitales(grafo)
    cargar_datos_csv(sistema_gestion, 'datos/pacientes.csv')

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


def actualizar_paciente(sistema_gestion, manejar_opcion_actualizar_paciente):
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

# Operaciones Pacientes
def buscar_paciente_rango(sistema_gestion):
    dni_min, dni_max = solcitar_rango_dni()
    pacientes = sistema_gestion.obtener_pacientes_rango(dni_min, dni_max)
    if pacientes:
        print("Pacientes encontrados:")
        for paciente in pacientes:
            print(paciente)
    else:
        print("No se encontraron pacientes en el rango de DNI especificado.")


def buscar_enfermedad(sistema_gestion, clave):
    pacientes = sistema_gestion.buscar_por_enfermedad(clave)
    if pacientes:
        print("Pacientes encontrados:")
        for paciente in pacientes:
            print(paciente)
    else:
        print(f"No se encontraron pacientes con {clave} en su historial.")


def buscar_medicamento(sistema_gestion, clave):
    pacientes = sistema_gestion.buscar_por_medicamento(clave)
    if pacientes:
        print("Pacientes encontrados:")
        for paciente in pacientes:
            print(paciente)
    else:
        print(f"No se encontraron pacientes con {clave} en su historial.")


def listar_pacientes(sistema_gestion):
    pacientes = sistema_gestion.listar_pacientes_ordenados()
    if pacientes:
        print("Pacientes ordenados por DNI:")
        for paciente in pacientes:
            print(paciente)
    else:
        print("No hay pacientes registrados.")

# Gestion Hospitales
def agregar_hospital(grafo):
    hospital = solicitar_hospitales(1)[0]
    grafo.agregar_vertice(hospital)


def agregar_conexion(grafo):
    hospital1, hospital2 = solicitar_hospitales(2)
    peso = int(input("Ingrese la distancia de la conexión: "))
    grafo.agregar_arista(hospital1, hospital2, peso)


def buscar_ruta(grafo):
    hospital1 = solicitar_hospitales(1)[0]
    if hospital1 in grafo.vertices:
        hospital2 = solicitar_hospitales(1)[0]
        ruta = grafo.dfs(hospital1, hospital2)
        if ruta is None:
            print("No se encontró una ruta entre los hospitales.")
        else:
            print("Ruta más corta encontrada (Dijkstra):", " -> ".join(ruta))


def buscar_ruta_corta(grafo):
    hospital1 = solicitar_hospitales(1)[0]
    if hospital1 in grafo.vertices:
        hospital2 = solicitar_hospitales(1)[0]
        ruta = grafo.bfs(hospital1, hospital2)
        if ruta is None:
            print("No se encontró una ruta entre los hospitales.")
        else:
            print("Ruta más corta:", ruta)

# Operaciones Diagnósticos

def agregar_diagnostico(grafo_diagnostico):
    os.system("clear")
    sintoma = input("Ingrese el síntoma inicial: ").lower()
    diagnostico = input("Ingrese el diagnóstico: ").lower()
    pasos = (
        input(
            "Ingrese los pasos necesarios para llegar al diagnóstico, separados por comas: "
        )
        .lower()
        .split(",")
    )

    grafo_diagnostico.agregar_vertice(sintoma)
    grafo_diagnostico.agregar_vertice(diagnostico)
    grafo_diagnostico.agregar_arista(sintoma, diagnostico)
    for paso in pasos:
        paso = paso.strip()
        if paso:
            grafo_diagnostico.agregar_vertice(paso)
            grafo_diagnostico.agregar_arista(diagnostico, paso)

    print(
        f"Diagnóstico '{diagnostico}' agregado con éxito para el síntoma '{sintoma}' con los pasos: {', '.join(pasos)}."
    )
    grafo_diagnostico.imprimir_grafo()


# Asegúrate de que el grafo_diagnostico tenga un método agregar_arista que permita agregar aristas entre los nodos.
def modificar_diagnostico(grafo_diagnostico):
    os.system("clear")
    sintoma = input("Ingrese el síntoma inicial: ").lower()
    diagnostico_actual = input("Ingrese el diagnóstico actual: ").lower()
    nuevo_diagnostico = input("Ingrese el nuevo diagnóstico: ").lower()
    if (
        sintoma in grafo_diagnostico.vertices
        and (diagnostico_actual, 1) in grafo_diagnostico.vertices[sintoma]
    ):
        grafo_diagnostico.agregar_vertice(nuevo_diagnostico)
        grafo_diagnostico.agregar_arista(sintoma, nuevo_diagnostico)
        print(
            f"Diagnóstico modificado de '{diagnostico_actual}' a '{nuevo_diagnostico}'."
        )
    else:
        print("No se encontró el diagnóstico actual para el síntoma ingresado.")


def eliminar_diagnostico(grafo_diagnostico):
    sintoma = input("Ingrese el síntoma del diagnóstico a eliminar: ").lower()
    diagnostico = input("Ingrese el diagnóstico a eliminar: ").lower()

    if (
        sintoma in grafo_diagnostico.vertices
        and (diagnostico, 1) in grafo_diagnostico.vertices[sintoma]
    ):
        grafo_diagnostico.vertices[sintoma].remove((diagnostico, 1))
        print(f"Diagnóstico '{diagnostico}' eliminado para el síntoma '{sintoma}'.")
    else:
        print("El diagnóstico no existe.")


def buscar_diagnostico_por_sintoma(grafo_diagnostico):
    sintoma = input("Ingrese el síntoma para buscar diagnósticos: ").lower()
    if sintoma in grafo_diagnostico.vertices:
        conexiones = grafo_diagnostico.vertices[sintoma]
        print(f"Diagnósticos para el síntoma '{sintoma}':")
        for diag, peso in conexiones:
            if diag != sintoma:
                print(f"- {diag}")
    else:
        print("No se encontraron diagnósticos para este síntoma.")


def generar_reporte_diagnosticos(grafo_diagnostico):
    """Procedimiento que imprime un reporte de los diagnósticos y sus síntomas asociados."""
    print("\nReporte de Diagnósticos")
    for sintoma, diagnosticos in grafo_diagnostico.vertices.items():
        print(f"\nSíntoma: {sintoma}")
        if diagnosticos:
            for diagnostico, peso in diagnosticos:
                print(f"  - Diagnóstico: {diagnostico}, Peso: {peso}")
        else:
            print("  No hay diagnósticos asociados.")

