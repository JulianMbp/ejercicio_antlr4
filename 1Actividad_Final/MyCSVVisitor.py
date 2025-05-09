import csv
from CSVFilterVisitor import CSVFilterVisitor

class MyCSVVisitor(CSVFilterVisitor):
    def __init__(self):
        self.data = []
        self.filtered_data = []
        self.filename = ""

    def visitLoadStat(self, ctx):
        self.filename = ctx.STRING().getText().replace('"', '')
        with open(self.filename, newline='', encoding='utf-8') as f:
            self.data = list(csv.DictReader(f))
        self.filtered_data = self.data  # Por defecto, sin filtrar
        return None

    def visitFilterStat(self, ctx):
        self.filtered_data = [row for row in self.data if self.eval_expr(ctx.expr(), row)]
        return None

    def eval_expr(self, expr, row):
        # Maneja operadores lógicos AND y OR
        if expr.AND():
            return self.eval_expr(expr.expr(0), row) and self.eval_expr(expr.expr(1), row)
        elif expr.OR():
            return self.eval_expr(expr.expr(0), row) or self.eval_expr(expr.expr(1), row)
        elif expr.getChildCount() == 3 and expr.getChild(0).getText() == '(':
            # Expresión entre paréntesis
            return self.eval_expr(expr.expr(0), row)
        else:
            # Comparación simple: column "edad" > 25
            col = expr.STRING().getText().replace('"', '')
            op = expr.OPERATOR().getText()
            val = int(expr.INT().getText())
            row_val = int(row[col])
            return eval(f"{row_val} {op} {val}")

    def visitPrintStat(self, ctx):
        for row in self.filtered_data:
            print(row)
        return None
