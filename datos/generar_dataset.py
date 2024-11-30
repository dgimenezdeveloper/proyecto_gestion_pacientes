# src/generar_dataset.py

import csv
from faker import Faker
import random

def generar_dataset(cantidad):
    fake = Faker('es_ES')
    with open('./datos/pacientes.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['dni', 'nombre', 'fecha_nac', 'historial_enfermedades', 'medicamentos'])
        
        for _ in range(cantidad):
            dni = fake.unique.random_int(min=10000000, max=99999999)  # DNIs argentinos
            nombre = fake.name()
            fecha_nac = fake.date_of_birth(minimum_age=0, maximum_age=100).strftime("%Y-%m-%d")
            historial_enfermedades = ','.join(fake.words(nb=random.randint(1, 5), ext_word_list=None))
            medicamentos = ','.join(fake.words(nb=random.randint(1, 5), ext_word_list=None))
            
            writer.writerow([dni, nombre, fecha_nac, historial_enfermedades, medicamentos])

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad de datos ficticios a generar: "))
    generar_dataset(cantidad)
    print(f"Se han generado {cantidad} registros en el archivo 'pacientes.csv'.")