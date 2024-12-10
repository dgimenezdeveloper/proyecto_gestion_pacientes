# src/paciente.py
from datetime import datetime

class Paciente:
    """
    Clase que representa a un paciente.
    """

    def __init__(self, id, nombre, fecha_nac, historial_enfermedades=None, medicamentos=None):
        """
        Inicializa una nueva instancia de la clase Paciente.

        - Args:
            * id (int): Identificador único del paciente.
            * nombre (str): Nombre del paciente.
            * fecha_nac (str): Fecha de nacimiento del paciente en formato "YYYY-MM-DD".
            * historial_enfermedades (list, opcional): Lista de enfermedades del paciente. Por defecto es una lista vacía.
            * medicamentos (list, opcional): Lista de medicamentos del paciente. Por defecto es una lista vacía.
        """
        self.id = id
        self.nombre = nombre
        self.fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")  # Convierte la cadena a datetime
        #self.edad = 0 
        self.historial_enfermedades = historial_enfermedades if historial_enfermedades else []
        self.medicamentos = medicamentos if medicamentos else []

    def calcular_edad(self):
        """
        Calcula la edad del paciente a partir de la fecha de nacimiento.

        Retorna:
            * (int): La edad del paciente.
        """
        hoy = datetime.today()
        edad = hoy.year - self.fecha_nac.year
        if hoy.month < self.fecha_nac.month or (hoy.month == self.fecha_nac.month and hoy.day < self.fecha_nac.day):
            edad -= 1
        return edad

    def buscar_en_historial(self, clave):
        """
        Busca una enfermedad o medicamento clave en el historial de tratamientos de un paciente.

        - Args:
            * clave (str): Enfermedad o medicamento clave a buscar.

        Retorna:
            * (bool): True si se encuentra la clave, False en caso contrario.
        """
        return self._buscar_en_historial_recursivo(self.historial_enfermedades + self.medicamentos, clave)

    def _buscar_en_historial_recursivo(self, historial, clave):
        """
        Función auxiliar recursiva para buscar una enfermedad o medicamento clave en el historial.

        - Args:
            * historial (list): Lista de enfermedades y medicamentos del paciente.
            * clave (str): Enfermedad o medicamento clave a buscar.

        Retorna:
            * (bool): True si se encuentra la clave, False en caso contrario.
        """
        # Caso base: si el historial está vacío, no se encontró la clave
        if not historial:
            return False
        
        # Verificar si la clave está en el tratamiento actual
        tratamiento_actual = historial[0]
        if tratamiento_actual == clave:
            return True
        
        # Llamada recursiva con el resto del historial
        return self._buscar_en_historial_recursivo(historial[1:], clave)

    def __lt__(self, otro):
        """
        Compara dos pacientes por su ID.

        - Args:
            * otro (Paciente): Otro paciente a comparar.

        Retorna:
            * (bool): True si el ID del paciente actual es menor que el ID del otro paciente, False en caso contrario.
        """
        return self.id < otro.id

    
    def __str__(self):
        """
        Devuelve una representación en cadena del paciente.

        - Retorna:
            * (str): Una cadena que representa al paciente.
        """
        return f"DNI: {self.id}\nNombre Paciente: {self.nombre}\nEdad: {self.calcular_edad()}\nEnfermedades: {self.historial_enfermedades}\nMedicamentos: {self.medicamentos}\n"