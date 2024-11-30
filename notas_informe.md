El programa es un sistema de gestión de pacientes y hospitales que permite realizar diversas operaciones relacionadas con la gestión de pacientes, hospitales y diagnósticos médicos. A continuación, se explica en detalle el flujo del programa y se justifica el uso de las estructuras de datos empleadas.

### Flujo del Programa

1. **Inicio del Programa**:
   - El programa comienza ejecutando el archivo main.py, que importa el módulo menu  y llama a la función menu_principal() para mostrar el menú principal al usuario.
2. **Menú Principal**:
   - El menu_principal() presenta al usuario un menú con cinco opciones:
     1. Gestión de Pacientes
     2. Operaciones con Pacientes
     3. Gestión de Hospitales
     4. Gestión de Diagnósticos
     5. Salir

3. **Gestión de Pacientes**:
   - Si el usuario selecciona la opción 1, se llama a menu_gestion_pacientes(sistema_gestion).
   - Este menú permite agregar, eliminar, obtener información y actualizar información de pacientes.
   - Utiliza la clase SistemaGestionPacientes para gestionar las operaciones.

4. **Operaciones con Pacientes**:
   - Si el usuario selecciona la opción 2, se llama a menu_operaciones_pacientes(sistema_gestion).
   - Este menú permite registrar, buscar y eliminar pacientes por DNI.
   - También utiliza la clase SistemaGestionPacientes.

5. **Gestión de Hospitales**:
   - Si el usuario selecciona la opción 3, se llama a menu_gestion_hospitales(grafo).
   - Este menú permite agregar hospitales, agregar conexiones entre hospitales, buscar rutas entre hospitales y calcular distancias.
   - Utiliza la clase Grafo para gestionar las operaciones.

6. **Gestión de Diagnósticos**:
   - Si el usuario selecciona la opción 4, se llama a menu_gestion_diagnosticos(grafo_diagnostico).
   - Este menú permite buscar los pasos necesarios para llegar a un diagnóstico a partir de un síntoma.
   - Utiliza la clase GrafoDiagnostico para gestionar las operaciones.

7. **Salir**:
   - Si el usuario selecciona la opción 5, el programa imprime un mensaje de salida y termina.

### Justificación del Uso de Estructuras de Datos

1. **Diccionario para Gestión de Pacientes**:
   - **Eficiencia de Búsqueda y Actualización**: Los diccionarios en Python permiten acceder, insertar y eliminar elementos en tiempo promedio constante \(O(1)\). Esto es crucial para gestionar una colección de pacientes de manera eficiente.
   - **Acceso Directo por Clave**: Cada paciente tiene un ID único que se utiliza como clave en el diccionario, permitiendo un acceso directo y rápido a los datos del paciente.

2. **Arbol Binario de Búsqueda**:
   - **Operaciones de Rango**: Los árboles binarios de búsqueda son eficientes para realizar operaciones de rango, como encontrar todos los pacientes con IDs dentro de un rango específico. Estas operaciones se pueden realizar en tiempo \(O(\log n)\) en promedio.
   - **Ordenación**: Mantener los pacientes ordenados por ID facilita la búsqueda y la eliminación de pacientes en un orden específico.

3. **Grafo**:
   - **Modelado de Relaciones**: Los grafos son ideales para modelar relaciones entre entidades, como hospitales y diagnósticos. Permiten representar conexiones y rutas entre diferentes nodos (hospitales o síntomas).
   - **Algoritmos de Búsqueda**: Los algoritmos de búsqueda en grafos, como DFS y BFS, son útiles para encontrar rutas y conexiones entre nodos. Estos algoritmos tienen una complejidad de \(O(V + E)\), donde \(V\) es el número de vértices y \(E\) es el número de aristas.
   - **Algoritmo de Dijkstra**: Utilizado para encontrar las rutas más cortas entre hospitales, es eficiente para grafos con pesos no negativos y tiene una complejidad de \(O((V + E) \log V)\) utilizando una cola de prioridades.
   
   **Grafo Hospitales**
   - Tipo: No dirigido.
   - Descripción: En este grafo, los hospitales son representados como nodos (o vértices), y las conexiones (o aristas) entre ellos representan las rutas o distancias entre los hospitales. Las aristas pueden tener un peso asociado, que generalmente representa la distancia o el costo de trasladarse de un hospital a otro. Dado que las conexiones entre hospitales no tienen una dirección específica (es decir, se puede ir de Hospital A a Hospital B y viceversa), se considera un grafo no dirigido.
   - Uso: Este tipo de grafo es útil para realizar búsquedas de rutas, calcular distancias y encontrar conexiones entre diferentes hospitales.

   **Grafo Diagnósticos**
   - Tipo: También puede ser no dirigido, dependiendo de cómo se modelen las relaciones.
   - Descripción: En este caso, los síntomas y diagnósticos son representados como nodos, y las conexiones entre ellos pueden representar relaciones de causa-efecto o pasos necesarios para llegar a un diagnóstico a partir de un síntoma. Si las relaciones son bidireccionales (por ejemplo, un síntoma puede estar relacionado con múltiples diagnósticos y viceversa), se trataría de un grafo no dirigido. Sin embargo, si se considera que hay una dirección en el proceso (de síntoma a diagnóstico), podría ser un grafo dirigido.
   - Uso: Este grafo permite realizar búsquedas para encontrar diagnósticos a partir de síntomas, facilitando la identificación de pasos necesarios para llegar a un diagnóstico médico.

4. **Cola de Prioridades**:
   - **Gestión de Prioridades**: Las colas de prioridades son útiles para gestionar elementos con prioridades, como en el algoritmo de Dijkstra. Permiten insertar elementos y extraer el elemento con la prioridad más alta en tiempo \(O(\log n)\).

### Conclusión

El uso de estas estructuras de datos está justificado por la necesidad de realizar operaciones eficientes en términos de tiempo y espacio. Los diccionarios permiten una gestión rápida de pacientes, los árboles binarios de búsqueda facilitan operaciones de rango y ordenación, los grafos modelan relaciones complejas y permiten búsquedas eficientes, y las colas de prioridades optimizan algoritmos de rutas más cortas. Estas elecciones aseguran que el sistema sea escalable y eficiente en la gestión de datos médicos y hospitalarios.