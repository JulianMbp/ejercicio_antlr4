import json
import csv
import sys
import os
from json_parser import JSONProcessor

def ejecutar_consulta(config):
    """Ejecuta una consulta con la configuración dada"""
    temp_file = "_temp_query.json"
    with open(temp_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2)
    
    print("\nEjecutando filtro...")
    processor = JSONProcessor(temp_file)
    processor.process()
    
    # Eliminar archivo temporal
    try:
        os.remove(temp_file)
    except:
        pass

def main():
    # Archivo CSV por defecto
    csv_file = "empleados.csv"
    
    print("=== FILTRADOR CSV ===")
    print("Selecciona un filtro para aplicar a tus datos:")
    
    # Lista de filtros predefinidos
    filtros = [
        # Filtros básicos de edad
        {"desc": "Edad mayor que 25", "filtro": {"column": "edad", "operator": "greater", "value": 25}},
        {"desc": "Edad menor que 30", "filtro": {"column": "edad", "operator": "less", "value": 30}},
        {"desc": "Edad igual a 40", "filtro": {"column": "edad", "operator": "equal", "value": 40}},
        {"desc": "Edad entre 30 y 40", "filtro": {"column": "edad", "operator": "in_range", "value": [30, 40]}},
        
        # Filtros de números pares/impares
        {"desc": "IDs pares", "filtro": {"column": "id", "operator": "even", "value": True}},
        {"desc": "IDs impares", "filtro": {"column": "id", "operator": "odd", "value": True}},
        {"desc": "Edades pares", "filtro": {"column": "edad", "operator": "even", "value": True}},
        {"desc": "Edades impares", "filtro": {"column": "edad", "operator": "odd", "value": True}},
        
        # Filtros de salario
        {"desc": "Salario mayor a 5 millones", "filtro": {"column": "salario", "operator": "greater", "value": 5000000}},
        {"desc": "Salario menor a 3 millones", "filtro": {"column": "salario", "operator": "less", "value": 3000000}},
        {"desc": "Salario entre 3 y 5 millones", "filtro": {"column": "salario", "operator": "in_range", "value": [3000000, 5000000]}},
        
        # Filtros de texto
        {"desc": "Nombres que contienen 'García'", "filtro": {"column": "nombre", "operator": "contains", "value": "García"}},
        {"desc": "Nombres que contienen 'López'", "filtro": {"column": "nombre", "operator": "contains", "value": "López"}},
        {"desc": "Nombres que terminan con 'ez'", "filtro": {"column": "nombre", "operator": "ends_with", "value": "ez"}},
        {"desc": "Nombres que comienzan con 'A'", "filtro": {"column": "nombre", "operator": "starts_with", "value": "A"}},
        
        # Filtros de longitud de texto
        {"desc": "Nombres con más de 15 caracteres", "filtro": {"column": "nombre", "operator": "length_greater", "value": 15}},
        {"desc": "Nombres con menos de 10 caracteres", "filtro": {"column": "nombre", "operator": "length_less", "value": 10}},
        
        # Filtros de días laborados
        {"desc": "Más de 2000 días laborados", "filtro": {"column": "dias_laborados", "operator": "greater", "value": 2000}},
        {"desc": "Menos de 1000 días laborados", "filtro": {"column": "dias_laborados", "operator": "less", "value": 1000}},
        {"desc": "Días laborados entre 1000 y 2000", "filtro": {"column": "dias_laborados", "operator": "in_range", "value": [1000, 2000]}},
        
        # Filtros con divisibilidad
        {"desc": "ID divisible por 5", "filtro": {"column": "id", "operator": "mod", "value": 5}},
        {"desc": "ID divisible por 3", "filtro": {"column": "id", "operator": "mod", "value": 3}},
        {"desc": "Días laborados divisibles por 100", "filtro": {"column": "dias_laborados", "operator": "mod", "value": 100}},
        
        # Filtros de valores absolutos
        {"desc": "Valor absoluto de edad - 40 menor que 5", "filtro": {"column": "calc:abs(int({edad}) - 40)", "operator": "less", "value": 5}},
        {"desc": "Valor absoluto de días laborados - 1500 menor que 100", "filtro": {"column": "calc:abs(int({dias_laborados}) - 1500)", "operator": "less", "value": 100}},
        
        # Filtros combinados con AND
        {"desc": "Edad > 30 AND salario > 4000000", "filtro": {"type": "AND", "conditions": [
            {"column": "edad", "operator": "greater", "value": 30},
            {"column": "salario", "operator": "greater", "value": 4000000}
        ]}},
        {"desc": "Nombres con 'ez' AND días laborados > 2000", "filtro": {"type": "AND", "conditions": [
            {"column": "nombre", "operator": "ends_with", "value": "ez"},
            {"column": "dias_laborados", "operator": "greater", "value": 2000}
        ]}},
        
        # Filtros combinados con OR
        {"desc": "Edad < 30 OR salario > 6000000", "filtro": {"type": "OR", "conditions": [
            {"column": "edad", "operator": "less", "value": 30},
            {"column": "salario", "operator": "greater", "value": 6000000}
        ]}},
        {"desc": "Nombres con 'García' OR 'López'", "filtro": {"type": "OR", "conditions": [
            {"column": "nombre", "operator": "contains", "value": "García"},
            {"column": "nombre", "operator": "contains", "value": "López"}
        ]}},
        
        # Filtros estadísticos
        {"desc": "Salarios atípicos (outliers)", "filtro": {"column": "salario", "operator": "outlier", "value": 6000000}},
        {"desc": "Edades atípicas (outliers)", "filtro": {"column": "edad", "operator": "outlier", "value": 55}},
        
        # Filtros de cálculos
        {"desc": "Edad multiplicada por días > 50000", "filtro": {"column": "calc:int({edad}) * int({dias_laborados})", "operator": "greater", "value": 50000}},
        {"desc": "Salario / edad > 100000", "filtro": {"column": "calc:int({salario}) / int({edad})", "operator": "greater", "value": 100000}},
        
        # Filtros complejos
        {"desc": "Personas menores a 30 años con salario alto", "filtro": {"type": "AND", "conditions": [
            {"column": "edad", "operator": "less", "value": 30},
            {"column": "salario", "operator": "greater", "value": 5000000}
        ]}},
        {"desc": "Personas mayores a 50 años con pocos días laborados", "filtro": {"type": "AND", "conditions": [
            {"column": "edad", "operator": "greater", "value": 50},
            {"column": "dias_laborados", "operator": "less", "value": 1000}
        ]}},
        {"desc": "Salario per día > 3000", "filtro": {"column": "calc:int({salario}) / int({dias_laborados})", "operator": "greater", "value": 3000}},
        {"desc": "Personas con apellido 'ez' O con muchos días", "filtro": {"type": "OR", "conditions": [
            {"column": "nombre", "operator": "ends_with", "value": "ez"},
            {"column": "dias_laborados", "operator": "greater", "value": 3000}
        ]}},
        {"desc": "Personas con ID par Y nombre corto", "filtro": {"type": "AND", "conditions": [
            {"column": "id", "operator": "even", "value": True},
            {"column": "nombre", "operator": "length_less", "value": 12}
        ]}}
    ]
    
    # Mostrar las opciones disponibles
    for i, filtro in enumerate(filtros, 1):
        print(f"{i}. {filtro['desc']}")
    
    # Añadir opción para salir
    print(f"{len(filtros) + 1}. Salir")
    
    # Obtener elección del usuario
    try:
        opcion = int(input("\nSelecciona una opción: "))
        
        if opcion == len(filtros) + 1:
            print("¡Hasta luego!")
            return
        
        if 1 <= opcion <= len(filtros):
            # Crear la configuración completa
            config = {
                "source": {
                    "file": csv_file
                },
                "filters": [filtros[opcion-1]["filtro"]],
                "aggregations": [
                    {
                        "type": "count",
                        "column": "id"
                    },
                    {
                        "type": "average",
                        "column": "salario"
                    },
                    {
                        "type": "sum",
                        "column": "dias_laborados"
                    }
                ],
                "output": {
                    "print": True,
                    "max_rows": 10
                }
            }
            
            # Ejecutar la consulta
            ejecutar_consulta(config)
        else:
            print("Opción no válida")
    
    except ValueError:
        print("Por favor, introduce un número válido")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main() 