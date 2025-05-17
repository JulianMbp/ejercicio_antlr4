import json
import os
import sys
import subprocess
import tempfile
from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor
from CustomErrorListener import CustomErrorListener
import csv

# Archivo con las consultas predefinidas
CONSULTAS_FILE = "consultas.json"

def procesar_script_desde_dsl(ruta_archivo, mostrar_mensajes=False, mostrar_resultados=True, mostrar_vista_previa=False):
    """Procesa un script DSL directamente"""
    
    input_stream = FileStream(ruta_archivo, encoding='utf-8')
    lexer = CSVFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVFilterParser(stream)
    
    # Agregar el manejador de errores
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    
    try:
        tree = parser.prog()
        visitor = MyCSVVisitor(mostrar_carga=mostrar_vista_previa)  # Controlar si se muestra la vista previa
        visitor.visit(tree)
        
        if mostrar_resultados:
            print("\nResultados:")
            
            # Verificar si hay resultados de agregación 
            if visitor.aggregations and len(visitor.aggregations) > 0:
                print("=" * 50)
                for agg_name, agg_value in visitor.aggregations.items():
                    # Formatear el valor si es un número para mayor legibilidad
                    formatted_value = agg_value
                    if isinstance(agg_value, (int, float)):
                        if agg_value.is_integer() if isinstance(agg_value, float) else True:
                            formatted_value = f"{int(agg_value):,}"
                        else:
                            formatted_value = f"{agg_value:,.2f}"
                            
                    print(f"{agg_name}: {formatted_value}")
                print("=" * 50)
                # Solo devolver los resultados de agregación
                return visitor.get_results()
                
            # Para otros tipos de resultados (filtros, etc.), mostrar registros
            elif visitor.filtered_data and len(visitor.filtered_data) > 0:
                # Asegurar que las columnas se muestren en un orden específico para mejor lectura
                preferred_order = ["id_evento", "nombre_evento", "tipo_evento", "fecha", "lugar", "costo_entrada", "cantidad_asistentes", "estado_evento"]
                headers = preferred_order + [h for h in visitor.filtered_data[0].keys() if h not in preferred_order]
                
                # Calcular el ancho para cada columna
                widths = {}
                for h in headers:
                    # Ancho mínimo es el título de la columna
                    widths[h] = max(len(h), 10)
                    for row in visitor.filtered_data:
                        if h in row:
                            value_width = len(str(row[h]))
                            if value_width > widths[h]:
                                widths[h] = min(value_width, 30)  # Máximo ancho de 30 caracteres
                
                # Imprimir encabezado
                header_row = " | ".join([f"{h:{widths[h]}}" for h in headers if h in widths])
                print(header_row)
                print("-" * len(header_row))
                
                # Mostrar filas
                for row in visitor.filtered_data:
                    row_values = []
                    for h in headers:
                        if h in row:
                            value = str(row[h])
                            # Truncar valores largos
                            if len(value) > widths[h]:
                                value = value[:widths[h]-3] + "..."
                            row_values.append(f"{value:{widths[h]}}")
                        else:
                            row_values.append(" " * widths[h])
                    print(" | ".join(row_values))
                
                print(f"\nTotal de registros: {len(visitor.filtered_data)}")
            else:
                print("No se encontraron registros que cumplan con los filtros.")
        
        return visitor.get_results()
    except Exception as e:
        if mostrar_mensajes:
            print(f"Error al procesar el script DSL: {e}")
        import traceback
        traceback.print_exc()
        return []

