import os
from utils.inputs import (
    solicitar_hospitales,
    solcitar_rango_dni,
    solicitar_nombre,
    solicitar_fecha_nacimiento,
    solicitar_lista,
)
from utils.utilidades import (
    agregar_paciente,
    eliminar_paciente,
    obtener_paciente,
    actualizar_paciente,
    agregar_hospital,
    agregar_conexion,
    buscar_ruta,
    buscar_ruta_corta,
    agregar_diagnostico,
    modificar_diagnostico,
    eliminar_diagnostico,
    buscar_diagnostico_por_sintoma,
    generar_reporte_diagnosticos,
    buscar_paciente_rango,
    buscar_enfermedad,
    buscar_medicamento,
    listar_pacientes
)
from utils.constantes import (
    AGREGAR_PACIENTE,
    ELIMINAR_PACIENTE,
    OBTENER_PACIENTE,
    ACTUALIZAR_PACIENTE,
    VOLVER_MENU_PRINCIPAL,
    BUSCAR_PACIENTE_RANGO_DNI,
    BUSCAR_PACIENTE_ENFERMEDAD,
    BUSCAR_PACIENTE_MEDICAMENTO,
    LISTAR_PACIENTES,
    ACTUALIZAR_NOMBRE,
    ACTUALIZAR_FECHA_NACIMIENTO,
    ACTUALIZAR_HISTORIAL_ENFERMEDADES,
    ACTUALIZAR_MEDICAMENTOS,
    AGREGAR_HOSPITAL,
    AGREGAR_CONEXION,
    BUSCAR_RUTA,
    BUSCAR_RUTA_CORTA,
    CALCULAR_DISTANCIAS,
    VOLVER_MENU_HOSPITALES,
    ENCONTRAR_PASOS,
    OPERACIONES_DIAGNOSTICOS,
    VOLVER_MENU_PRINCIPAL_DIAGNOSTICOS,
    AGREGAR_DIAGNOSTICO,
    MODIFICAR_DIAGNOSTICO,
    ELIMINAR_DIAGNOSTICO,
    BUSCAR_DIAGNOSTICO_SINTOMA,
    GENERAR_REPORTE,
    VOLVER_MENU_DIAGNOSTICOS,
)


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


def manejar_opcion_operaciones_pacientes(opcion, sistema_gestion):
    if opcion == BUSCAR_PACIENTE_RANGO_DNI:
        buscar_paciente_rango(sistema_gestion)
    elif opcion == BUSCAR_PACIENTE_ENFERMEDAD:
        clave = input("Ingrese enfermedad: ").lower()
        buscar_enfermedad(sistema_gestion, clave)
    elif opcion == BUSCAR_PACIENTE_MEDICAMENTO:
        clave = input("Ingrese medicamento: ").lower()
        buscar_medicamento(sistema_gestion, clave)
    elif opcion == LISTAR_PACIENTES:
        listar_pacientes(sistema_gestion)
    elif opcion == VOLVER_MENU_PRINCIPAL:
        print("Volviendo al Menú Principal...")
    else:
        print("Opción no válida. Intente de nuevo.")


def manejar_opcion_actualizar_paciente(opcion, sistema_gestion, dni):
    if opcion == ACTUALIZAR_NOMBRE:
        nombre = solicitar_nombre()
        sistema_gestion.actualizar_paciente(dni, nombre=nombre)
    elif opcion == ACTUALIZAR_FECHA_NACIMIENTO:
        fecha_nac = solicitar_fecha_nacimiento()
        sistema_gestion.actualizar_paciente(dni, fecha_nac=fecha_nac)
    elif opcion == ACTUALIZAR_HISTORIAL_ENFERMEDADES:
        historial_enfermedades = solicitar_lista(
            "Ingrese historial de enfermedades (separadas por comas): "
        )
        sistema_gestion.actualizar_paciente(
            dni, historial_enfermedades=historial_enfermedades
        )
    elif opcion == ACTUALIZAR_MEDICAMENTOS:
        medicamentos = solicitar_lista("Ingrese medicamentos (separados por comas): ")
        sistema_gestion.actualizar_paciente(dni, medicamentos=medicamentos)
    elif opcion == VOLVER_MENU_PRINCIPAL:
        print("Volviendo al menú anterior...")
    else:
        print("Opción no válida. Intente de nuevo.")


def manejar_opcion_gestion_hospitales(opcion, grafo):
    if opcion == AGREGAR_HOSPITAL:
        agregar_hospital(grafo)
    elif opcion == AGREGAR_CONEXION:
        agregar_conexion(grafo)
    elif opcion == BUSCAR_RUTA:
        buscar_ruta(grafo)
    elif opcion == BUSCAR_RUTA_CORTA:
        buscar_ruta_corta(grafo)
    elif opcion == CALCULAR_DISTANCIAS:
        hospital = solicitar_hospitales(1)[0]
        grafo.imprimir_dijkstra(hospital)
    elif opcion == VOLVER_MENU_HOSPITALES:
        print("Volviendo al Menú Principal...")
        os.system("clear")
    else:
        print("Opción no válida. Intente de nuevo.")


def manejar_opcion_gestion_diagnosticos(
    opcion, grafo_diagnostico, menu_operaciones_diagnosticos
):
    if opcion == ENCONTRAR_PASOS:
        os.system("clear")
        sintoma = input("Ingrese el síntoma inicial: ").lower()
        diagnostico = input("Ingrese el diagnóstico: ").lower()
        camino = grafo_diagnostico.dfs(sintoma, diagnostico)
        if camino:
            print(f"Pasos necesarios para {diagnostico}: {' -> '.join(camino)}")
        else:
            print("No se encontraron pasos para este diagnóstico.")
        input("\nPresione Enter para continuar...")
    elif opcion == OPERACIONES_DIAGNOSTICOS:
        menu_operaciones_diagnosticos(grafo_diagnostico)
        os.system("clear")
    elif opcion == VOLVER_MENU_PRINCIPAL_DIAGNOSTICOS:
        continuar = False
    else:
        print("Opción no válida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")


def manejar_opcion_operaciones_diagnosticos(opcion, grafo_diagnostico):
    if opcion == AGREGAR_DIAGNOSTICO:
        agregar_diagnostico(grafo_diagnostico)
    elif opcion == MODIFICAR_DIAGNOSTICO:
        modificar_diagnostico(grafo_diagnostico)
    elif opcion == ELIMINAR_DIAGNOSTICO:
        eliminar_diagnostico(grafo_diagnostico)
    elif opcion == BUSCAR_DIAGNOSTICO_SINTOMA:
        buscar_diagnostico_por_sintoma(grafo_diagnostico)
    elif opcion == GENERAR_REPORTE:
        generar_reporte_diagnosticos(grafo_diagnostico)
    elif opcion == VOLVER_MENU_DIAGNOSTICOS:
        continuar = False
    else:
        print("Opción no válida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")
