import json
import csv
import re
import math
import datetime
from datetime import datetime as dt

class JSONProcessor:
    def __init__(self, json_file):
        """Inicializa el procesador con un archivo JSON"""
        self.json_file = json_file
        self.data = []
        self.filtered_data = []
        self.aggregation_results = {}

    def load_json_config(self):
        """Carga la configuración desde el archivo JSON"""
        with open(self.json_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_data(self, file_path):
        """Carga los datos desde un archivo CSV"""
        with open(file_path, newline='', encoding='utf-8') as f:
            self.data = list(csv.DictReader(f))
        self.filtered_data = self.data  # Inicialmente, sin filtrar

    def apply_filters(self, filters):
        """Aplica múltiples filtros a los datos"""
        if not filters:
            return
        
        self.filtered_data = self.data.copy()
        
        for filter_config in filters:
            # Si es un filtro simple (compatible con versión anterior)
            if "column" in filter_config:
                column = filter_config["column"]
                operator = filter_config["operator"]
                value = filter_config["value"]
                
                self.filtered_data = [
                    row for row in self.filtered_data 
                    if self.evaluate_condition(row, column, operator, value)
                ]
            
            # Si es un filtro compuesto (AND/OR)
            elif "type" in filter_config and "conditions" in filter_config:
                filter_type = filter_config["type"]
                conditions = filter_config["conditions"]
                
                if filter_type == "AND":
                    self.filtered_data = [
                        row for row in self.filtered_data 
                        if self.evaluate_and_conditions(row, conditions)
                    ]
                elif filter_type == "OR":
                    self.filtered_data = [
                        row for row in self.filtered_data 
                        if self.evaluate_or_conditions(row, conditions)
                    ]
                else:
                    print(f"Tipo de filtro desconocido: {filter_type}")

    def evaluate_and_conditions(self, row, conditions):
        """Evalúa múltiples condiciones con operador lógico AND"""
        for condition in conditions:
            # Si es un filtro simple
            if "column" in condition:
                column = condition["column"]
                operator = condition["operator"]
                value = condition["value"]
                
                if not self.evaluate_condition(row, column, operator, value):
                    return False
            # Si es un filtro anidado
            elif "type" in condition and "conditions" in condition:
                filter_type = condition["type"]
                nested_conditions = condition["conditions"]
                
                if filter_type == "AND":
                    if not self.evaluate_and_conditions(row, nested_conditions):
                        return False
                elif filter_type == "OR":
                    if not self.evaluate_or_conditions(row, nested_conditions):
                        return False
                else:
                    print(f"Tipo de filtro anidado desconocido: {filter_type}")
                    return False
            else:
                print(f"Estructura de condición inválida: {condition}")
                return False
            
        return True

    def evaluate_or_conditions(self, row, conditions):
        """Evalúa múltiples condiciones con operador lógico OR"""
        if not conditions:
            return True
        
        for condition in conditions:
            # Si es un filtro simple
            if "column" in condition:
                column = condition["column"]
                operator = condition["operator"]
                value = condition["value"]
                
                if self.evaluate_condition(row, column, operator, value):
                    return True
            # Si es un filtro anidado
            elif "type" in condition and "conditions" in condition:
                filter_type = condition["type"]
                nested_conditions = condition["conditions"]
                
                if filter_type == "AND":
                    if self.evaluate_and_conditions(row, nested_conditions):
                        return True
                elif filter_type == "OR":
                    if self.evaluate_or_conditions(row, nested_conditions):
                        return True
                else:
                    print(f"Tipo de filtro anidado desconocido: {filter_type}")
            else:
                print(f"Estructura de condición inválida: {condition}")
            
        return False

    def evaluate_condition(self, row, column, operator, value):
        """Evalúa una condición para una fila utilizando uno de los 40 operadores disponibles"""
        try:
            # Si la columna empieza con "calc:", realizamos un cálculo en vez de acceder a la columna
            if column.startswith("calc:"):
                expression = column[5:]  # Quitar el prefijo "calc:"
                row_value = self._evaluate_expression(expression, row)
            else:
                row_value = row.get(column, None)
            
            # 1. Operadores de comparación básicos
            if operator == "equal" or operator == "==":
                return row_value == value
            elif operator == "not_equal" or operator == "!=":
                return row_value != value
            elif operator == "greater" or operator == ">":
                return self._to_number(row_value) > self._to_number(value)
            elif operator == "less" or operator == "<":
                return self._to_number(row_value) < self._to_number(value)
            elif operator == "greater_equal" or operator == ">=":
                return self._to_number(row_value) >= self._to_number(value)
            elif operator == "less_equal" or operator == "<=":
                return self._to_number(row_value) <= self._to_number(value)
            
            # 2. Operadores matemáticos
            elif operator == "mod":
                return self._to_number(row_value) % self._to_number(value) == 0
            elif operator == "mod_equal":
                modval, target = value if isinstance(value, list) else (value, 0)
                return self._to_number(row_value) % self._to_number(modval) == target
            elif operator == "abs_less":
                return abs(self._to_number(row_value)) < self._to_number(value)
            elif operator == "abs_greater":
                return abs(self._to_number(row_value)) > self._to_number(value)
            elif operator == "even":
                return self._to_number(row_value) % 2 == 0
            elif operator == "odd":
                return self._to_number(row_value) % 2 != 0
            
            # 3. Operadores de texto
            elif operator == "contains":
                return str(value) in str(row_value)
            elif operator == "not_contains":
                return str(value) not in str(row_value)
            elif operator == "starts_with":
                return str(row_value).startswith(str(value))
            elif operator == "ends_with":
                return str(row_value).endswith(str(value))
            elif operator == "matches":
                return bool(re.match(str(value), str(row_value)))
            elif operator == "length_equal":
                return len(str(row_value)) == int(value)
            elif operator == "length_greater":
                return len(str(row_value)) > int(value)
            elif operator == "length_less":
                return len(str(row_value)) < int(value)
            elif operator == "is_upper":
                return str(row_value).isupper()
            elif operator == "is_lower":
                return str(row_value).islower()
            elif operator == "is_alphabetic":
                return str(row_value).isalpha()
            elif operator == "is_numeric":
                return str(row_value).isdigit()
            
            # 4. Operadores de verificación de existencia
            elif operator == "is_null":
                return row_value is None or row_value == ""
            elif operator == "is_not_null":
                return row_value is not None and row_value != ""
            elif operator == "has_key":
                return value in row
            elif operator == "not_has_key":
                return value not in row
            
            # 5. Operadores de lista
            elif operator == "in":
                return row_value in value if isinstance(value, list) else False
            elif operator == "not_in":
                return row_value not in value if isinstance(value, list) else True
            elif operator == "any_in":
                return any(v in str(row_value) for v in value) if isinstance(value, list) else False
            elif operator == "all_in":
                return all(v in str(row_value) for v in value) if isinstance(value, list) else False
            
            # 6. Operadores de fecha/tiempo
            elif operator == "date_before":
                return self._parse_date(row_value) < self._parse_date(value)
            elif operator == "date_after":
                return self._parse_date(row_value) > self._parse_date(value)
            elif operator == "date_between":
                date = self._parse_date(row_value)
                start, end = map(self._parse_date, value) if isinstance(value, list) else (None, None)
                return start <= date <= end if start and end else False
            elif operator == "weekday":
                day = self._parse_date(row_value).weekday()
                return day == value
            elif operator == "weekend":
                day = self._parse_date(row_value).weekday()
                return day >= 5  # 5=sábado, 6=domingo
            
            # 7. Operadores estadísticos
            elif operator == "in_range":
                num = self._to_number(row_value)
                min_val, max_val = value if isinstance(value, list) and len(value) >= 2 else (0, value)
                return min_val <= num <= max_val
            elif operator == "outlier":
                # Define un valor como atípico si está fuera de cierto rango
                num = self._to_number(row_value)
                threshold = self._to_number(value)
                return abs(num) > threshold
            
            # 8. Operadores personalizados
            elif operator == "custom_eval":
                # Permite una expresión personalizada
                local_vars = {"x": self._to_number(row_value)}
                return eval(value, {"__builtins__": {}}, local_vars)
            
            else:
                raise ValueError(f"Operador no soportado: {operator}")
        except Exception as e:
            print(f"Error evaluando condición ({operator}): {e}")
            return False

    def _to_number(self, value):
        """Convierte el valor a número si es posible"""
        if value is None:
            return 0
        if isinstance(value, (int, float)):
            return value
        
        try:
            if '.' in str(value):
                return float(value)
            else:
                return int(value)
        except (ValueError, TypeError):
            return 0
    
    def _parse_date(self, value):
        """Convierte una cadena en fecha"""
        if isinstance(value, datetime.datetime):
            return value
        
        # Lista de formatos de fecha a probar
        formats = [
            "%Y-%m-%d", 
            "%d/%m/%Y", 
            "%m/%d/%Y", 
            "%Y-%m-%d %H:%M:%S",
            "%d-%m-%Y",
            "%Y/%m/%d"
        ]
        
        for fmt in formats:
            try:
                return dt.strptime(value, fmt)
            except (ValueError, TypeError):
                continue
        
        # Si ninguno funciona, retornar la fecha actual
        print(f"No se pudo parsear la fecha: {value}")
        return dt.now()
    
    def _evaluate_expression(self, expression, row):
        """Evalúa una expresión que puede contener referencias a columnas"""
        # Reemplazar referencias a columnas con sus valores
        for col_name in row.keys():
            placeholder = "{" + col_name + "}"
            if placeholder in expression:
                try:
                    expression = expression.replace(placeholder, str(row[col_name]))
                except:
                    expression = expression.replace(placeholder, "0")
        
        # Evaluar la expresión
        try:
            # Crear un entorno de evaluación seguro con funciones básicas
            safe_globals = {
                "__builtins__": {
                    "int": int,
                    "float": float,
                    "str": str,
                    "abs": abs,
                    "round": round,
                    "len": len,
                    "max": max,
                    "min": min,
                    "sum": sum
                },
                "math": math
            }
            
            return eval(expression, safe_globals, {})
        except Exception as e:
            print(f"Error evaluando expresión {expression}: {e}")
            return 0

    def apply_aggregations(self, aggregations):
        """Aplica las operaciones de agregación a los datos filtrados"""
        for agg in aggregations:
            agg_type = agg["type"]
            column = agg["column"]
            
            if agg_type == "count":
                self.aggregation_results[f"count_{column}"] = len(self.filtered_data)
            
            elif agg_type == "sum":
                try:
                    total = sum(float(row[column]) for row in self.filtered_data)
                    self.aggregation_results[f"sum_{column}"] = total
                except (ValueError, KeyError) as e:
                    print(f"Error calculando suma: {e}")
            
            elif agg_type == "average":
                try:
                    if not self.filtered_data:
                        self.aggregation_results[f"avg_{column}"] = 0
                    else:
                        total = sum(float(row[column]) for row in self.filtered_data)
                        self.aggregation_results[f"avg_{column}"] = total / len(self.filtered_data)
                except (ValueError, KeyError) as e:
                    print(f"Error calculando promedio: {e}")
            
            elif agg_type == "max":
                try:
                    if not self.filtered_data:
                        self.aggregation_results[f"max_{column}"] = None
                    else:
                        values = [float(row[column]) for row in self.filtered_data]
                        self.aggregation_results[f"max_{column}"] = max(values)
                except (ValueError, KeyError) as e:
                    print(f"Error calculando máximo: {e}")
            
            elif agg_type == "min":
                try:
                    if not self.filtered_data:
                        self.aggregation_results[f"min_{column}"] = None
                    else:
                        values = [float(row[column]) for row in self.filtered_data]
                        self.aggregation_results[f"min_{column}"] = min(values)
                except (ValueError, KeyError) as e:
                    print(f"Error calculando mínimo: {e}")
            
            elif agg_type == "median":
                try:
                    if not self.filtered_data:
                        self.aggregation_results[f"median_{column}"] = None
                    else:
                        values = sorted([float(row[column]) for row in self.filtered_data])
                        n = len(values)
                        i = n // 2
                        if n % 2 == 0:
                            self.aggregation_results[f"median_{column}"] = (values[i-1] + values[i]) / 2
                        else:
                            self.aggregation_results[f"median_{column}"] = values[i]
                except (ValueError, KeyError) as e:
                    print(f"Error calculando mediana: {e}")
            
            elif agg_type == "std_dev":
                try:
                    if not self.filtered_data or len(self.filtered_data) < 2:
                        self.aggregation_results[f"std_dev_{column}"] = None
                    else:
                        values = [float(row[column]) for row in self.filtered_data]
                        mean = sum(values) / len(values)
                        variances = [(x - mean) ** 2 for x in values]
                        variance = sum(variances) / len(values)
                        self.aggregation_results[f"std_dev_{column}"] = math.sqrt(variance)
                except (ValueError, KeyError) as e:
                    print(f"Error calculando desviación estándar: {e}")
            
            else:
                print(f"Tipo de agregación no soportado: {agg_type}")

    def print_results(self, max_rows=5):
        """Imprime los resultados filtrados y las agregaciones"""
        print(f"\nResultados filtrados ({len(self.filtered_data)} filas):")
        
        # Limitar el número de filas mostradas
        rows_to_show = min(max_rows, len(self.filtered_data))
        for row in self.filtered_data[:rows_to_show]:
            print(row)
        
        if len(self.filtered_data) > rows_to_show:
            print("...")
        
        print("\nResultados de agregaciones:")
        for key, value in self.aggregation_results.items():
            print(f"{key}: {value}")

    def _generate_query_representation(self, config):
        """Genera una representación legible de la consulta basada en la configuración JSON"""
        query_parts = []
        
        # 1. Source
        if "source" in config:
            source_file = config["source"]["file"]
            query_parts.append(f"CARGAR '{source_file}'")
        
        # 2. Filters
        if "filters" in config:
            for filter_config in config["filters"]:
                filter_text = self._filter_to_text(filter_config)
                if filter_text:
                    query_parts.append(f"FILTRAR {filter_text}")
        
        # 3. Aggregations
        if "aggregations" in config:
            for agg in config["aggregations"]:
                agg_type = agg["type"].upper()
                column = agg["column"]
                
                if agg_type == "COUNT":
                    query_parts.append(f"CONTAR '{column}'")
                elif agg_type == "SUM":
                    query_parts.append(f"SUMAR '{column}'")
                elif agg_type == "AVERAGE":
                    query_parts.append(f"PROMEDIO '{column}'")
                elif agg_type == "MAX":
                    query_parts.append(f"MÁXIMO '{column}'")
                elif agg_type == "MIN":
                    query_parts.append(f"MÍNIMO '{column}'")
                elif agg_type == "MEDIAN":
                    query_parts.append(f"MEDIANA '{column}'")
                elif agg_type == "STD_DEV":
                    query_parts.append(f"DESVIACIÓN_ESTÁNDAR '{column}'")
                else:
                    query_parts.append(f"{agg_type} '{column}'")
        
        # 4. Output
        if config.get("output", {}).get("print", False):
            query_parts.append("IMPRIMIR")
        
        return ";\n".join(query_parts) + ";"
    
    def _filter_to_text(self, filter_config, level=0):
        """Convierte un filtro a su representación de texto"""
        indent = "  " * level
        
        # Si es un filtro simple
        if "column" in filter_config and "operator" in filter_config:
            column = filter_config["column"]
            operator = filter_config["operator"]
            value = filter_config["value"]
            
            # Mapeo de operadores a texto
            op_map = {
                "equal": "==", "not_equal": "!=", "greater": ">", "less": "<",
                "greater_equal": ">=", "less_equal": "<=", "contains": "CONTIENE",
                "not_contains": "NO CONTIENE", "starts_with": "EMPIEZA CON",
                "ends_with": "TERMINA CON", "in_range": "EN RANGO", "mod": "MÓDULO",
                "even": "ES PAR", "odd": "ES IMPAR", "is_null": "ES NULO",
                "is_not_null": "NO ES NULO", "matches": "MATCH REGEX"
            }
            
            # Si hay un mapeo para el operador, usarlo, si no, usar el operador tal cual
            op_text = op_map.get(operator, operator)
            
            # Formatear valor según su tipo
            if isinstance(value, list):
                value_text = f"[{', '.join(map(str, value))}]"
            elif isinstance(value, str):
                value_text = f"'{value}'"
            else:
                value_text = str(value)
            
            return f"{indent}{column} {op_text} {value_text}"
        
        # Si es un filtro compuesto (AND/OR)
        elif "type" in filter_config and "conditions" in filter_config:
            filter_type = filter_config["type"]
            conditions = filter_config["conditions"]
            
            cond_texts = []
            for cond in conditions:
                cond_text = self._filter_to_text(cond, level + 1)
                if cond_text:
                    cond_texts.append(cond_text)
            
            if not cond_texts:
                return ""
            
            join_text = f"\n{indent}{filter_type} " if level > 0 else f" {filter_type} "
            result = join_text.join(cond_texts)
            
            if level > 0:
                result = f"{indent}(\n{result}\n{indent})"
            
            return result
        
        return ""

    def process(self):
        """Procesa los datos según la configuración JSON"""
        try:
            # Cargar configuración
            config = self.load_json_config()
            
            # Generar y mostrar la representación de la consulta
            query_representation = self._generate_query_representation(config)
            print("\n=== CONSULTA A EJECUTAR ===")
            print(query_representation)
            print("==========================\n")
            
            # Cargar datos
            csv_file = config["source"]["file"]
            self.load_data(csv_file)
            
            # Aplicar filtros
            self.apply_filters(config.get("filters", []))
            
            # Aplicar agregaciones
            self.apply_aggregations(config.get("aggregations", []))
            
            # Imprimir resultados si se especifica
            if config.get("output", {}).get("print", False):
                max_rows = config.get("output", {}).get("max_rows", 5)
                self.print_results(max_rows)
                
            return self.filtered_data, self.aggregation_results
            
        except Exception as e:
            print(f"Error procesando datos: {e}")
            import traceback
            traceback.print_exc()
            return [], {}

def main():
    import sys
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        json_file = "programa.json"
    
    processor = JSONProcessor(json_file)
    processor.process()

if __name__ == "__main__":
    main() 