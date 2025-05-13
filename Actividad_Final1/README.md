# Mini-Compilador DSL para Consultas de Eventos Culturales

Este proyecto implementa un mini-compilador basado en DSL (Domain Specific Language) que permite realizar consultas dinámicas sobre un archivo CSV de eventos culturales, mediante instrucciones secuenciales tipo comando.

## Estructura del Proyecto

- `CSVFilter.g4`: Gramática ANTLR4 que define el DSL
- `main.py`: Punto de entrada del programa con menú interactivo
- `MyCSVVisitor.py`: Implementación del visitante que procesa las instrucciones DSL
- `CustomErrorListener.py`: Manejador de errores personalizado
- `consultas.json`: Archivo con 40 consultas predefinidas
- `eventos.csv`: Archivo CSV con datos de eventos culturales

## Estructura del CSV

El archivo CSV incluye los siguientes campos:
- id_evento
- nombre_evento
- tipo_evento
- fecha
- lugar
- organizador
- costo_entrada
- cantidad_asistentes
- patrocinadores
- estado_evento

## Menú Interactivo

El programa cuenta con un menú interactivo que permite:
1. Ejecutar todas las consultas predefinidas
2. Seleccionar una consulta predefinida específica
3. Ejecutar un archivo DSL personalizado
4. Ejecutar un archivo JSON personalizado

## Instrucciones del DSL

El DSL soporta las siguientes instrucciones:

### 1. Cargar datos desde un archivo CSV
```
load "eventos.csv";
```

### 2. Aplicar filtros sobre campos

#### Filtros básicos
```
filter column "campo" operador valor;
```

Operadores soportados: `>=`, `<=`, `>`, `<`, `==`, `!=`, `contains`

#### Filtros BETWEEN
```
filter column "campo" between valor1 and valor2;
```

#### Filtros IN
```
filter column "campo" in (valor1, valor2, valor3);
```

#### Filtros LIKE (búsqueda por patrón)
```
filter column "campo" like "patrón";
```
Donde % representa cualquier secuencia de caracteres y _ representa un solo carácter.

### 3. Filtros combinados con operadores lógicos
```
filter column "campo1" operador valor1 AND filter column "campo2" operador valor2;
filter column "campo1" operador valor1 OR filter column "campo2" operador valor2;
```

### 4. Operaciones de agregación
```
aggregate count column "campo";
aggregate sum column "campo";
aggregate average column "campo";
aggregate min column "campo";
aggregate max column "campo";
aggregate between column "campo";
```

### 5. Agregaciones con condiciones
```
aggregate count column "campo" where "condición_campo" operador valor;
```

### 6. Ordenar resultados
```
sort by "campo" asc;
sort by "campo" desc;
```

### 7. Limitar resultados
```
limit 10;
```

### 8. Agrupar resultados
```
group by "campo";
```

### 9. Realizar JOIN entre archivos CSV
```
join "segundo_archivo.csv" on "clave_primaria" = "clave_secundaria";
```

### 10. Imprimir resultados
```
print;
```

## Formato JSON

También se pueden definir consultas en formato JSON:

```json
{
    "consultas": [
        {
            "id": 1,
            "descripcion": "Descripción de la consulta",
            "operaciones": [
                {
                    "tipo": "load",
                    "archivo": "eventos.csv"
                },
                {
                    "tipo": "filter",
                    "columna": "costo_entrada",
                    "operador": ">",
                    "valor": 100000
                },
                {
                    "tipo": "aggregate",
                    "funcion": "count",
                    "columna": "id_evento"
                },
                {
                    "tipo": "print"
                }
            ]
        }
    ]
}
```

También se pueden incluir instrucciones DSL directamente en el JSON:

```json
{
    "consultas": [
        {
            "id": 1,
            "descripcion": "Descripción de la consulta",
            "operaciones": [
                {
                    "tipo": "load",
                    "archivo": "eventos.csv"
                },
                {
                    "instruccion": "filter column \"costo_entrada\" > 50000 AND filter column \"cantidad_asistentes\" > 3000;"
                },
                {
                    "tipo": "print"
                }
            ]
        }
    ]
}
```

## Cómo ejecutar

1. Para iniciar el menú interactivo:
   ```
   python main.py
   ```

2. Para ejecutar directamente un script en formato JSON:
   ```
   python main.py archivo.json
   ```

3. Para ejecutar directamente un script en formato DSL:
   ```
   python main.py archivo.dsl
   ```

## Tipos de datos soportados

- Enteros (sin comillas): 123, 456
- Flotantes (con punto decimal): 123.45
- Cadenas (entre comillas dobles): "texto"
- Booleanos: true, false

## Requisitos

- Python 3.6 o superior
- ANTLR4 runtime para Python 