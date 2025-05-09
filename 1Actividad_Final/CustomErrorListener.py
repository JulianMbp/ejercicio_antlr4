from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error en línea {line}, columna {column}: {msg}")

def main():
    input_stream = FileStream("programa.dsl", encoding='utf-8')
    lexer = CSVFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Instanciamos el parser
    parser = CSVFilterParser(stream)
    
    # Agregar el custom error listener
    parser.removeErrorListeners()  # Elimina los listeners por defecto
    parser.addErrorListener(CustomErrorListener())  # Agrega nuestro listener personalizado
    
    # Intentar parsear el árbol
    try:
        tree = parser.prog()  # Aquí se genera el árbol de análisis
        visitor = MyCSVVisitor()  # Usamos el visitante para recorrer el árbol
        visitor.visit(tree)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
