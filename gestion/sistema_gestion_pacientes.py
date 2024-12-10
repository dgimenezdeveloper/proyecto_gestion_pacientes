# src/sistema_gestion_pacientes.py

from .gestion_pacientes import GestionPacientes
from estructuras.arbol_binario import ArbolBinarioBusqueda

class SistemaGestionPacientes:
    def __init__(self):
        self.gestion_pacientes = GestionPacientes()
        self.arbol = ArbolBinarioBusqueda()

    def agregar_paciente(self, paciente):
        if self.gestion_pacientes.agregar_paciente(paciente):
            self.arbol.insertar(paciente)
            return True
        return False

    def eliminar_paciente(self, id):
        if self.gestion_pacientes.eliminar_paciente(id):
            self.arbol.eliminar(id)
            return True
        return False

    def obtener_paciente(self, id):
        if self.gestion_pacientes.obtener_paciente(id) and self.arbol.buscar(id):
            return self.gestion_pacientes.obtener_paciente(id)
    
    def obtener_pacientes_rango(self, dni_min, dni_max):
        return self.arbol.obtener_pacientes_rango(dni_min, dni_max)
    
    def buscar_por_enfermedad(self, clave):
        return self.arbol.buscar_por_enfermedad(clave)
    
    def buscar_por_medicamento(self, clave):
        return self.arbol.buscar_por_medicamento(clave)
    
    def listar_pacientes_ordenados(self):
        return self.arbol.listar_pacientes_ordenados()
    

    def actualizar_paciente(self, id, nombre=None, fecha_nac=None, historial_enfermedades=None, medicamentos=None):
        if self.gestion_pacientes.actualizar_paciente(id, nombre, fecha_nac, historial_enfermedades, medicamentos):
            paciente = self.gestion_pacientes.obtener_paciente(id)
            self.arbol.eliminar(id)
            self.arbol.insertar(paciente)
            return True
        return False

    def __str__(self):
        return str(self.gestion_pacientes)