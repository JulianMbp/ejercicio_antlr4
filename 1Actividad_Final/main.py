from antlr4 import *
from CSVFilterLexer import CSVFilterLexer
from CSVFilterParser import CSVFilterParser
from MyCSVVisitor import MyCSVVisitor
from CustomErrorListener import CustomErrorListener  # Importamos el listener personalizado

def main():
    input_stream = FileStream("programa.dsl", encoding='utf-8')
    lexer = CSVFilterLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    # Instanciamos el parser
    parser = CSVFilterParser(stream)
    
    # Elimina los listeners por defecto
    parser.removeErrorListeners()
    # Agrega el CustomErrorListener
    parser.addErrorListener(CustomErrorListener())
    
    # Intentar parsear el árbol
    try:
        tree = parser.prog()  # Aquí se genera el árbol de análisis
        visitor = MyCSVVisitor()  # Usamos el visitante para recorrer el árbol
        visitor.visit(tree)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
