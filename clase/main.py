from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor

input_stream = FileStream("programa.dsl", encoding='utf-8')
lexer = CSVFilterLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = CSVFilterParser(stream)

# Manejo de errores
tree = parser.prog()
visitor = MyCSVVisitor()
visitor.visit(tree)