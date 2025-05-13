import json
import os
import sys
from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor
from CustomErrorListener import CustomErrorListener

# Archivo con las consultas predefinidas
CONSULTAS_FILE = "consultas.json"

def procesar_script_desde_dsl(ruta_archivo):
    """Procesa un script DSL directamente"""
    print(f"\nProcesando script DSL desde: {ruta_archivo}")
    
    input_stream = FileStream(ruta_archivo, encoding='utf-8')
    lexer = CSVFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVFilterParser(stream)
    
    # Agregar el manejador de errores
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    
    try:
        tree = parser.prog()
        visitor = MyCSVVisitor()
        visitor.visit(tree)
        return visitor.get_results()
    except Exception as e:
        print(f"Error al procesar el script DSL: {e}")
        return []

def procesar_script_desde_json(ruta_json, consulta_id=None):
    """Procesa un script JSON convirtiéndolo a DSL"""
    print(f"\nProcesando script JSON desde: {ruta_json}")
    
    try:
        with open(ruta_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        consultas = data.get("consultas", [])
        
        # Si se especifica un ID de consulta, filtrar solo esa
        if consulta_id is not None:
            if 1 <= consulta_id <= len(consultas):
                consultas = [consultas[consulta_id - 1]]
            else:
                print(f"Error: No existe la consulta con ID {consulta_id}")
                return []
                
        # Procesar todas las consultas seleccionadas
        all_results = []
        for i, consulta in enumerate(consultas):
            if consulta_id is None:
                print(f"\nEjecutando consulta #{i+1}: {consulta.get('descripcion', 'Sin descripción')}")
            
            instrucciones = []
            
            # Extraer las operaciones
            operaciones = consulta.get("operaciones", [])
            for operacion in operaciones:
                if "tipo" in operacion and operacion["tipo"] == "load":
                    instrucciones.append(f'load "{operacion["archivo"]}";')
                elif "tipo" in operacion and operacion["tipo"] == "filter":
                    if "filter_type" in operacion and operacion["filter_type"] == "between":
                        instrucciones.append(f'filter column "{operacion["columna"]}" between {operacion["valor1"]} and {operacion["valor2"]};')
                    elif "filter_type" in operacion and operacion["filter_type"] == "in":
                        valores = ", ".join([f'"{v}"' if isinstance(v, str) else str(v) for v in operacion["valores"]])
                        instrucciones.append(f'filter column "{operacion["columna"]}" in ({valores});')
                    elif "filter_type" in operacion and operacion["filter_type"] == "like":
                        instrucciones.append(f'filter column "{operacion["columna"]}" like "{operacion["patron"]}";')
                    else:
                        valor = operacion["valor"]
                        if isinstance(valor, str) and not valor.isdigit() and not valor.startswith('"'):
                            valor = f'"{valor}"'
                        instrucciones.append(f'filter column "{operacion["columna"]}" {operacion["operador"]} {valor};')
                elif "tipo" in operacion and operacion["tipo"] == "aggregate":
                    if "condicion" in operacion:
                        condicion = operacion["condicion"]
                        instrucciones.append(f'aggregate {operacion["funcion"]} column "{operacion["columna"]}" where "{condicion["columna"]}" {condicion["operador"]} {condicion["valor"]};')
                    else:
                        instrucciones.append(f'aggregate {operacion["funcion"]} column "{operacion["columna"]}";')
                elif "tipo" in operacion and operacion["tipo"] == "sort":
                    instrucciones.append(f'sort by "{operacion["columna"]}" {operacion["orden"]};')
                elif "tipo" in operacion and operacion["tipo"] == "limit":
                    instrucciones.append(f'limit {operacion["limite"]};')
                elif "tipo" in operacion and operacion["tipo"] == "join":
                    instrucciones.append(f'join "{operacion["archivo_secundario"]}" on "{operacion["clave_primaria"]}" = "{operacion["clave_secundaria"]}";')
                elif "tipo" in operacion and operacion["tipo"] == "group":
                    instrucciones.append(f'group by "{operacion["columna"]}";')
                elif "tipo" in operacion and operacion["tipo"] == "print":
                    instrucciones.append("print;")
                # Si hay instrucciones DSL directas, incluirlas también
                elif "instruccion" in operacion:
                    instrucciones.append(operacion["instruccion"])
            
            # Combinar todas las instrucciones en un solo script DSL
            script_dsl = "\n".join(instrucciones)
            
            # Escribir el script DSL a un archivo temporal
            temp_dsl_file = "temp_script.dsl"
            with open(temp_dsl_file, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Procesar el script DSL
            results = procesar_script_desde_dsl(temp_dsl_file)
            all_results.extend(results)
            
            # Limpiar el archivo temporal
            if os.path.exists(temp_dsl_file):
                os.remove(temp_dsl_file)
        
        return all_results
        
    except Exception as e:
        print(f"Error al procesar el script JSON: {e}")
        return []

def imprimir_menu():
    """Imprime el menú de opciones"""
    print("\n===== MINI COMPILADOR DSL PARA CONSULTAS CSV =====")
    print("1. Ejecutar todas las consultas predefinidas")
    print("2. Seleccionar una consulta predefinida")
    print("3. Ejecutar un archivo DSL personalizado")
    print("4. Ejecutar un archivo JSON personalizado")
    print("0. Salir")
    print("=================================================")
    return input("Seleccione una opción: ")

def mostrar_consultas_disponibles(ruta_json=CONSULTAS_FILE):
    """Muestra las consultas disponibles en el archivo de consultas"""
    try:
        with open(ruta_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        consultas = data.get("consultas", [])
        print("\n===== CONSULTAS DISPONIBLES =====")
        for i, consulta in enumerate(consultas):
            print(f"{i+1}. {consulta.get('descripcion', 'Sin descripción')}")
        print("=================================")
        
        return len(consultas)
    except Exception as e:
        print(f"Error al leer el archivo de consultas: {e}")
        return 0

def main():
    # Verificar que exista el archivo de consultas
    if not os.path.exists(CONSULTAS_FILE):
        print(f"Error: No se encontró el archivo de consultas {CONSULTAS_FILE}")
        print("Por favor, asegúrese de que el archivo exista en el directorio actual.")
        return
    
    # Si hay argumentos de línea de comandos, procesarlos directamente
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        
        if archivo.endswith(".json"):
            procesar_script_desde_json(archivo)
        elif archivo.endswith(".dsl"):
            procesar_script_desde_dsl(archivo)
        else:
            print(f"Formato de archivo no soportado: {archivo}")
            print("Por favor proporcione un archivo .json o .dsl")
        return
        
    # Modo interactivo con menú
    while True:
        opcion = imprimir_menu()
        
        if opcion == "0":
            print("¡Hasta pronto!")
            break
            
        elif opcion == "1":
            # Ejecutar todas las consultas predefinidas
            procesar_script_desde_json(CONSULTAS_FILE)
            
        elif opcion == "2":
            # Seleccionar una consulta predefinida
            num_consultas = mostrar_consultas_disponibles()
            if num_consultas > 0:
                try:
                    consulta_id = int(input("Ingrese el número de la consulta a ejecutar: "))
                    if 1 <= consulta_id <= num_consultas:
                        procesar_script_desde_json(CONSULTAS_FILE, consulta_id)
                    else:
                        print(f"Error: El número debe estar entre 1 y {num_consultas}")
                except ValueError:
                    print("Error: Debe ingresar un número válido")
            
        elif opcion == "3":
            # Ejecutar un archivo DSL personalizado
            archivo = input("Ingrese la ruta del archivo DSL: ")
            if archivo.endswith(".dsl"):
                procesar_script_desde_dsl(archivo)
            else:
                print("Error: El archivo debe tener extensión .dsl")
            
        elif opcion == "4":
            # Ejecutar un archivo JSON personalizado
            archivo = input("Ingrese la ruta del archivo JSON: ")
            if archivo.endswith(".json"):
                procesar_script_desde_json(archivo)
            else:
                print("Error: El archivo debe tener extensión .json")
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()