def mostrar_analisis_lexico(dsl_content, verbose=True):
    """Muestra los tokens generados por el analizador léxico"""
    if verbose:
        print("\n===== ANÁLISIS LÉXICO =====")
    
    # Crear un archivo temporal con el contenido DSL
    with tempfile.NamedTemporaryFile(suffix='.dsl', delete=False, mode='w', encoding='utf-8') as temp_file:
        temp_file.write(dsl_content)
        temp_dsl = temp_file.name
    
    try:
        # Ejecutar antlr4-parse con la opción -tokens para obtener la salida sin procesar
        comando = f"cat {temp_dsl} | antlr4-parse CSVFilter.g4 prog -tokens"
        print(f"Ejecutando: {comando}")
        
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()
        
        # Mostrar la salida tal cual la genera antlr4
        if salida:
            salida_str = salida.decode('utf-8')
            print(salida_str)
        
        # Mostrar los errores tal cual los genera antlr4
        if error:
            error_str = error.decode('utf-8')
            print(error_str)
            
        # También obtener los tokens usando la API de Python para devolver para uso interno
        input_stream = InputStream(dsl_content)
        lexer = CSVFilterLexer(input_stream)
        tokens = lexer.getAllTokens()
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
            
        return tokens
    except Exception as e:
        if verbose:
            print(f"Error en el análisis léxico: {e}")
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
        return []

def mostrar_analisis_sintactico(dsl_content, verbose=True):
    """Muestra el árbol sintáctico en formato de texto"""
    if verbose:
        print("\n===== ANÁLISIS SINTÁCTICO =====")
    
    # Crear un archivo temporal con el contenido DSL
    with tempfile.NamedTemporaryFile(suffix='.dsl', delete=False, mode='w', encoding='utf-8') as temp_file:
        temp_file.write(dsl_content)
        temp_dsl = temp_file.name
    
    try:
        # Ejecutar antlr4-parse con la opción -tree para obtener la salida sin procesar
        comando = f"cat {temp_dsl} | antlr4-parse CSVFilter.g4 prog -tree"
        print(f"Ejecutando: {comando}")
        
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()
        
        # Mostrar la salida tal cual la genera antlr4
        if salida:
            salida_str = salida.decode('utf-8')
            print(salida_str)
        
        # Mostrar los errores tal cual los genera antlr4
        if error:
            error_str = error.decode('utf-8')
            print(error_str)
        
        # También crear el árbol usando la API de Python para devolver para uso interno
        input_stream = InputStream(dsl_content)
        lexer = CSVFilterLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CSVFilterParser(stream)
        
        # Agregar el manejador de errores
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())
        
        # Obtener el árbol sintáctico
        tree = parser.prog()
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
            
        return tree
    except Exception as e:
        if verbose:
            print(f"Error en el análisis sintáctico: {e}")
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
        return None

def mostrar_arbol_sintactico_gui(dsl_content):
    """Muestra el árbol sintáctico con interfaz gráfica usando antlr4-parse"""
    print("\n===== VISUALIZACIÓN DEL ÁRBOL SINTÁCTICO =====")
    
    # Crear un archivo temporal con el contenido DSL
    with tempfile.NamedTemporaryFile(suffix='.dsl', delete=False, mode='w', encoding='utf-8') as temp_file:
        temp_file.write(dsl_content)
        temp_dsl = temp_file.name
    
    try:
        # Construir el comando para usar antlr4-parse con -gui
        # Asegúrate de que el archivo CSVFilter.g4 esté en el directorio actual
        comando = f"cat {temp_dsl} | antlr4-parse CSVFilter.g4 prog -gui"
        
        print(f"Ejecutando: {comando}")
        
        # Ejecutar el comando y mostrar la salida sin procesar
        proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida, error = proceso.communicate()
        
        # Mostrar la salida tal cual la genera antlr4
        if salida:
            salida_str = salida.decode('utf-8')
            print(salida_str)
        
        # Mostrar los errores tal cual los genera antlr4
        if error:
            error_str = error.decode('utf-8')
            print(error_str)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
            
        return proceso.returncode == 0
    except Exception as e:
        print(f"Error al visualizar el árbol sintáctico: {e}")
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
        return False

