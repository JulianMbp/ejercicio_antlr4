# 🛠 Proyecto: Procesamiento de CSV y Conversión de JSON a XML con ANTLR y Python

## 👨‍💻 Desarrollador
- Julian M. Bastidas Perez

## 📚 Descripción General

Este proyecto implementa un sistema para el procesamiento de datos en formato **CSV** y **JSON**, con capacidades de limpieza, validación, análisis y transformación de datos. La solución utiliza **ANTLR 4** para la definición de gramáticas y **Python** para la implementación de la lógica de negocio.

---

## 📋 Actividades Implementadas

| Tarea                                                               | Estado |
|---------------------------------------------------------------------|--------|
| Exportar JSON a XML jerárquico y legible con indentación           | ✅     |
| Validar la estructura básica del JSON antes de convertirlo         | ✅     |
| Leer y analizar archivos CSV con ANTLR                             | ✅     |
| Limpiar montos en formato string (`$`, `,`, `""`)                  | ✅     |
| Detectar campos vacíos o mal formateados en columna "Cantidad"     | ✅     |
| Detectar filas duplicadas                                          | ✅     |
| Contar cuántos campos vacíos hay en total                          | ✅     |
| Contar cuántos registros por mes existen                           | ✅     |
| Generar un diccionario `{"Junio": total_montos}`                   | ✅     |
| Exportar datos limpios a JSON y CSV                                | ✅     |

---

## ▶️ Instrucciones para Ejecutar los Archivos

### 1. Procesamiento de CSV
Para ejecutar el procesador de archivos CSV:
```bash
python csv_processor.py
```
**Función**: Este script procesa el archivo `data.csv`, limpia los datos, detecta filas duplicadas, valida campos y genera estadísticas.
**Resultado**: Genera un archivo `limpio.json` con los datos procesados.

### 2. Conversión de JSON a XML
Para convertir archivos JSON a XML:
```bash
python json_to_xml.py
```
**Función**: Este script analiza el archivo `t.json` utilizando la gramática ANTLR definida, valida su estructura y lo convierte a formato XML.
**Resultado**: Genera un archivo `salida.xml` con el XML estructurado y formateado.

---

## 🧠 Anotaciones y Decisiones Clave del Desarrollo

### Arquitectura y Diseño
- **Modularidad**: Se optó por separar las gramáticas ANTLR en archivos distintos (CSV.g4 y JSON.g4) para facilitar el mantenimiento y claridad del código.
- **Encapsulamiento**: Se implementaron clases dedicadas para cada funcionalidad principal (`CSVProcessor` y `XMLEmitter`), aplicando principios de diseño orientado a objetos.
- **Extensibilidad**: La arquitectura permite extender fácilmente las funcionalidades mediante la adición de nuevos métodos a las clases existentes.

### Decisiones Técnicas Importantes
- Se utilizó **ANTLR 4.13.2** para definir gramáticas específicas que permiten un análisis sintáctico robusto.
- Se implementó el **runtime de Python de ANTLR** junto con `FileStream` y `ParseTreeWalker` para construir el XML manualmente desde el árbol sintáctico.
- Se desarrolló una validación recursiva del JSON para garantizar estructuras válidas antes de la conversión a XML.
- Se utilizó `DictReader` en Python para procesar archivos CSV de forma flexible y eficiente.
- Se creó una función de indentación personalizada para garantizar que el XML generado sea legible y bien formateado.

### Optimizaciones y Mejoras
- Se implementó la detección de campos vacíos y filas duplicadas utilizando estructuras de datos eficientes como sets para maximizar el rendimiento.
- La clase `XMLEmitter` extiende `JSONListener` para aprovechar el patrón Visitor y generar XML estructurado de manera eficiente.
- La conversión de fechas (de "06" a "Junio") se realiza manualmente para mayor claridad y control en el procesamiento de datos temporales.

### Observaciones Durante el Desarrollo
- El uso de ANTLR simplificó significativamente el análisis sintáctico de formatos complejos.
- La separación de la lógica de negocio del procesamiento de la gramática mejoró la mantenibilidad del código.
- Se realizaron pruebas extensivas para garantizar la robustez de la solución frente a diferentes estructuras de datos de entrada.
- El desarrollo se realizó en Visual Studio debido a problemas con Codespace durante el período de implementación.

---

## 📂 Estructura del Proyecto

Los principales archivos del proyecto son:

- **CSV.g4**: Gramática ANTLR para el formato CSV
- **JSON.g4**: Gramática ANTLR para el formato JSON
- **csv_processor.py**: Clase para procesar, limpiar y analizar archivos CSV
- **json_to_xml.py**: Implementación para convertir JSON a XML usando ANTLR
- **data.csv**: Archivo CSV de ejemplo para procesamiento
- **t.json**: Archivo JSON de ejemplo para conversión a XML
- **limpio.json**: Resultado del procesamiento del CSV
- **salida.xml**: Resultado de la conversión de JSON a XML

---

## 📝 Requisitos y Notas Adicionales

- Los archivos generados por ANTLR (Lexer, Parser, Listener) son necesarios para que los scripts principales funcionen correctamente.
- El proyecto está configurado para trabajar con codificación UTF-8 en todos los archivos.
- La librería ANTLR utilizada (antlr-4.13.1-complete.jar) debe estar presente en el directorio del proyecto.
