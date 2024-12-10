class NodoArbol:
    """
    Clase que representa un nodo en un árbol binario de búsqueda.

    Atributos:
        paciente (Paciente): Objeto de la clase Paciente.
        izquierda (NodoArbol): Nodo hijo izquierdo.
        derecha (NodoArbol): Nodo hijo derecho.
    """
    def __init__(self, paciente):
        """
        Inicializa un nodo con el identificador del paciente y el objeto paciente.

        Args:
            paciente (Paciente): Objeto de la clase Paciente.
        """
        self.paciente = paciente
        self.id = paciente.id  # Usamos el atributo 'id' del paciente
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:
    """
    Clase que representa un árbol binario de búsqueda.

    Atributos:
        raiz (NodoArbol): Nodo raíz del árbol.
    """
    def __init__(self):
        """
        Inicializa un árbol binario de búsqueda vacío.
        """
        self.raiz = None

    def insertar(self, paciente):
        """
        Inserta un nuevo nodo en el árbol binario de búsqueda.

        Args:
            paciente (Paciente): Objeto de la clase Paciente.
        """
        if self.raiz is None:
            self.raiz = NodoArbol(paciente)
        else:
            self._insertar_recursivo(self.raiz, paciente)

    def _insertar_recursivo(self, nodo, paciente):
        """
        Inserta un nuevo nodo en el árbol binario de búsqueda de manera recursiva.

        Args:
            nodo (NodoArbol): Nodo actual en el que se está realizando la inserción.
            paciente (Paciente): Objeto de la clase Paciente.
        """
        if paciente.id < nodo.id:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(paciente)
            else:
                self._insertar_recursivo(nodo.izquierda, paciente)
        elif paciente.id > nodo.id:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(paciente)
            else:
                self._insertar_recursivo(nodo.derecha, paciente)

    def buscar(self, id):
        """
        Busca un nodo en el árbol binario de búsqueda.

        Args:
            id (int): ID del paciente a buscar.

        Returns:
            NodoArbol: Nodo que contiene el paciente buscado, o None si no se encuentra.
        """
        return self._buscar_recursivo(self.raiz, id)

    def _buscar_recursivo(self, nodo, id):
        """
        Busca un nodo en el árbol binario de búsqueda de manera recursiva.

        Args:
            nodo (NodoArbol): Nodo actual en el que se está realizando la búsqueda.
            id (int): ID del paciente a buscar.

        Returns:
            NodoArbol: Nodo que contiene el paciente buscado, o None si no se encuentra.
        """
        if nodo is None or nodo.id == id:
            return nodo
        if id < nodo.id:
            return self._buscar_recursivo(nodo.izquierda, id)
        return self._buscar_recursivo(nodo.derecha, id)

    def buscar_por_enfermedad(self, enfermedad):
        """
        Busca un nodo en el árbol binario de búsqueda por enfermedad.

        Args:
            nodo (NodoArbol): Nodo actual en el que se está realizando la búsqueda.
            enfermedad (str): Enfermedad a buscar en el historial de tratamientos.

        Returns:
            NodoArbol: Nodo que contiene el paciente con la enfermedad buscada, o None si no se encuentra.
        """
        resultados = []
        self._buscar_por_enfermedad_recursivo(self.raiz, enfermedad, resultados)
        return resultados
    
    def _buscar_por_enfermedad_recursivo(self, nodo, enfermedad, resultados):
        """
        Busca un nodo en el árbol binario de búsqueda por enfermedad de manera recursiva.

        Args:
            nodo (NodoArbol): Nodo actual en el que se está realizando la búsqueda.
            enfermedad (str): Enfermedad a buscar en el historial de tratamientos.
            resultados (list): Lista de resultados para almacenar los pacientes con la enfermedad buscada.
        """
        if nodo is None:
            return
        if nodo.paciente.buscar_en_historial(enfermedad):
            resultados.append(nodo.paciente)
        self._buscar_por_enfermedad_recursivo(nodo.izquierda, enfermedad, resultados)
        self._buscar_por_enfermedad_recursivo(nodo.derecha, enfermedad, resultados)
    
    def buscar_por_medicamento(self, medicamento):
        """
        Busca un nodo en el árbol binario de búsqueda por medicamento.

        Args:
            nodo (NodoArbol): Nodo actual en el que se está realizando la búsqueda.
            medicamento (str): Medicamento a buscar en el historial de tratamientos.

        Returns:
            NodoArbol: Nodo que contiene el paciente con el medicamento buscado, o None si no se encuentra.
        """
        resultados = []
        self._buscar_por_medicamento_recursivo(self.raiz, medicamento, resultados)
        return resultados
    
    def _buscar_por_medicamento_recursivo(self, nodo, medicamento, resultados):
        """
        Busca un nodo en el árbol binario de búsqueda por medicamento de manera recursiva.

        Args:
            nodo (NodoArbol): Nodo actual en el que se está realizando la búsqueda.
            medicamento (str): Medicamento a buscar en el historial de tratamientos.
            resultados (list): Lista de resultados para almacenar los pacientes con el medicamento buscado.
        """
        if nodo is None:
            return
        if nodo.paciente.buscar_en_historial(medicamento):
            resultados.append(nodo.paciente)
        self._buscar_por_medicamento_recursivo(nodo.izquierda, medicamento, resultados)
        self._buscar_por_medicamento_recursivo(nodo.derecha, medicamento, resultados)
    
    def eliminar(self, id):
        """
        Elimina un nodo del árbol binario de búsqueda.

        Args:
            id (int): ID del paciente a eliminar.
        """
        self.raiz = self._eliminar_recursivo(self.raiz, id)

    def _eliminar_recursivo(self, nodo, id):
        """
        Elimina un nodo del árbol binario de búsqueda de manera recursiva.

        Args:
            nodo (NodoArbol): Nodo actual en el que se está realizando la eliminación.
            id (int): ID del paciente a eliminar.

        Returns:
            NodoArbol: Nodo resultante después de la eliminación.
        """
        if nodo is None:
            return nodo
        if id < nodo.id:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, id)
        elif id > nodo.id:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, id)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minimo_valor_nodo(nodo.derecha)
            nodo.id = temp.id
            nodo.paciente = temp.paciente
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, temp.id)
        return nodo

    def _minimo_valor_nodo(self, nodo):
        """
        Encuentra el nodo con el valor mínimo en el árbol binario de búsqueda.

        Args:
            nodo (NodoArbol): Nodo a partir del cual buscar el valor mínimo.

        Returns:
            NodoArbol: Nodo con el valor mínimo.
        """
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def obtener_pacientes_rango(self, id_min, id_max):
        """
        Obtiene los pacientes en un rango de IDs.

        Args:
            id_min (int): ID mínimo del rango.
            id_max (int): ID máximo del rango.

        Returns:
            list: Lista de objetos de la clase Paciente en el rango especificado.
        """
        resultado = []
        self._obtener_pacientes_rango_recursivo(self.raiz, id_min, id_max, resultado)
        return resultado

    def _obtener_pacientes_rango_recursivo(self, nodo, id_min, id_max, resultado):
        """
        Función auxiliar recursiva para obtener pacientes en un rango de IDs.

        Args:
            nodo (NodoArbol): Nodo actual del árbol binario de búsqueda.
            id_min (int): ID mínimo del rango.
            id_max (int): ID máximo del rango.
            resultado (list): La lista de resultados para almacenar los pacientes.
        """
        if nodo is None:
            return
        if id_min <= nodo.id <= id_max:
            resultado.append(nodo.paciente)
        if id_min < nodo.id:
            self._obtener_pacientes_rango_recursivo(nodo.izquierda, id_min, id_max, resultado)
        if nodo.id < id_max:
            self._obtener_pacientes_rango_recursivo(nodo.derecha, id_min, id_max, resultado)
    
    def listar_pacientes_ordenados(self):
        """
        Lista los pacientes en orden ascendente de ID.

        Returns:
            list: Lista de objetos de la clase Paciente ordenados por ID.
        """
        resultado = []
        self._listar_pacientes_ordenados_recursivo(self.raiz, resultado)
        return resultado
    
    def _listar_pacientes_ordenados_recursivo(self, nodo, resultado):
        """
        Función auxiliar recursiva para listar pacientes en orden ascendente de ID.

        Args:
            nodo (NodoArbol): Nodo actual del árbol binario de búsqueda.
            resultado (list): La lista de resultados para almacenar los pacientes.
        """
        if nodo is not None:
            self._listar_pacientes_ordenados_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.paciente)
            self._listar_pacientes_ordenados_recursivo(nodo.derecha, resultado)