def procesar_script_desde_json(ruta_json, consulta_id=None, mostrar_mensajes=True, mostrar_lexico=False, mostrar_sintactico=False, mostrar_arbol_gui=False):
    """Procesa un script JSON convirtiéndolo a DSL"""
    if mostrar_mensajes:
        print(f"\nProcesando consulta desde: {ruta_json}")
    
    try:
        with open(ruta_json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Verificar si es un JSON de consulta única sin array "consultas"
        if "operaciones" in data:
            consultas = [data]
        else:
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
            if consulta_id is None and len(consultas) > 1 and mostrar_mensajes:
                print(f"\nEjecutando consulta #{i+1}: {consulta.get('descripcion', 'Sin descripción')}")
            elif mostrar_mensajes:
                print(f"\n{consulta.get('descripcion', 'Ejecutando consulta')}")
            
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
            
            # Si se solicita análisis léxico, mostrarlo
            if mostrar_lexico:
                print(f"\nConsulta DSL generada para '{consulta.get('descripcion', 'Consulta')}': \n{script_dsl}")
                mostrar_analisis_lexico(script_dsl)
            
            # Si se solicita análisis sintáctico, mostrarlo
            if mostrar_sintactico:
                print(f"\nAnálisis sintáctico para '{consulta.get('descripcion', 'Consulta')}':")
                mostrar_analisis_sintactico(script_dsl)
            
            # Si se solicita visualización del árbol, mostrarla
            if mostrar_arbol_gui:
                print(f"\nVisualizando árbol sintáctico para '{consulta.get('descripcion', 'Consulta')}':")
                mostrar_arbol_sintactico_gui(script_dsl)
            
            # Escribir el script DSL a un archivo temporal
            temp_dsl_file = "temp_script.dsl"
            with open(temp_dsl_file, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Procesar el script DSL y obtener resultados
            # Solo mostrar resultados una vez al final del procesamiento
            archivo_csv = None
            for op in operaciones:
                if op.get("tipo") == "load":
                    archivo_csv = op.get("archivo")
                    break

            if archivo_csv and mostrar_mensajes:
                try:
                    with open(archivo_csv, newline='', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        total_rows = sum(1 for _ in reader)
                        print(f"Archivo '{archivo_csv}' cargado: {total_rows} registros")
                except Exception as e:
                    print(f"Error al cargar archivo: {e}")
            
            # Procesar el script sin mostrar resultados intermedios
            results = procesar_script_desde_dsl(temp_dsl_file, mostrar_mensajes=False, mostrar_resultados=False, mostrar_vista_previa=False)
            all_results.extend(results)
            
            # Mostrar resultados una sola vez de forma estandarizada
            if results:
                print("\nResultados:")
                print("=" * 80)
                
                # Determinar columnas dinámicamente
                if results and isinstance(results[0], dict):
                    columnas = list(results[0].keys())
                    # Calcular el ancho de cada columna
                    anchos = {}
                    for col in columnas:
                        # Ancho mínimo es la longitud del nombre de la columna
                        anchos[col] = len(str(col))
                        # Encontrar el valor más largo para cada columna
                        for row in results:
                            valor = str(row.get(col, ""))
                            if len(valor) > anchos[col]:
                                anchos[col] = len(valor)
                    
                    # Imprimir cabecera
                    header = "| "
                    for col in columnas:
                        header += str(col).ljust(anchos[col]) + " | "
                    print(header)
                    print("-" * len(header))
                    
                    # Imprimir filas
                    for row in results:
                        fila = "| "
                        for col in columnas:
                            valor = str(row.get(col, ""))
                            fila += valor.ljust(anchos[col]) + " | "
                        print(fila)
                    
                    print("=" * 80)
                    print(f"Total de registros: {len(results)}")
                else:
                    # Si no es un diccionario, mostrar de forma plana
                    for result in results:
                        print(result)
            else:
                print("\nNo se encontraron resultados.")
            
            # Limpiar el archivo temporal
            if os.path.exists(temp_dsl_file):
                os.remove(temp_dsl_file)
                
            # Imprimir una línea para separar resultados
            if i < len(consultas) - 1 and mostrar_mensajes:
                print("\n" + "="*50)
        
        return all_results
        
    except Exception as e:
        if mostrar_mensajes:
            print(f"Error al procesar el script JSON: {e}")
            import traceback
            traceback.print_exc()
        return []

def imprimir_menu():
    """Imprime el menú de opciones"""
    print("\n===== MINI COMPILADOR DSL PARA CONSULTAS CSV =====")
    print("1. Filtrar por costo de entrada")
    print("2. Filtrar por tipo de evento")
    print("3. Filtrar por lugar")
    print("4. Estadísticas de eventos")
    print("5. Filtros avanzados (combinados)")
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
    # Verificar que exista el archivo de eventos.csv
    if not os.path.exists("eventos.csv"):
        print("Error: No se encontró el archivo eventos.csv")
        print("Por favor, asegúrese de que el archivo exista en el directorio actual.")
        return
    
    # Si hay argumentos de línea de comandos, procesarlos directamente
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        
        # Verificar opciones adicionales
        mostrar_lexico = "--lexico" in sys.argv
        mostrar_sintactico = "--sintactico" in sys.argv
        mostrar_arbol_gui = "--arbol" in sys.argv
        
        # Verificar si se especifica un ID de consulta específico
        consulta_id = None
        for arg in sys.argv:
            if arg.startswith("--id="):
                try:
                    consulta_id = int(arg.split("=")[1])
                except ValueError:
                    print("Error: El argumento --id debe tener un número entero")
                    return
        
        if archivo.endswith(".json"):
            procesar_script_desde_json(archivo, consulta_id=consulta_id, 
                                      mostrar_lexico=mostrar_lexico, 
                                      mostrar_sintactico=mostrar_sintactico, 
                                      mostrar_arbol_gui=mostrar_arbol_gui)
        elif archivo.endswith(".dsl"):
            # Para archivos DSL, si se solicita análisis léxico o sintáctico, hacerlo directamente
            if mostrar_lexico or mostrar_sintactico or mostrar_arbol_gui:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                
                if mostrar_lexico:
                    mostrar_analisis_lexico(contenido)
                
                if mostrar_sintactico:
                    mostrar_analisis_sintactico(contenido)
                
                if mostrar_arbol_gui:
                    mostrar_arbol_sintactico_gui(contenido)
            
            # Procesar el archivo DSL normalmente
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
            # Filtrar por costo de entrada
            menu_filtrar_por_costo()
            
        elif opcion == "2":
            # Filtrar por tipo de evento
            menu_filtrar_por_tipo()
            
        elif opcion == "3":
            # Filtrar por lugar
            menu_filtrar_por_lugar()
            
        elif opcion == "4":
            # Estadísticas de eventos
            menu_estadisticas()
            
        elif opcion == "5":
            # Filtros avanzados combinados
            menu_filtros_avanzados()
            
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

def menu_filtrar_por_costo():
    """Menú interactivo para filtrar por costo de entrada"""
    print("\n===== FILTRAR POR COSTO DE ENTRADA =====")
    print("Elija el tipo de comparación:")
    print("1. Mayor que")
    print("2. Menor que")
    print("3. Entre dos valores")
    print("0. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "0":
        return
    
    if opcion == "1":
        try:
            valor = int(input("\nFiltrar eventos con costo MAYOR que: "))
            # Crear script DSL directamente
            script_dsl = f'load "eventos.csv";\nfilter column "costo_entrada" > {valor};\nprint;'
            
            # Escribir a archivo temporal
            temp_dsl = "temp_consulta.dsl"
            with open(temp_dsl, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Ejecutar consulta
            print(f"\nEventos con costo mayor a {valor}:")
            print("="*80)
            procesar_script_desde_dsl(temp_dsl)
            
            # Limpiar
            if os.path.exists(temp_dsl):
                os.remove(temp_dsl)
                
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    elif opcion == "2":
        try:
            valor = int(input("\nFiltrar eventos con costo MENOR que: "))
            # Crear script DSL directamente
            script_dsl = f'load "eventos.csv";\nfilter column "costo_entrada" < {valor};\nprint;'
            
            # Escribir a archivo temporal
            temp_dsl = "temp_consulta.dsl"
            with open(temp_dsl, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Ejecutar consulta
            print(f"\nEventos con costo menor a {valor}:")
            print("="*80)
            procesar_script_desde_dsl(temp_dsl)
            
            # Limpiar
            if os.path.exists(temp_dsl):
                os.remove(temp_dsl)
                
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    elif opcion == "3":
        try:
            valor1 = int(input("\nValor mínimo: "))
            valor2 = int(input("Valor máximo: "))
            
            # Crear script DSL directamente
            script_dsl = f'load "eventos.csv";\nfilter column "costo_entrada" between {valor1} and {valor2};\nprint;'
            
            # Escribir a archivo temporal
            temp_dsl = "temp_consulta.dsl"
            with open(temp_dsl, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Ejecutar consulta
            print(f"\nEventos con costo entre {valor1} y {valor2}:")
            print("="*80)
            procesar_script_desde_dsl(temp_dsl)
            
            # Limpiar
            if os.path.exists(temp_dsl):
                os.remove(temp_dsl)
                
        except ValueError:
            print("Error: Debe ingresar números válidos")
    
    else:
        print("Opción no válida.")

def menu_filtrar_por_tipo():
    """Menú interactivo para filtrar por tipo de evento"""
    print("\n===== FILTRAR POR TIPO DE EVENTO =====")
    print("Tipos de eventos disponibles:")
    print("1. Concierto")
    print("2. Festival")
    print("3. Exposición")
    print("4. Conferencia")
    print("5. Seminario")
    print("6. Taller")
    print("0. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "0":
        return
    
    tipos = {
        "1": "Concierto",
        "2": "Festival",
        "3": "Exposición",
        "4": "Conferencia", 
        "5": "Seminario",
        "6": "Taller"
    }
    
    if opcion in tipos:
        tipo_evento = tipos[opcion]
        
        # Crear script DSL directamente - asegurarnos de usar comillas dobles y sin espacio extra
        script_dsl = f'load "eventos.csv";\nfilter column "tipo_evento" == "{tipo_evento}";\nprint;'
        
        # Para depuración, mostrar la consulta
        print(f"\nConsulta DSL: {script_dsl}")
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print(f"\nEventos de tipo {tipo_evento}:")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    else:
        print("Opción no válida.")

def menu_filtrar_por_lugar():
    """Menú interactivo para filtrar por lugar del evento"""
    print("\n===== FILTRAR POR LUGAR =====")
    print("1. Madrid")
    print("2. Barcelona")
    print("3. Valencia")
    print("4. Otro lugar (ingreso manual)")
    print("0. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "0":
        return
    
    lugares = {
        "1": "Madrid",
        "2": "Barcelona",
        "3": "Valencia"
    }
    
    lugar = ""
    if opcion in lugares:
        lugar = lugares[opcion]
    elif opcion == "4":
        lugar = input("Ingrese el nombre del lugar: ")
    else:
        print("Opción no válida.")
        return
    
    # Crear script DSL directamente
    script_dsl = f'load "eventos.csv";\nfilter column "lugar" == "{lugar}";\nprint;'
    
    # Escribir a archivo temporal
    temp_dsl = "temp_consulta.dsl"
    with open(temp_dsl, 'w', encoding='utf-8') as f:
        f.write(script_dsl)
    
    # Ejecutar consulta
    print(f"\nEventos en {lugar}:")
    print("="*80)
    procesar_script_desde_dsl(temp_dsl)
    
    # Limpiar
    if os.path.exists(temp_dsl):
        os.remove(temp_dsl)

def menu_estadisticas():
    """Menú interactivo para estadísticas sobre eventos"""
    print("\n===== ESTADÍSTICAS DE EVENTOS =====")
    print("1. Promedio de costo de entrada")
    print("2. Promedio de asistentes por evento")
    print("3. Total de asistentes a todos los eventos")
    print("4. Evento con mayor costo de entrada")
    print("5. Evento con menor costo de entrada") 
    print("6. Estadísticas por tipo de evento")
    print("7. Eventos más populares (top 5)")
    print("0. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "0":
        return
    
    if opcion == "1":
        # Crear script DSL directamente
        script_dsl = 'load "eventos.csv";\naggregate average column "costo_entrada";\nprint;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print("\nPromedio de costo de entrada:")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    
    elif opcion == "2":
        # Crear script DSL directamente
        script_dsl = 'load "eventos.csv";\naggregate average column "cantidad_asistentes";\nprint;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print("\nPromedio de asistentes por evento:")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    
    elif opcion == "3":
        # Crear script DSL directamente
        script_dsl = 'load "eventos.csv";\naggregate sum column "cantidad_asistentes";\nprint;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print("\nTotal de asistentes a todos los eventos:")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    
    elif opcion == "4":
        # Crear script DSL directamente
        script_dsl = 'load "eventos.csv";\nsort by "costo_entrada" desc;\nlimit 1;\nprint;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print("\nEvento con mayor costo de entrada:")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    
    elif opcion == "5":
        # Crear script DSL directamente
        script_dsl = 'load "eventos.csv";\nsort by "costo_entrada" asc;\nlimit 1;\nprint;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print("\nEvento con menor costo de entrada:")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    
    elif opcion == "6":
        # Estadísticas por tipo de evento
        # Vamos a realizar análisis agrupado por tipo
        
        try:
            # Cargar todos los datos
            with open("eventos.csv", newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                data = list(reader)
            
            # Inicializar estadísticas por tipo
            stats_por_tipo = {}
            
            for row in data:
                tipo = row["tipo_evento"]
                if tipo not in stats_por_tipo:
                    stats_por_tipo[tipo] = {
                        "count": 0,
                        "costo_total": 0,
                        "asistentes_total": 0
                    }
                
                # Agregar datos
                stats_por_tipo[tipo]["count"] += 1
                stats_por_tipo[tipo]["costo_total"] += float(row["costo_entrada"])
                stats_por_tipo[tipo]["asistentes_total"] += int(row["cantidad_asistentes"])
            
            # Calcular promedios y mostrar resultados
            print("\n===== ESTADÍSTICAS POR TIPO DE EVENTO =====")
            print(f"{'Tipo de Evento':<15} | {'Cantidad':<10} | {'Costo Promedio':<15} | {'Asistentes Promedio':<20}")
            print("-" * 70)
            
            for tipo, stats in sorted(stats_por_tipo.items()):
                count = stats["count"]
                costo_promedio = stats["costo_total"] / count if count > 0 else 0
                asistentes_promedio = stats["asistentes_total"] / count if count > 0 else 0
                
                print(f"{tipo:<15} | {count:<10} | {costo_promedio:,.2f} | {asistentes_promedio:,.2f}")
            
            print("-" * 70)
            print(f"Total de eventos: {len(data)}")
                
        except Exception as e:
            print(f"Error al calcular estadísticas por tipo: {str(e)}")
    
    elif opcion == "7":
        # Eventos más populares (top 5)
        script_dsl = 'load "eventos.csv";\nsort by "cantidad_asistentes" desc;\nlimit 5;\nprint;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print("\nEventos más populares (Top 5 por asistencia):")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    
    else:
        print("Opción no válida.")

def menu_filtros_avanzados():
    """Menú interactivo para filtros avanzados y combinados"""
    print("\n===== FILTROS AVANZADOS COMBINADOS =====")
    print("1. Filtrar por tipo y rango de costo")
    print("2. Filtrar por lugar y asistentes")
    print("3. Filtrar por tipo y estado del evento")
    print("4. Eventos de alto costo (top 10%)")
    print("5. Eventos populares en un lugar específico")
    print("0. Volver al menú principal")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "0":
        return
    
    if opcion == "1":
        # Filtrar por tipo y rango de costo
        tipos = {
            "1": "Concierto",
            "2": "Festival",
            "3": "Exposición",
            "4": "Conferencia", 
            "5": "Seminario",
            "6": "Taller"
        }
        
        print("\nSeleccione el tipo de evento:")
        for key, value in tipos.items():
            print(f"{key}. {value}")
        tipo_opcion = input("Opción: ")
        
        if tipo_opcion not in tipos:
            print("Tipo de evento no válido.")
            return
            
        tipo_evento = tipos[tipo_opcion]
        
        try:
            min_costo = int(input("\nCosto mínimo: "))
            max_costo = int(input("Costo máximo: "))
            
            if min_costo > max_costo:
                min_costo, max_costo = max_costo, min_costo  # Intercambiar si están al revés
                
            # Crear script DSL con filtros combinados
            script_dsl = f'load "eventos.csv";\n'
            script_dsl += f'filter column "tipo_evento" == "{tipo_evento}";\n'
            script_dsl += f'filter column "costo_entrada" between {min_costo} and {max_costo};\n'
            script_dsl += 'print;'
            
            # Escribir a archivo temporal
            temp_dsl = "temp_consulta.dsl"
            with open(temp_dsl, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Ejecutar consulta
            print(f"\nEventos de tipo {tipo_evento} con costo entre {min_costo} y {max_costo}:")
            print("="*80)
            procesar_script_desde_dsl(temp_dsl)
            
            # Limpiar
            if os.path.exists(temp_dsl):
                os.remove(temp_dsl)
                
        except ValueError:
            print("Error: Debe ingresar valores numéricos válidos.")
            
    elif opcion == "2":
        # Filtrar por lugar y asistentes
        lugar = input("\nIngrese el nombre del lugar (ciudad): ")
        
        try:
            min_asistentes = int(input("\nMínimo de asistentes: "))
            
            # Crear script DSL con filtros combinados
            script_dsl = f'load "eventos.csv";\n'
            script_dsl += f'filter column "lugar" == "{lugar}";\n'
            script_dsl += f'filter column "cantidad_asistentes" >= {min_asistentes};\n'
            script_dsl += 'sort by "cantidad_asistentes" desc;\n'
            script_dsl += 'print;'
            
            # Escribir a archivo temporal
            temp_dsl = "temp_consulta.dsl"
            with open(temp_dsl, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Ejecutar consulta
            print(f"\nEventos en {lugar} con al menos {min_asistentes} asistentes (ordenados por popularidad):")
            print("="*80)
            procesar_script_desde_dsl(temp_dsl)
            
            # Limpiar
            if os.path.exists(temp_dsl):
                os.remove(temp_dsl)
                
        except ValueError:
            print("Error: Debe ingresar un número válido de asistentes.")
            
    elif opcion == "3":
        # Filtrar por tipo y estado del evento
        tipos = {
            "1": "Concierto",
            "2": "Festival",
            "3": "Exposición",
            "4": "Conferencia", 
            "5": "Seminario",
            "6": "Taller"
        }
        
        estados = {
            "1": "Programado",
            "2": "Realizado",
            "3": "Cancelado"
        }
        
        print("\nSeleccione el tipo de evento:")
        for key, value in tipos.items():
            print(f"{key}. {value}")
        tipo_opcion = input("Opción: ")
        
        if tipo_opcion not in tipos:
            print("Tipo de evento no válido.")
            return
            
        tipo_evento = tipos[tipo_opcion]
        
        print("\nSeleccione el estado del evento:")
        for key, value in estados.items():
            print(f"{key}. {value}")
        estado_opcion = input("Opción: ")
        
        if estado_opcion not in estados:
            print("Estado no válido.")
            return
            
        estado_evento = estados[estado_opcion]
        
        # Crear script DSL con filtros combinados
        script_dsl = f'load "eventos.csv";\n'
        script_dsl += f'filter column "tipo_evento" == "{tipo_evento}";\n'
        script_dsl += f'filter column "estado_evento" == "{estado_evento}";\n'
        script_dsl += 'sort by "fecha" asc;\n'
        script_dsl += 'print;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print(f"\nEventos de tipo {tipo_evento} con estado {estado_evento} (ordenados por fecha):")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
    
    elif opcion == "4":
        # Eventos de alto costo (top 10%)
        try:
            # Primero vamos a obtener el umbral para el top 10% usando una consulta de agregación
            # Calculamos el percentil 90 usando una aproximación
            
            # Paso 1: Cargar todos los datos
            script_dsl = f'load "eventos.csv";\n'
            script_dsl += 'sort by "costo_entrada" desc;\n'
            script_dsl += 'print;'
            
            # Escribir a archivo temporal
            temp_dsl = "temp_carga.dsl"
            with open(temp_dsl, 'w', encoding='utf-8') as f:
                f.write(script_dsl)
            
            # Ejecutar la consulta para obtener todos los datos ordenados
            visitor = MyCSVVisitor()
            input_stream = FileStream(temp_dsl, encoding='utf-8')
            lexer = CSVFilterLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = CSVFilterParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(CustomErrorListener())
            tree = parser.prog()
            visitor.visit(tree)
            
            # Calcular el umbral del percentil 90
            all_data = visitor.filtered_data
            if all_data and len(all_data) > 0:
                # Tomar aproximadamente el 10% superior de los datos
                top_10_percent_index = max(0, int(len(all_data) * 0.1))
                if top_10_percent_index < len(all_data):
                    umbral_costo = float(all_data[top_10_percent_index]["costo_entrada"])
                    
                    # Ahora crear una consulta para mostrar eventos por encima del umbral
                    script_dsl = f'load "eventos.csv";\n'
                    script_dsl += f'filter column "costo_entrada" >= {umbral_costo};\n'
                    script_dsl += 'sort by "costo_entrada" desc;\n'
                    script_dsl += 'print;'
                    
                    # Escribir a archivo temporal
                    temp_dsl = "temp_consulta.dsl"
                    with open(temp_dsl, 'w', encoding='utf-8') as f:
                        f.write(script_dsl)
                    
                    # Ejecutar consulta
                    print(f"\nEventos de alto costo (top 10%, mayor o igual a {umbral_costo:,.2f}):")
                    print("="*80)
                    procesar_script_desde_dsl(temp_dsl)
                    
                    # Limpiar
                    if os.path.exists(temp_dsl):
                        os.remove(temp_dsl)
                else:
                    print("No hay suficientes datos para calcular el top 10%.")
            else:
                print("No se pudieron cargar los datos para analizar los costos.")
                
            # Limpiar
            if os.path.exists(temp_dsl):
                os.remove(temp_dsl)
                
        except Exception as e:
            print(f"Error al procesar la consulta de alto costo: {str(e)}")
            
    elif opcion == "5":
        # Eventos populares en un lugar específico
        lugar = input("\nIngrese el nombre del lugar (ciudad): ")
        
        # Crear script DSL para encontrar eventos populares en ese lugar
        script_dsl = f'load "eventos.csv";\n'
        script_dsl += f'filter column "lugar" == "{lugar}";\n'
        script_dsl += 'sort by "cantidad_asistentes" desc;\n'
        script_dsl += 'print;'
        
        # Escribir a archivo temporal
        temp_dsl = "temp_consulta.dsl"
        with open(temp_dsl, 'w', encoding='utf-8') as f:
            f.write(script_dsl)
        
        # Ejecutar consulta
        print(f"\nEventos más populares en {lugar} (ordenados por número de asistentes):")
        print("="*80)
        procesar_script_desde_dsl(temp_dsl)
        
        # Limpiar
        if os.path.exists(temp_dsl):
            os.remove(temp_dsl)
            
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()