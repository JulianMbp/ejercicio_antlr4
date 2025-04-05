# Prueba 1 

 antlr4 -Dlanguage=Python3 CSV.g4

python load_csv.py CSV.csv


## se agrego la impresion de los datos del getText --> load_csv.py
```python
    def exitText(self, ctx:CSVParser.TextContext):
        self.currentRowFieldValues.append(ctx.getText())
        print(f"Valor 1 ctx -->{ctx.getText()}")
        """ para ver texto """

    def exitString(self, ctx:CSVParser.StringContext):
        self.currentRowFieldValues.append(ctx.getText())
        print(f"Valor 2 ctx -->{ctx.getText()}")
        """ para ver en comillas dobles """

    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        self.currentRowFieldValues.append(self.EMPTY)
        print(f"Valor 3 ctx -->{ctx.getText()}")
        """ para ver valores vacios """

    
```

##  Validar que todas las filas tengan el mismo número de columnas

```python
def exitRow(self, ctx:CSVParser.RowContext):
    if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
        return

    if len(self.currentRowFieldValues) != len(self.header):
        print(f"Fila inválida: {self.currentRowFieldValues}")

    # Como antes: convertir en dict
    m = {}
    for i, val in enumerate(self.currentRowFieldValues):
        key = self.header[i] if i < len(self.header) else f"col_{i}"
        m[key] = val
    self.rows.append(m)
```