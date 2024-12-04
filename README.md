# Sistema de Gestión de Pacientes y Hospitales

Este programa es un sistema de gestión de pacientes y hospitales que permite realizar diversas operaciones relacionadas con la gestión de pacientes, hospitales y diagnósticos médicos.

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clona el repositorio:
    ```sh
    git clone git@github.com:dgimenezdeveloper/proyecto_gestion_pacientes.git
    cd proyecto_gestion_pacientes
    ```

2. Instala las dependencias necesarias (si las hay).

## Estructura del Proyecto

```
.
├── .gitignore                        # Archivo para ignorar archivos en Git
├── .vscode/                          # Configuraciones del entorno de desarrollo para Visual Studio Code
│   └── settings.json                 # Configuraciones específicas del proyecto
├── analisis_algoritmico/                           # Módulo para análisis algorítmico
│   ├── __init__.py                   # Inicialización del módulo
│   └── analisis_algoritmico.py       # Análisis de complejidad algorítmica
├── datos/                            # Módulo para manejar datos
│   ├── __init__.py                   # Inicialización del módulo
│   ├── datos_diagnosticos.py         # Datos de diagnósticos médicos
│   ├── datos_hospitales.py           # Datos y conexiones entre hospitales
│   ├── datos_pacientes.py            # Datos de pacientes
│   ├── generar_dataset.py            # Generador de datos ficticios
│   └── pacientes.csv                 # Archivo CSV con datos de pacientes
├── estructuras/                      # Módulo para estructuras de datos
│   ├── __init__.py                   # Inicialización del módulo
│   ├── arbol_binario.py              # Implementación de árbol binario de búsqueda
│   ├── arbol_general.py              # Implementación de árbol general
│   ├── cola_prioridades.py           # Implementación de cola de prioridades
│   └── grafo.py                      # Implementación de grafo
├── gestion/                          # Módulo para la gestión de pacientes y hospitales
│   ├── __init__.py                   # Inicialización del módulo
│   ├── gestion_pacientes.py          # Gestión de la colección de pacientes
│   ├── paciente.py                   # Clase que representa a un paciente
│   └── sistema_gestion_pacientes.py  # Sistema de gestión de pacientes
├── LICENSE                           # Archivo de licencia del proyecto
├── notas_informe.md                  # Notas y reflexiones sobre el informe del proyecto
├── README.md                         # Documentación principal del proyecto
├── src/                              # Directorio principal del código fuente
│   ├── __init__.py                   # Inicialización del módulo
│   ├── main.py                       # Punto de entrada principal de la aplicación
│   └── config.py                     # Configuración global del proyecto
└── utils/                            # Módulo de utilidades
    ├── __init__.py                   # Inicialización del módulo
    ├── inputs.py                     # Funciones para solicitar entradas al usuario
    └── logger.py                     # Configuración y manejo de logs del sistema
```

## Uso
1. Ejecuta el programa:
    ```bash
    python src/main.py
    ```

2. Selecciona la opción deseada en el menú.

3. Sigue las instrucciones interactivas para realizar las operaciones disponibles.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama (\`git checkout -b feature/nueva-caracteristica\`).
3. Realiza tus cambios y haz commit (\`git commit -am 'Añadir nueva característica'\`).
4. Sube tus cambios (\`git push origin feature/nueva-caracteristica\`).
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo \`LICENSE\` para más detalles."