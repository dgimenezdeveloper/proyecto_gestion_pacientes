from datetime import datetime
from .paciente import Paciente

class GestionPacientes:
    """
    Clase para gestionar una colección de pacientes.

    - Atributos:
        * pacientes (dicc): Diccionario de pacientes donde las claves son los IDs de los pacientes y los valores son instancias de la clase Paciente.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de la clase GestionPacientes.
        """
        self.pacientes = {}

    def agregar_paciente(self, paciente):
        """
        Agrega un nuevo paciente a la colección.

        - Args:
            * paciente (Paciente): Instancia de la clase Paciente a agregar.

        - Raises:
            * ValueError: Si el paciente con el ID dado ya existe.
        """
        if paciente.id in self.pacientes:
            return False
        self.pacientes[paciente.id] = paciente
        return True

    def eliminar_paciente(self, id):
        """
        Elimina un paciente de la colección.

        - Args:
            * id (int): ID único del paciente a eliminar.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        if id in self.pacientes:
            del self.pacientes[id]
            return True
        return False

    def obtener_paciente(self, id):
        """
        Obtiene un paciente de la colección.

        - Args:
            * id (int): ID único del paciente a obtener.

        - Retorna:
            * Paciente: La instancia de la clase Paciente correspondiente al ID dado, o None si no se encuentra.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        return self.pacientes.get(id)

    def actualizar_paciente(self, id, nombre=None, fecha_nac=None, historial_enfermedades=None, medicamentos=None):
        """
        Actualiza la información de un paciente en la colección.

        - Args:
            * id (int): ID único del paciente a actualizar.
            * nombre (str, opcional): Nuevo nombre del paciente.
            * fecha_nac (str, opcional): Nueva fecha de nacimiento del paciente en formato "YYYY-MM-DD".
            * historial_enfermedades (list, opcional): Nuevo historial de enfermedades del paciente.
            * medicamentos (list, opcional): Nueva lista de medicamentos del paciente.

        - Raise:
            * KeyError: Si no se encuentra un paciente con el ID dado.
        """
        paciente = self.obtener_paciente(id)
        if paciente:
            self._actualizar_nombre(paciente, nombre)
            self._actualizar_fecha_nacimiento(paciente, fecha_nac)
            self._actualizar_historial(paciente, historial_enfermedades)
            self._actualizar_medicamentos(paciente, medicamentos)
            return True
        return False
    
    def _actualizar_nombre(self, paciente, nombre):
        """Actualiza el nombre del paciente si se proporciona uno nuevo."""
        if nombre:
            paciente.nombre = nombre

    def _actualizar_fecha_nacimiento(self, paciente, fecha_nac):
        """Actualiza la fecha de nacimiento del paciente si se proporciona una nueva."""
        if fecha_nac:
            paciente.fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")
            paciente.edad = paciente.calcular_edad()

    def _actualizar_historial(self, paciente, historial_enfermedades):
        """Actualiza el historial de enfermedades del paciente si se proporciona uno nuevo."""
        if historial_enfermedades:
            paciente.historial_enfermedades.extend(historial_enfermedades)

    def _actualizar_medicamentos(self, paciente, medicamentos):
        """Actualiza la lista de medicamentos del paciente si se proporciona una nueva."""
        if medicamentos:
            paciente.medicamentos.extend(medicamentos)
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la colección de pacientes.

        - Retorna:
            * str: Una cadena que representa la colección de pacientes.
        """
        resultado = []
        for id_paciente, paciente in self.pacientes.items():
            resultado.append(f"Id paciente: {id_paciente}\n {paciente}")
        return "\n".join(resultado)



if __name__ == "__main__":
    # Crear pacientes
    paciente1 = Paciente(1,"Juan", "1990-01-01", ["Gripe", "Fiebre"], ["Paracetamol", "Ibuprofeno"])
    paciente2 = Paciente(2,"Ana", "1985-05-10", ["Covid-19", "Asma"], ["Remdesivir", "Salbutamol"])
    paciente3 = Paciente(3,"Luis", "1975-03-22", ["Diabetes", "Hipertensión"], ["Insulina", "Lisinopril"])
    paciente4 = Paciente(4,"Maria", "2000-07-15", ["Alergia", "Migraña"], ["Loratadina", "Sumatriptán"])

    # Crear una colección de pacientes
    gestion_pacientes = GestionPacientes()
    gestion_pacientes.agregar_paciente(paciente1)
    gestion_pacientes.agregar_paciente(paciente2)
    gestion_pacientes.agregar_paciente(paciente3)
    gestion_pacientes.agregar_paciente(paciente4)

    # Mostrar la colección de pacientes
    print("Colección de pacientes:")
    print(gestion_pacientes)

    # Obtener y mostrar un paciente
    print("\nObtener paciente con ID 2:")
    paciente = gestion_pacientes.obtener_paciente(2)
    print(paciente)

    # Actualizar un paciente
    print("\nActualizar paciente con ID 3:")
    gestion_pacientes.actualizar_paciente(3, nombre="Luis Pérez", historial_enfermedades=["Diabetes", "Hipertensión", "Colesterol"], medicamentos=["Insulina", "Lisinopril", "Atorvastatina"])
    paciente = gestion_pacientes.obtener_paciente(3)
    print(paciente)

    # Eliminar un paciente
    print("\nEliminar paciente con ID 1:")
    gestion_pacientes.eliminar_paciente(1)
    print(gestion_pacientes)

    # Probar la función de búsqueda recursiva
    print("\nBuscar 'Insulina' en el historial del paciente con ID 3:")
    encontrado = paciente.buscar_en_historial("Insulina")
    print(f"¿Se encontró 'Insulina'? {'Sí' if encontrado else 'No'}")

    print("\nBuscar 'Covid-19' en el historial del paciente con ID 4:")
    encontrado = gestion_pacientes.obtener_paciente(4).buscar_en_historial("Covid-19")
    print(f"¿Se encontró 'Covid-19'? {'Sí' if encontrado else 'No'}")

    print("\nBuscar 'Migraña' en el historial del paciente con ID 4:")
    encontrado = gestion_pacientes.obtener_paciente(4).buscar_en_historial("Migraña")
    print(f"¿Se encontró 'Migraña'? {'Sí' if encontrado else 'No'}")