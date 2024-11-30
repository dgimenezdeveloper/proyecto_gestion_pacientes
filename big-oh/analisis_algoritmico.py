from time import time
import csv
from estructuras.arbol_binario import ArbolBinarioBusqueda
from gestion.gestion_pacientes import GestionPacientes
from gestion.paciente import Paciente
from datos.datos_pacientes import cargar_datos_csv

def medir_tiempo(algoritmo, *args):
    start_time = time()
    algoritmo(*args)
    end_time = time()
    elapsed = end_time - start_time
    return elapsed

def cargar_datos_pacientes(archivo, sistema_gestion):
    with open(archivo, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            paciente = Paciente(
                id=int(row['dni']),
                nombre=row['nombre'],
                fecha_nac=row['fecha_nac'],
                historial_enfermedades=row['historial_enfermedades'].split(','),
                medicamentos=row['medicamentos'].split(',')
            )
            sistema_gestion.agregar_paciente(paciente)

def medir_tiempos_clases(archivo):
    # Crear instancia de GestionPacientes y ArbolBinarioBusqueda
    sistema_gestion = GestionPacientes()
    arbol_binario = ArbolBinarioBusqueda()

    # Cargar datos de pacientes desde el archivo CSV
    tiempo_cargar_datos = medir_tiempo(cargar_datos_pacientes, archivo, sistema_gestion)
    print(f"Tiempo de cargar datos de pacientes: {tiempo_cargar_datos:.6f} segundos")

    # Agregar paciente en GestionPacientes
    nuevo_paciente = Paciente(100, "Carlos", "1985-02-15")
    tiempo_agregar_gestion_pacientes = medir_tiempo(sistema_gestion.agregar_paciente, nuevo_paciente)
    print(f"Tiempo de agregar paciente en GestionPacientes: {tiempo_agregar_gestion_pacientes:.6f} segundos")

    # Agregar paciente en ArbolBinarioBusqueda
    tiempo_agregar_arbol = medir_tiempo(arbol_binario.insertar, nuevo_paciente)
    print(f"Tiempo de agregar paciente en ArbolBinarioBusqueda: {tiempo_agregar_arbol:.6f} segundos")

    # Obtener paciente en GestionPacientes
    tiempo_obtener_paciente = medir_tiempo(sistema_gestion.obtener_paciente, 1)  # Suponiendo que el paciente con ID 1 existe
    print(f"Tiempo de obtener paciente en GestionPacientes: {tiempo_obtener_paciente:.6f} segundos")

    # Obtener paciente en ArbolBinarioBusqueda
    tiempo_obtener_arbol = medir_tiempo(arbol_binario.buscar, 1)  # Suponiendo que el paciente con ID 1 existe
    print(f"Tiempo de obtener paciente en ArbolBinarioBusqueda: {tiempo_obtener_arbol:.6f} segundos")

    # Actualizar paciente en GestionPacientes
    tiempo_actualizar_paciente = medir_tiempo(lambda: sistema_gestion.actualizar_paciente(1, nombre="Juan Pérez"))
    print(f"Tiempo de actualizar paciente en GestionPacientes: {tiempo_actualizar_paciente:.6f} segundos")

    # Eliminar paciente en GestionPacientes
    tiempo_eliminar_gestion_pacientes = medir_tiempo(sistema_gestion.eliminar_paciente, 1)  # Suponiendo que el paciente con ID 1 existe
    print(f"Tiempo de eliminar paciente en GestionPacientes: {tiempo_eliminar_gestion_pacientes:.6f} segundos")

    # Eliminar paciente en ArbolBinarioBusqueda
    tiempo_eliminar_arbol = medir_tiempo(arbol_binario.eliminar, 1)  # Suponiendo que el paciente con ID 1 existe
    print(f"Tiempo de eliminar paciente en ArbolBinarioBusqueda: {tiempo_eliminar_arbol:.6f} segundos")

if __name__ == "__main__":
    archivo_pacientes = './datos/pacientes.csv'
    medir_tiempos_clases(archivo_pacientes)