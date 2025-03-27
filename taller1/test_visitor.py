from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from EvalVisitor import EvalVisitor
from antlr4.tree.Trees import Trees

def main():
    # Pedir entrada al usuario
    input_string = input('Introduce el código a evaluar: ')
    
    # Crear el flujo de entrada ANTLR
    input_stream = InputStream(input_string)
    
    # Crear el analizador léxico
    lexer = MiGramaticaLexer(input_stream)
    
    # Crear un flujo de tokens
    token_stream = CommonTokenStream(lexer)
    
    # Crear el analizador sintáctico
    parser = MiGramaticaParser(token_stream)
    
    # Obtener el árbol de análisis
    tree = parser.programa()
    
    # Imprimir el árbol de análisis
    print("Árbol de análisis:")
    print(Trees.toStringTree(tree, None, parser))
    
    # Crear y ejecutar el visitor
    visitor = EvalVisitor()
    resultado = visitor.visit(tree)
    
    # Mostrar el estado final de las variables
    print("\nEstado final de las variables:")
    for var, valor in resultado.items():
        print(f"{var} = {valor}")

if __name__ == '__main__':
    main() 