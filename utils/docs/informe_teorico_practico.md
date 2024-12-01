# Informe Teórico-Práctico del Proyecto: Sistema de Gestión de Pacientes y Hospitales

## 1. Introducción

El proyecto de gestión de pacientes y hospitales tiene como objetivo desarrollar un sistema que permita realizar diversas operaciones relacionadas con la administración de datos médicos. Este informe detalla las decisiones de diseño tomadas durante el desarrollo del sistema, el análisis de complejidad de las operaciones implementadas y la justificación de las estructuras de datos elegidas para resolver los problemas planteados.

## 2. Decisiones de Diseño

### 2.1. Modularidad

El sistema se ha diseñado de manera modular, dividiendo las funcionalidades en diferentes módulos y clases. Esto facilita el mantenimiento y la escalabilidad del sistema, permitiendo que diferentes partes del código se desarrollen y prueben de forma independiente. Los módulos principales incluyen:

- **Gestión de Pacientes**: Encargado de las operaciones relacionadas con los pacientes.
- **Gestión de Hospitales**: Maneja la información y relaciones entre hospitales.
- **Gestión de Diagnósticos**: Permite buscar diagnósticos a partir de síntomas.

### 2.2. Interfaz de Usuario

Se ha implementado un menú interactivo que permite a los usuarios seleccionar diferentes opciones de manera intuitiva. Esto mejora la usabilidad del sistema y permite a los usuarios realizar operaciones sin necesidad de conocimientos técnicos avanzados.

## 3. Análisis de Complejidad

El análisis de complejidad se centra en las operaciones más relevantes del sistema, considerando tanto el tiempo como el espacio:

### 3.1. Gestión de Pacientes

- **Agregar Paciente**: \(O(1)\) en el caso de un diccionario, ya que se puede acceder directamente a la clave.
- **Eliminar Paciente**: \(O(1)\) en un diccionario, permitiendo una eliminación rápida.
- **Obtener Paciente**: \(O(1)\) para obtener la información de un paciente por su ID.
- **Actualizar Paciente**: \(O(1)\) para acceder y modificar la información del paciente.

### 3.2. Operaciones con Pacientes

- **Buscar Paciente por DNI**: \(O(1)\) en un diccionario, lo que permite una búsqueda eficiente.
- **Operaciones de Rango** (IMPLEMENTACION PENDIENTE): Para operaciones que requieren un rango de IDs, se puede utilizar un árbol binario de búsqueda, que proporciona un tiempo promedio de \(O(\log n)\).

### 3.3. Gestión de Hospitales

- **Agregar Hospital**: \(O(1)\) al agregar un nuevo vértice en el grafo.
- **Buscar Rutas**: Utilizando algoritmos de búsqueda como DFS o BFS, la complejidad es \(O(V + E)\), donde \(V\) es el número de hospitales y \(E\) es el número de conexiones.

### 3.4. Gestión de Diagnósticos

- **Buscar Diagnóstico por Síntoma**: Utilizando un grafo, la complejidad también es \(O(V + E)\), permitiendo encontrar rutas entre síntomas y diagnósticos.

## 4. Justificación de las Estructuras de Datos Utilizadas

### 4.1. Diccionario

Se utilizó un diccionario para la gestión de pacientes debido a su capacidad para proporcionar acceso rápido y eficiente a los datos. Cada paciente se identifica mediante un ID único, lo que permite realizar operaciones de búsqueda, actualización y eliminación en tiempo constante.

### 4.2. Árbol Binario de Búsqueda

Se implementó un árbol binario de búsqueda para facilitar operaciones de rango y mantener los pacientes ordenados por ID. Esto es útil para realizar búsquedas eficientes y obtener pacientes dentro de un rango específico, mejorando así la capacidad de análisis de datos.

### 4.3. Grafo

El uso de grafos es fundamental para modelar las relaciones entre hospitales y diagnósticos. Los grafos permiten representar conexiones y rutas, lo que es esencial para optimizar la logística en el traslado de pacientes y en la investigación de diagnósticos. La capacidad de aplicar algoritmos como Dijkstra para encontrar rutas más cortas es una ventaja significativa en la gestión de datos médicos.

### 4.4. Cola de Prioridades

Se consideró el uso de colas de prioridades para gestionar elementos con prioridades, especialmente en algoritmos de rutas como Dijkstra. Esto permite extraer el elemento con la prioridad más alta de manera eficiente, mejorando la efectividad del sistema en situaciones críticas.

## 5. Conclusiones

El diseño del sistema de gestión de pacientes y hospitales se basa en decisiones estratégicas relacionadas con la modularidad, la usabilidad y la eficiencia. La elección de estructuras de datos adecuadas ha permitido optimizar el análisis y procesamiento de grandes volúmenes de datos médicos, mejorando la calidad de la atención médica. A medida que el sistema evoluciona, se pueden considerar nuevas estructuras de datos y algoritmos para seguir mejorando su rendimiento y adaptabilidad a las necesidades cambiantes del sector salud. La implementación de un enfoque basado en datos y estructuras de datos optimizadas es esencial para enfrentar los desafíos futuros en la gestión de información médica.