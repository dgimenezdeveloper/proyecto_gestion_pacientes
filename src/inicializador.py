from datos.datos_pacientes import cargar_datos_csv
from datos.datos_hospitales import cargar_datos_hospitales
from datos.datos_diagnosticos import obtener_datos_diagnosticos
from estructuras.grafo import Grafo
from gestion.sistema_gestion_pacientes import SistemaGestionPacientes

def inicializar():
    sistema_gestion = SistemaGestionPacientes()
    grafo = Grafo()
    grafo_diagnostico = Grafo()
    return sistema_gestion, grafo, grafo_diagnostico

def inicializar_datos(sistema_gestion, grafo, grafo_diagnostico):
    vertices, aristas = obtener_datos_diagnosticos()
    grafo_diagnostico.cargar_datos(vertices, aristas)
    cargar_datos_hospitales(grafo)
    cargar_datos_csv(sistema_gestion, 'datos/pacientes.csv')