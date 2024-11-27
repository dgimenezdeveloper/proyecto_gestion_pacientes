# Sistema de Gestión de Pacientes y Hospitales

Este programa es un sistema de gestión de pacientes y hospitales que permite realizar diversas operaciones relacionadas con la gestión de pacientes, hospitales y diagnósticos médicos.

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Instala las dependencias necesarias (si las hay).

## Estructura del Proyecto

- `src/`
  - `main.py`: Punto de entrada del programa.
  - `menu.py`: Contiene las funciones para mostrar los menús y gestionar las opciones seleccionadas por el usuario.
  - `gestion/`
    - `__init__.py`: Inicializa el módulo de gestión.
    - `sistema_gestion_pacientes.py`: Contiene la clase `SistemaGestionPacientes` para gestionar pacientes.
    - `paciente.py`: Contiene las clases `Paciente` y `GestionPacientes`.
  - `datos/`
    - `__init__.py`: Inicializa el módulo de datos.
    - `datos_diagnosticos.py`: Contiene la función `obtener_datos_diagnosticos`.
    - `datos_hospitales.py`: Contiene las funciones `obtener_datos_hospitales` y `cargar_datos_hospitales`.
  - `estructuras/`
    - `__init__.py`: Inicializa el módulo de estructuras.
    - `arbol_binario.py`: Contiene las clases `ArbolBinarioBusqueda` y `NodoArbol`.
    - `arbol_general.py`: Contiene las clases `ArbolGeneral` y `NodoGeneral`.
    - `cola_prioridades.py`: Contiene la clase `ColaPrioridades`.
    - `grafo.py`: Contiene la clase `Grafo`.
  - `utils/`
    - `__init__.py`: Inicializa el módulo de utilidades.
    - `inputs.py`: Contiene funciones para solicitar datos al usuario.

## Uso
1. Ejecuta el programa:
    ```bash
    python src/main.py
    ```

2. Selecciona la opción deseada en el menú.

3. Sigue las instrucciones interactivas para realizar las operaciones disponibles.

## Estructura del Proyecto

```plaintext
📁 src/
├── main.py                     # Punto de entrada principal del programa.
├── menu.py                     # Maneja los menús interactivos.
├── gestion/
│   ├── __init__.py             # Inicialización del módulo de gestión.
│   ├── sistema_gestion_pacientes.py  # Clase para gestionar pacientes.
│   └── paciente.py             # Clases relacionadas con pacientes.
├── datos/
│   ├── __init__.py             # Inicialización del módulo de datos.
│   ├── datos_diagnosticos.py   # Datos de diagnósticos médicos.
│   └── datos_hospitales.py     # Datos y conexiones entre hospitales.
├── estructuras/
│   ├── __init__.py             # Inicialización del módulo de estructuras.
│   ├── arbol_binario.py        # Árbol binario de búsqueda.
│   ├── arbol_general.py        # Árbol general para modelado de datos.
│   ├── cola_prioridades.py     # Cola de prioridades.
│   └── grafo.py                # Grafo para modelado de relaciones.
└── utils/
    ├── __init__.py             # Inicialización del módulo de utilidades.
    └── inputs.py               # Funciones auxiliares para entradas de usuario.