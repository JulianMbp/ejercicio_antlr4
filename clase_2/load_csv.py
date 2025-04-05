import sys
from antlr4 import *
from CSVLexer import CSVLexer
from CSVParser import CSVParser
from CSVListener import CSVListener

class Loader(CSVListener):
    EMPTY = ""
    def __init__(self):
        self.rows = []
        self.header = []
        self.currentRowFieldValues = []

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
        

    def exitText(self, ctx:CSVParser.TextContext):
        self.currentRowFieldValues.append(ctx.getText())
        print(f"Valor 1 ctx -->{ctx.getText()}")

    def exitString(self, ctx:CSVParser.StringContext):
        self.currentRowFieldValues.append(ctx.getText())
        print(f"Valor 2 ctx -->{ctx.getText()}")

    def exitEmpty(self, ctx:CSVParser.EmptyContext):
        self.currentRowFieldValues.append(self.EMPTY)
        print(f"Valor 3 ctx -->{ctx.getText()}")

    def exitHeader(self, ctx:CSVParser.HeaderContext):
        self.header = list(self.currentRowFieldValues)

    def exitRow(self, ctx:CSVParser.RowContext):
        # Evita procesar la fila si es parte del header
        if ctx.parentCtx.getRuleIndex() == CSVParser.RULE_header:
            return

        m = {}
        for i, val in enumerate(self.currentRowFieldValues):
            key = self.header[i] if i < len(self.header) else f"col_{i}"
            m[key] = val
        self.rows.append(m)


def main(argv):
    input_stream = FileStream(argv[1], encoding='utf-8')
    lexer = CSVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CSVParser(stream)
    tree = parser.csvFile()

    loader = Loader()
    walker = ParseTreeWalker()
    walker.walk(loader, tree)

    for row in loader.rows:
        print(row)

if __name__ == '__main__':
    main(sys.argv)