from antlr4 import *
from MiGramaticaLexer import MiGramaticaLexer
from MiGramaticaParser import MiGramaticaParser
from MyListener import MyListener
from antlr4.tree.Trees import Trees

def main():
    # Pedir entrada al usuario
    input_string = input('Introduce el código a analizar: ')
    
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
    
    # Crear un recorredor de árboles
    walker = ParseTreeWalker()
    
    # Recorrer el árbol con nuestro Listener
    listener = MyListener()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
