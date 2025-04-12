# Actividad: Manejo de Errores con ANTLR4 en Python

## Requisitos previos
- Python 3.x
- ANTLR4 instalado
- Biblioteca ANTLR4 para Python (`pip install antlr4-python3-runtime`)

## Estructura del proyecto
- `Simple.g4`: Gramática ANTLR4 para el lenguaje Simple
- `main.py`: Programa principal para realizar pruebas
- Archivos autogenerados por ANTLR4: 
  - `SimpleLexer.py`
  - `SimpleParser.py`
  - `SimpleListener.py`
- `SimpleCustomListener.py`: Listener personalizado para procesar eventos
- `Listener.py`: Implementación del listener para detectar clases, métodos y asignaciones

## Pasos para ejecutar las pruebas

1. **Generar los archivos de ANTLR4**
   ```
   antlr4 -Dlanguage=Python3 Simple.g4
   ```

2. **Ejecutar el programa principal**
   ```
   python main.py
   ```

## Descripción de la gramática
La gramática `Simple.g4` define un lenguaje simple orientado a objetos con:
- Declaraciones de clase
- Miembros (variables y métodos)
- Sentencias de asignación
- Expresiones aritméticas (+, -, *, /)
- Llamadas a funciones

## Implementación del Listener
El archivo `Listener.py` implementa un listener personalizado que detecta:
- Declaraciones de clase
- Definiciones de métodos
- Asignaciones de variables

## Manejo de errores
El programa implementa el manejo de errores mediante:
- `VerboseErrorListener`: Clase personalizada para mostrar errores sintácticos
- Captura de excepciones durante el proceso de análisis

## Ejemplos de prueba
El `main.py` contiene varios casos de prueba con diferentes estructuras de clases y métodos para validar el funcionamiento del analizador y su capacidad para detectar elementos y manejar errores.
