import csv
import json
import re
from CSVFilterVisitor import CSVFilterVisitor

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self, mostrar_carga=True):
        self.data = []
        self.filtered_data = []
        self.filename = ""
        self.operations = []
        self.aggregations = {}
        self.results = []
        self.joined_data = None
        self.current_operation = {}
        self.mostrar_carga = mostrar_carga
        self.loaded_file = None
        self.error = None
        
    def visitProg(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)
        return None
        
    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        self.loaded_file = self.filename
        self.operations.append({
            "type": "load",
            "filename": self.filename
        })
        
        try:
            with open(self.filename, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.filtered_data = list(reader)
            
            return self.filtered_data
        except Exception as e:
            self.error = f"Error al cargar el archivo CSV: {e}"
            return None

    def visitFilterStat(self, ctx):
        column = ctx.STRING(0).getText().replace('"', '')
        
        # Manejar diferentes tipos de filtros
        if ctx.K_BETWEEN():
            # Filtro BETWEEN
            filter_type = "between"
            value1 = self._extract_value(ctx.value(0))
            value2 = self._extract_value(ctx.value(1))
            
            self.operations.append({
                "type": "filter",
                "filter_type": "between",
                "column": column,
                "value1": value1,
                "value2": value2
            })
        elif ctx.K_IN():
            # Filtro IN (lista de valores)
            filter_type = "in"
            values = []
            for value_ctx in ctx.value():
                values.append(self._extract_value(value_ctx))
            
            self.operations.append({
                "type": "filter",
                "filter_type": "in",
                "column": column,
                "values": values
            })
        elif ctx.K_LIKE():
            # Filtro LIKE (patrón)
            filter_type = "like"
            pattern = ctx.STRING(1).getText().replace('"', '')
            
            self.operations.append({
                "type": "filter",
                "filter_type": "like",
                "column": column,
                "pattern": pattern
            })
        else:
            # Filtro estándar (operador)
            operator = ctx.OPERATOR().getText()
            value = self._extract_value(ctx.value(0))
            
            self.operations.append({
                "type": "filter",
                "column": column,
                "operator": operator,
                "value": value
            })
            
        return None

    def visitAggregateStat(self, ctx):
        function = ctx.AGGR_FUNC().getText()
        column = ctx.STRING(0).getText().replace('"', '')
        
        # Comprobar si hay condición WHERE
        if ctx.K_WHERE():
            condition_column = ctx.STRING(1).getText().replace('"', '')
            condition_operator = ctx.OPERATOR().getText()
            condition_value = self._extract_value(ctx.value())
            
            self.operations.append({
                "type": "aggregate",
                "aggregate_type": function,
                "column": column,
                "filter_condition": {
                    "column": condition_column,
                    "operator": condition_operator,
                    "value": condition_value
                }
            })
        else:
            self.operations.append({
                "type": "aggregate",
                "aggregate_type": function,
                "column": column
            })
            
        return None

    def visitSortStat(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        order = ctx.sortOrder().getText()  # asc o desc
        
        self.operations.append({
            "type": "sort",
            "column": column,
            "order": order
        })
        return None
        
    def visitLimitStat(self, ctx):
        limit = int(ctx.INT().getText())
        
        self.operations.append({
            "type": "limit",
            "limit": limit
        })
        return None
        
    def visitJoinStat(self, ctx):
        second_file = ctx.STRING(0).getText().replace('"', '')
        first_key = ctx.STRING(1).getText().replace('"', '')
        second_key = ctx.STRING(2).getText().replace('"', '')
        
        self.operations.append({
            "type": "join",
            "second_file": second_file,
            "first_key": first_key,
            "second_key": second_key
        })
        return None
        
    def visitGroupStat(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        
        self.operations.append({
            "type": "group",
            "column": column
        })
        return None

    def visitPrintStat(self, ctx):
        # Ejecutar las operaciones acumuladas
        self._execute_operations()
        
        # Guardar resultados
        if self.aggregations:
            for agg_name, agg_value in self.aggregations.items():
                self.results.append({agg_name: agg_value})
        else:
            self.results = self.filtered_data.copy()
        
        # Registrar la operación pero sin imprimir nada
        self.operations.append({
            "type": "print"
        })
        
        return self.filtered_data
    
    def _execute_operations(self):
        # Ejecutar operaciones acumuladas
        self.data = []
        self.filtered_data = []
        self.aggregations = {}
        self.results = []  # Limpiar resultados anteriores
        self.current_operation = {}
        
        for operation in self.operations:
            self.current_operation = operation
            if operation["type"] == "load":
                self._load_data(operation["filename"])
            elif operation["type"] == "filter":
                self._apply_filter(operation)
            elif operation["type"] == "aggregate":
                self._apply_aggregation(operation)
            elif operation["type"] == "sort":
                self._apply_sort(operation)
            elif operation["type"] == "limit":
                self._apply_limit(operation)
            elif operation["type"] == "join":
                self._apply_join(operation)
            elif operation["type"] == "group":
                self._apply_group(operation)
    
    def _load_data(self, filename):
        try:
            with open(filename, newline='', encoding='utf-8') as f:
                self.data = list(csv.DictReader(f))
            self.filtered_data = self.data.copy()
        except Exception as e:
            print(f"Error al cargar el archivo '{filename}': {e}")
            self.data = []
            self.filtered_data = []
    
    def _apply_filter(self, filter_operation):
        if "filter_type" not in filter_operation:
            # Filtro estándar con operador
            column = filter_operation["column"]
            operator = filter_operation["operator"]
            value = filter_operation["value"]
            
            filtered_results = []
            for row in self.filtered_data:
                if column not in row:
                    continue
                    
                row_value = row[column]
                
                # Si estamos comparando cadenas, normalizar
                if isinstance(value, str) and not value.replace('.', '', 1).isdigit():
                    # Comparación de texto insensible a mayúsculas/minúsculas
                    if operator == "==":
                        if row_value.strip().lower() == value.strip().lower():
                            filtered_results.append(row)
                        continue
                    elif operator == "!=":
                        if row_value.strip().lower() != value.strip().lower():
                            filtered_results.append(row)
                        continue
                
                # Convertir a número o booleano si es necesario
                if isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.', '', 1).isdigit()):
                    try:
                        row_value = float(row_value)
                        if isinstance(value, str):
                            value = float(value)
                    except ValueError:
                        continue  # Si no se puede convertir a número, ignorar el registro
                elif isinstance(value, bool) or value in ('true', 'false'):
                    row_value = str(row_value).lower() == 'true'
                    if isinstance(value, str):
                        value = value.lower() == 'true'
                
                # Evaluar la condición del filtro
                if self._evaluate_condition(row_value, operator, value):
                    filtered_results.append(row)
                    
            self.filtered_data = filtered_results
        
        elif filter_operation["filter_type"] == "between":
            # Filtro BETWEEN
            column = filter_operation["column"]
            value1 = filter_operation["value1"]
            value2 = filter_operation["value2"]
            
            filtered_results = []
            for row in self.filtered_data:
                if column not in row:
                    continue
                    
                try:
                    row_value = float(row[column])
                    if value1 <= row_value <= value2:
                        filtered_results.append(row)
                except ValueError:
                    pass  # Ignorar valores no numéricos
                    
            self.filtered_data = filtered_results
            
        elif filter_operation["filter_type"] == "in":
            # Filtro IN
            column = filter_operation["column"]
            values = filter_operation["values"]
            
            filtered_results = []
            for row in self.filtered_data:
                if column not in row:
                    continue
                    
                row_value = row[column]
                
                # Para comparaciones de texto, normalizar
                if all(isinstance(v, str) for v in values):
                    # Normalizar valores para comparación de texto
                    row_value = row_value.strip().lower()
                    normalized_values = [v.strip().lower() for v in values]
                    if row_value in normalized_values:
                        filtered_results.append(row)
                    continue
                
                # Convertir a número si los valores son numéricos
                if all(isinstance(v, (int, float)) for v in values):
                    try:
                        row_value = float(row_value)
                    except ValueError:
                        continue
                
                if row_value in values:
                    filtered_results.append(row)
                    
            self.filtered_data = filtered_results
            
        elif filter_operation["filter_type"] == "like":
            # Filtro LIKE
            column = filter_operation["column"]
            pattern = filter_operation["pattern"]
            
            # Convertir patrón LIKE a expresión regular
            regex_pattern = self._like_to_regex(pattern)
            
            filtered_results = []
            for row in self.filtered_data:
                if column not in row:
                    continue
                    
                row_value = str(row[column])
                if re.search(regex_pattern, row_value, re.IGNORECASE):
                    filtered_results.append(row)
                    
            self.filtered_data = filtered_results
    
    def _like_to_regex(self, pattern):
        """Convierte un patrón LIKE a una expresión regular"""
        # Escapar caracteres especiales de regex
        pattern = re.escape(pattern)
        # Reemplazar los comodines de LIKE por equivalentes regex
        pattern = pattern.replace('\\%', '.*').replace('\\_', '.')
        return f"^{pattern}$"
    
    def _evaluate_condition(self, value1, operator, value2):
        if operator == '>':
            return value1 > value2
        elif operator == '<':
            return value1 < value2
        elif operator == '>=':
            return value1 >= value2
        elif operator == '<=':
            return value1 <= value2
        elif operator == '==':
            return value1 == value2
        elif operator == '!=':
            return value1 != value2
        elif operator.lower() == 'contains':
            return str(value2) in str(value1)
        return False
    
    def _apply_aggregation(self, agg_operation):
        agg_type = agg_operation["aggregate_type"]
        column = agg_operation["column"]
        
        # Si hay una condición de filtro, aplicarla primero
        data_to_use = self.filtered_data
        if "filter_condition" in agg_operation:
            filtered_data = []
            for row in self.filtered_data:
                if self._evaluate_filter_condition(row, agg_operation["filter_condition"]):
                    filtered_data.append(row)
            data_to_use = filtered_data
        
        # Realizar la agregación correspondiente
        if agg_type == "count":
            result = len(data_to_use)
            self.aggregations[f"count_{column}"] = result
        else:
            # Convertir valores a numéricos para operaciones numéricas
            numeric_values = []
            for row in data_to_use:
                try:
                    numeric_values.append(float(row[column]))
                except (ValueError, TypeError):
                    pass  # Ignorar valores no numéricos
            
            if not numeric_values:
                self.aggregations[f"{agg_type}_{column}"] = 0
                return
                
            if agg_type == "sum":
                result = sum(numeric_values)
                self.aggregations[f"sum_{column}"] = result
            elif agg_type == "average":
                result = sum(numeric_values) / len(numeric_values)
                self.aggregations[f"average_{column}"] = result
            elif agg_type == "min":
                result = min(numeric_values)
                self.aggregations[f"min_{column}"] = result
            elif agg_type == "max":
                result = max(numeric_values)
                self.aggregations[f"max_{column}"] = result
    
    def _evaluate_filter_condition(self, row, filter_condition):
        column = filter_condition["column"]
        operator = filter_condition["operator"]
        value = filter_condition["value"]
        
        row_value = row[column]
        
        # Convertir a número si es posible
        if isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.', '', 1).isdigit()):
            try:
                row_value = float(row_value)
                if isinstance(value, str):
                    value = float(value)
            except ValueError:
                pass
        
        # Evaluar la condición
        return self._evaluate_condition(row_value, operator, value)
        
    def _apply_sort(self, sort_operation):
        column = sort_operation["column"]
        order = sort_operation["order"]
        
        # Ordenar los datos
        try:
            # Intentar ordenar numéricamente si es posible
            self.filtered_data = sorted(
                self.filtered_data, 
                key=lambda x: self._safe_numeric_value(x[column]), 
                reverse=(order == 'desc')
            )
        except:
            # Si falla, ordenar como texto
            self.filtered_data = sorted(
                self.filtered_data, 
                key=lambda x: str(x[column]).lower(), 
                reverse=(order == 'desc')
            )
    
    def _safe_numeric_value(self, value):
        """Intenta convertir un valor a numérico de forma segura"""
        try:
            return float(value)
        except (ValueError, TypeError):
            return str(value).lower()
            
    def _apply_limit(self, limit_operation):
        limit = limit_operation["limit"]
        self.filtered_data = self.filtered_data[:limit]
    
    def _apply_join(self, join_operation):
        second_file = join_operation["second_file"]
        first_key = join_operation["first_key"]
        second_key = join_operation["second_key"]
        
        try:
            # Cargar el segundo archivo
            with open(second_file, newline='', encoding='utf-8') as f:
                second_data = list(csv.DictReader(f))
            
            # Crear un índice para el segundo archivo
            second_index = {}
            for row in second_data:
                key = row[second_key]
                if key not in second_index:
                    second_index[key] = []
                second_index[key].append(row)
            
            # Realizar el join
            joined_data = []
            for row in self.filtered_data:
                first_value = row[first_key]
                if first_value in second_index:
                    # Para cada fila coincidente en el segundo archivo
                    for second_row in second_index[first_value]:
                        # Combinar las filas
                        joined_row = row.copy()
                        for k, v in second_row.items():
                            # Evitar sobrescribir columnas con el mismo nombre
                            if k in joined_row and k != second_key:
                                joined_row[f"{second_file}_{k}"] = v
                            else:
                                joined_row[k] = v
                        joined_data.append(joined_row)
            
            self.filtered_data = joined_data
                
        except Exception as e:
            print(f"Error al realizar join con archivo '{second_file}': {e}")
    
    def _apply_group(self, group_operation):
        column = group_operation["column"]
        
        # Agrupar los datos
        grouped_data = {}
        for row in self.filtered_data:
            key = row[column]
            if key not in grouped_data:
                grouped_data[key] = []
            grouped_data[key].append(row)
        
        # Convertir los grupos a un formato de resultados
        result_data = []
        for key, group in grouped_data.items():
            # Contar elementos en el grupo
            count = len(group)
            
            # Calcular algunas estadísticas básicas para columnas numéricas
            stats = {"grupo": key, "count": count}
            
            # Añadir la primera fila como ejemplo
            example_row = group[0]
            for k, v in example_row.items():
                if k != column:
                    stats[f"ejemplo_{k}"] = v
            
            result_data.append(stats)
        
        self.filtered_data = result_data
    
    def _extract_value(self, value_ctx):
        """Extrae el valor de un contexto de valor"""
        if value_ctx.INT():
            return int(value_ctx.INT().getText())
        elif value_ctx.FLOAT():
            return float(value_ctx.FLOAT().getText())
        elif value_ctx.BOOLEAN():
            return value_ctx.BOOLEAN().getText() == 'true'
        else:  # STRING
            return value_ctx.STRING().getText().replace('"', '')
            
    def get_results(self):
        """Devuelve los resultados de la última operación"""
        return self.results