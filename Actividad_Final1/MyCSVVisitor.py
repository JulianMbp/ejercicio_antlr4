import csv
import json
import re
from CSVFilterVisitor import CSVFilterVisitor

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self):
        self.data = []
        self.filtered_data = []
        self.filename = ""
        self.operations = []
        self.aggregations = {}
        self.results = []
        self.joined_data = None
        self.current_operation = {}
        
    def visitProg(self, ctx):
        for stat in ctx.stat():
            self.visit(stat)
        return None
        
    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        self.operations.append({
            "type": "load",
            "filename": self.filename
        })
        return None

    def visitFilterStat(self, ctx):
        column = ctx.STRING(0).getText().replace('"', '')
        
        # Filtro estándar con operador
        if ctx.OPERATOR():
            op = ctx.OPERATOR().getText()
            
            # Obtener el valor, que puede ser STRING, INT, FLOAT o BOOLEAN
            value_ctx = ctx.value(0)
            value = self._extract_value(value_ctx)
                
            filter_cond = {
                "type": "filter",
                "column": column,
                "operator": op,
                "value": value
            }
            
            # Si hay un operador lógico, procesar el filtro anidado
            if ctx.LOGICAL_OP():
                logical_op = ctx.LOGICAL_OP().getText()
                nested_filter = self.visit(ctx.filterStat())
                filter_cond["logical_op"] = logical_op
                filter_cond["nested_filter"] = nested_filter
        
        # Filtro BETWEEN
        elif ctx.getChild(2).getText() == 'between':
            value1 = self._extract_value(ctx.value(0))
            value2 = self._extract_value(ctx.value(1))
            
            filter_cond = {
                "type": "filter",
                "filter_type": "between",
                "column": column,
                "value1": value1,
                "value2": value2
            }
            
        # Filtro IN
        elif ctx.getChild(2).getText() == 'in':
            values = []
            value_list = ctx.valueList()
            for i in range(len(value_list.value())):
                values.append(self._extract_value(value_list.value(i)))
                
            filter_cond = {
                "type": "filter",
                "filter_type": "in",
                "column": column,
                "values": values
            }
            
        # Filtro LIKE
        elif ctx.getChild(2).getText() == 'like':
            pattern = ctx.STRING(1).getText().replace('"', '')
            
            filter_cond = {
                "type": "filter",
                "filter_type": "like",
                "column": column,
                "pattern": pattern
            }
            
        self.operations.append(filter_cond)
        return filter_cond

    def visitAggregateStat(self, ctx):
        agg_type = ctx.aggregateType().getText()
        column = ctx.STRING(0).getText().replace('"', '')
        
        agg_operation = {
            "type": "aggregate",
            "aggregate_type": agg_type,
            "column": column
        }
        
        # Si hay una condición WHERE
        if ctx.filterCondition():
            filter_cond = self.visitFilterCondition(ctx.filterCondition())
            agg_operation["filter_condition"] = filter_cond
        
        self.operations.append(agg_operation)
        return None
        
    def visitFilterCondition(self, ctx):
        column = ctx.STRING().getText().replace('"', '')
        op = ctx.OPERATOR().getText()
        value = self._extract_value(ctx.value())
        
        filter_cond = {
            "column": column,
            "operator": op,
            "value": value
        }
        
        # Si hay un operador lógico, procesar la condición anidada
        if ctx.LOGICAL_OP():
            logical_op = ctx.LOGICAL_OP().getText()
            nested_cond = self.visitFilterCondition(ctx.filterCondition())
            filter_cond["logical_op"] = logical_op
            filter_cond["nested_condition"] = nested_cond
            
        return filter_cond

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
        
        # Imprimir los resultados
        if self.aggregations:
            print("\nResultados de las agregaciones:")
            for agg_name, agg_value in self.aggregations.items():
                print(f"{agg_name}: {agg_value}")
                self.results.append({agg_name: agg_value})
        else:
            print("\nRegistros filtrados:")
            count = 0
            for row in self.filtered_data:
                print(row)
                count += 1
                self.results.append(row)
                if count >= 20:  # Limitar a 20 registros en la impresión
                    print(f"\n... y {len(self.filtered_data) - 20} registros más.")
                    break
                    
        return None
    
    def _execute_operations(self):
        # Ejecutar operaciones acumuladas
        self.data = []
        self.filtered_data = []
        self.aggregations = {}
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
            print(f"Cargado archivo '{filename}' con {len(self.data)} registros.")
        except Exception as e:
            print(f"Error al cargar el archivo '{filename}': {e}")
            self.data = []
            self.filtered_data = []
    
    def _apply_filter(self, filter_operation, data=None):
        if data is None:
            data = self.filtered_data
            result_data = []
        else:
            result_data = []
            
        # Filtro estándar con operador
        if "filter_type" not in filter_operation:
            column = filter_operation["column"]
            operator = filter_operation["operator"]
            value = filter_operation["value"]
            
            for row in data:
                row_value = row[column]
                
                # Convertir a número o booleano si es necesario
                if isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.', '', 1).isdigit()):
                    try:
                        row_value = float(row_value)
                        if isinstance(value, str):
                            value = float(value)
                    except ValueError:
                        pass
                elif isinstance(value, bool) or value in ('true', 'false'):
                    row_value = str(row_value).lower() == 'true'
                    if isinstance(value, str):
                        value = value.lower() == 'true'
                
                # Evaluar la condición del filtro
                condition_met = self._evaluate_condition(row_value, operator, value)
                    
                # Manejar operadores lógicos y filtros anidados
                if "logical_op" in filter_operation and "nested_filter" in filter_operation:
                    nested_result = self._evaluate_nested_filter(row, filter_operation["nested_filter"])
                    logical_op = filter_operation["logical_op"]
                    
                    if logical_op == "AND":
                        condition_met = condition_met and nested_result
                    elif logical_op == "OR":
                        condition_met = condition_met or nested_result
                
                if condition_met:
                    result_data.append(row)
        
        # Filtro BETWEEN
        elif filter_operation["filter_type"] == "between":
            column = filter_operation["column"]
            value1 = filter_operation["value1"]
            value2 = filter_operation["value2"]
            
            for row in data:
                try:
                    row_value = float(row[column])
                    if row_value >= value1 and row_value <= value2:
                        result_data.append(row)
                except (ValueError, TypeError):
                    pass  # Ignorar valores no numéricos
        
        # Filtro IN
        elif filter_operation["filter_type"] == "in":
            column = filter_operation["column"]
            values = filter_operation["values"]
            
            for row in data:
                if row[column] in values:
                    result_data.append(row)
        
        # Filtro LIKE
        elif filter_operation["filter_type"] == "like":
            column = filter_operation["column"]
            pattern = filter_operation["pattern"]
            # Convertir patrón SQL LIKE a regex
            pattern_regex = pattern.replace('%', '.*').replace('_', '.')
            
            for row in data:
                if re.search(pattern_regex, row[column], re.IGNORECASE):
                    result_data.append(row)
        
        if data == self.filtered_data:
            self.filtered_data = result_data
            
        return result_data
    
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
        elif operator == 'contains':
            return str(value2) in str(value1)
        return False
    
    def _evaluate_nested_filter(self, row, filter_operation):
        column = filter_operation["column"]
        operator = filter_operation["operator"]
        value = filter_operation["value"]
        
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
        condition_met = self._evaluate_condition(row_value, operator, value)
            
        # Manejar filtros anidados recursivamente
        if "logical_op" in filter_operation and "nested_filter" in filter_operation:
            nested_result = self._evaluate_nested_filter(row, filter_operation["nested_filter"])
            logical_op = filter_operation["logical_op"]
            
            if logical_op == "AND":
                condition_met = condition_met and nested_result
            elif logical_op == "OR":
                condition_met = condition_met or nested_result
                
        return condition_met
    
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
            elif agg_type == "between":
                self.aggregations[f"min_{column}"] = min(numeric_values)
                self.aggregations[f"max_{column}"] = max(numeric_values)
    
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
        condition_met = self._evaluate_condition(row_value, operator, value)
        
        # Manejar condiciones anidadas
        if "logical_op" in filter_condition and "nested_condition" in filter_condition:
            nested_result = self._evaluate_filter_condition(row, filter_condition["nested_condition"])
            logical_op = filter_condition["logical_op"]
            
            if logical_op == "AND":
                condition_met = condition_met and nested_result
            elif logical_op == "OR":
                condition_met = condition_met or nested_result
        
        return condition_met
        
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
        try:
            return float(value)
        except (ValueError, TypeError):
            return float('-inf')  # Valores no numéricos van al inicio
    
    def _apply_limit(self, limit_operation):
        limit = limit_operation["limit"]
        self.filtered_data = self.filtered_data[:limit]
    
    def _apply_join(self, join_operation):
        second_file = join_operation["second_file"]
        first_key = join_operation["first_key"]
        second_key = join_operation["second_key"]
        
        # Cargar el segundo archivo
        try:
            with open(second_file, newline='', encoding='utf-8') as f:
                second_data = list(csv.DictReader(f))
            
            # Crear un índice para el segundo conjunto de datos
            second_index = {}
            for row in second_data:
                key = row[second_key]
                if key not in second_index:
                    second_index[key] = []
                second_index[key].append(row)
            
            # Realizar la unión
            joined_data = []
            for row in self.filtered_data:
                key = row[first_key]
                if key in second_index:
                    for second_row in second_index[key]:
                        # Crear una nueva fila combinando ambas
                        new_row = {}
                        new_row.update(row)
                        for k, v in second_row.items():
                            if k != second_key:  # Evitar duplicar la columna de unión
                                new_row[f"{second_file.split('.')[0]}_{k}"] = v
                        joined_data.append(new_row)
            
            if joined_data:
                self.filtered_data = joined_data
                print(f"Join realizado: {len(joined_data)} registros resultantes.")
            else:
                print("Warning: El JOIN no produjo resultados.")
                
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
