# src/main.py

import sys
import os

# Agrega el directorio raíz del proyecto a la ruta de búsqueda de módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from menu import menu_principal

if __name__ == "__main__":
    menu_principal()