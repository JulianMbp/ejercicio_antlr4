# Procesador de Consultas CSV con ANTLR4

Este proyecto implementa un mini compilador DSL (Domain Specific Language) para realizar consultas sobre archivos CSV utilizando la herramienta ANTLR4 para el análisis léxico y sintáctico.

## Estructura del Proyecto

- `CSVFilter.g4`: Gramática ANTLR4 que define la sintaxis del DSL
- `main.py`: Programa principal con interfaz de usuario y funcionalidades
- `MyCSVVisitor.py`: Implementación del visitante que ejecuta las operaciones DSL
- `eventos.csv`: Archivo de datos de ejemplo

## Requisitos

- Python 3.6 o superior
- ANTLR4 Runtime para Python
- Java Runtime Environment (para análisis sintáctico visual)

## Uso del Programa

### Ejecutar el programa principal

```bash
python main.py
```

Este comando inicia la interfaz interactiva que permite:
- Filtrar por costo de entrada
- Filtrar por tipo de evento
- Filtrar por lugar
- Ver estadísticas de eventos
- Realizar filtros avanzados combinados

### Ejecutar consultas desde un archivo DSL

```bash
# Crear un archivo DSL con la consulta
echo 'load "eventos.csv"; filter column "tipo_evento" == "Concierto"; print;' > test.dsl

# Ejecutar la consulta directamente
python main.py test.dsl
```

### Ejecutar consultas desde un archivo JSON

```bash
python main.py consultas.json
```

## Análisis Sintáctico

Para realizar análisis sintáctico de las consultas DSL, puedes usar los siguientes comandos:

### Ver tokens (análisis léxico)

```bash
cat test.dsl | antlr4-parse CSVFilter.g4 prog -tokens
```

Este comando muestra cada token reconocido por el analizador léxico, incluyendo su tipo y posición.

### Ver árbol sintáctico en formato texto

```bash
cat test.dsl | antlr4-parse CSVFilter.g4 prog -tree
```

Este comando muestra el árbol sintáctico en formato de texto, mostrando la estructura jerárquica de la consulta.

### Visualizar árbol sintáctico con interfaz gráfica

```bash
cat test.dsl | antlr4-parse CSVFilter.g4 prog -gui
```

Este comando abre una ventana gráfica que muestra el árbol sintáctico de manera visual.

## Sintaxis del DSL

El DSL soporta las siguientes operaciones:

### Cargar un archivo CSV
```
load "archivo.csv";
```

### Filtrar datos
```
filter column "nombre_columna" == "valor";
filter column "costo" > 1000;
filter column "fecha" between 2022-01-01 and 2022-12-31;
filter column "categoria" in ("A", "B", "C");
filter column "descripcion" like "patrón%";
```

### Agregar datos
```
aggregate count column "id_evento";
aggregate sum column "costo_entrada";
aggregate average column "cantidad_asistentes";
aggregate min column "costo_entrada";
aggregate max column "costo_entrada";
```

### Ordenar resultados
```
sort by "columna" asc;
sort by "columna" desc;
```

### Limitar resultados
```
limit 10;
```

### Imprimir resultados
```
print;
```

## Generación de Código ANTLR4

Si necesitas regenerar los archivos de parser y lexer:

```bash
# Generar archivos Java
antlr4 CSVFilter.g4

# Generar archivos Python
antlr4 -Dlanguage=Python3 CSVFilter.g4
```

## Ejemplos de Consultas

### Filtro simple
```
load "eventos.csv";
filter column "tipo_evento" == "Concierto";
print;
```

### Filtro combinado
```
load "eventos.csv";
filter column "tipo_evento" == "Concierto";
filter column "costo_entrada" > 100000;
sort by "fecha" asc;
print;
```

### Agregación
```
load "eventos.csv";
aggregate average column "costo_entrada";
print;
```