import csv
from gestion.paciente import Paciente


def cargar_datos_csv(sistema_gestion, archivo):
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