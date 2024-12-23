from datetime import datetime

def solicitar_dni():
    while True:
        try:
            dni = input("Ingrese DNI: ").strip()
            if not dni:
                print("Error: El DNI no puede estar vacío.")
                continue
            return int(dni)
        except ValueError:
            print("Error: El DNI debe ser un número entero.")

def solcitar_rango_dni():
    while True:
        try:
            minimo = int(input("Ingrese el mínimo del rango de DNI: ").strip())
            maximo = int(input("Ingrese el máximo del rango de DNI: ").strip())
            if minimo > maximo:
                print("Error: El mínimo del rango no puede ser mayor que el máximo.")
                continue
            return minimo, maximo
        except ValueError:
            print("Error: El rango debe ser un número entero.")

def solicitar_nombre():
    while True:
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
        else:
            return nombre

def solicitar_fecha_nacimiento():
    while True:
        fecha_nac = input("Fecha de Nacimiento (DD-MM-YYYY): ")
        try:
            # Convertir de DD-MM-YYYY a YYYY-MM-DD
            fecha_nac_formateada = datetime.strptime(fecha_nac, "%d-%m-%Y").strftime("%Y-%m-%d")
            return fecha_nac_formateada
        except ValueError:
            print("Error: La fecha de nacimiento debe estar en el formato DD-MM-YYYY.")

def solicitar_lista(mensaje):
    return input(mensaje).split(",")

def solicitar_hospitales(cantidad):
    if cantidad == 1:
        hospital = input("Ingrese el nombre del hospital: ").strip()
        return (hospital,)
    elif cantidad == 2:
        hospital1 = input("Ingrese el nombre del primer hospital: ").strip()
        hospital2 = input("Ingrese el nombre del segundo hospital: ").strip()
        return (hospital1, hospital2)
    else:
        raise ValueError("Cantidad inválida. Solo se permiten 1 o 2 hospitales.")