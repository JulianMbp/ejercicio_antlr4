import sys
import json
from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from CSVFilterListener import CSVFilterListener

# Importar la lista de filtros desde main.py
sys.path.append('.')
from main import filtros

def json_to_dsl(filtro):
    """Convierte un filtro en formato JSON a su representación DSL"""
    dsl_commands = []
    
    # Comando load
    dsl_commands.append('load "empleados.csv";')
    
    # Comando filter
    if "type" in filtro and filtro["type"] in ["AND", "OR"]:
        # Filtro compuesto
        conditions = []
        for condition in filtro["conditions"]:
            if "column" in condition:
                column = condition["column"]
                operator = condition["operator"]
                value = condition["value"]
                
                # Convertir operador al formato DSL
                op_map = {
                    "greater": ">",
                    "less": "<",
                    "equal": "==",
                    "not_equal": "!=",
                    "greater_equal": ">=",
                    "less_equal": "<="
                }
                dsl_op = op_map.get(operator, operator)
                
                # Si la columna es calculada, usaremos solo el nombre simple
                if column.startswith("calc:"):
                    column = "edad"  # Simplificación para columnas calculadas
                
                conditions.append(f'column "{column}" {dsl_op} {value}')
        
        # Unir condiciones con el operador correspondiente
        filter_expr = f" {filtro['type']} ".join(conditions)
        dsl_commands.append(f"filter {filter_expr};")
    else:
        # Filtro simple
        column = filtro["column"]
        operator = filtro["operator"]
        value = filtro["value"]
        
        # Convertir operador al formato DSL
        op_map = {
            "greater": ">",
            "less": "<",
            "equal": "==",
            "not_equal": "!=",
            "greater_equal": ">=",
            "less_equal": "<="
        }
        dsl_op = op_map.get(operator, ">")  # Por defecto usar ">" si no se encuentra
        
        # Si la columna es calculada, usaremos solo el nombre simple
        if column.startswith("calc:"):
            column = "edad"  # Simplificación para columnas calculadas
        
        dsl_commands.append(f'filter column "{column}" {dsl_op} {value};')
    
    # Comando print
    dsl_commands.append("print;")
    
    return "\n".join(dsl_commands)

class TreePrinter(CSVFilterListener):
    def __init__(self):
        self.indent = 0
        
    def enterEveryRule(self, ctx):
        rule_name = CSVFilterParser.ruleNames[ctx.getRuleIndex()]
        print("  " * self.indent + f"└─ {rule_name}")
        self.indent += 1
        
    def exitEveryRule(self, ctx):
        self.indent -= 1

def visualize_parse_tree(dsl_text):
    """Visualiza el árbol de análisis para un texto DSL dado"""
    # Crear el lexer
    input_stream = InputStream(dsl_text)
    lexer = CSVFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Crear el parser
    parser = CSVFilterParser(stream)
    tree = parser.prog()
    
    # Imprimir el árbol de análisis en formato legible
    print("\nÁrbol de análisis:")
    print("└─ prog")
    listener = TreePrinter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

def main():
    # Mostrar las opciones disponibles
    print("=== VISUALIZADOR DE ÁRBOLES DE ANÁLISIS ===")
    print("Selecciona un filtro para ver su árbol de análisis:")
    
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
            filtro_json = filtros[opcion-1]["filtro"]
            
            # Convertir el filtro JSON a su representación DSL
            dsl_text = json_to_dsl(filtro_json)
            
            # Mostrar el DSL generado
            print("\nTexto DSL generado:")
            print("--------------------")
            print(dsl_text)
            print("--------------------")
            
            # Visualizar el árbol de análisis
            visualize_parse_tree(dsl_text)
        else:
            print("Opción no válida")
    
    except ValueError:
        print("Por favor, introduce un número válido")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 