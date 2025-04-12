from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from SimpleLexer import SimpleLexer
from SimpleParser import SimpleParser
from SimpleListener import SimpleListener
from antlr4 import ParseTreeWalker

# Listener personalizado
class SimpleCustomListener(SimpleListener):
    def enterClassDef(self, ctx):
        class_name = ctx.ID().getText()
        print(f"🏛️ Clase encontrada: {class_name}")

    def enterMember(self, ctx):
        if ctx.getChildCount() == 3:  
            var_name = ctx.ID().getText()
            print(f"🔸 Variable miembro: int {var_name}")
        elif ctx.getChildCount() > 3: 
            method_name = ctx.ID(0).getText()
            param = ctx.ID(1).getText()
            print(f"🔹 Método encontrado: int {method_name}({param})")

    def enterStat(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == '=':
            var = ctx.getChild(0).getText()
            expr = ctx.getChild(2).getText()
            print(f"🧾 Asignación: {var} = {expr}")



class VerboseErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"❌ Error de sintaxis en línea {line}, columna {column}: {msg}")

# Función que parsea y aplica el listener
def parse_input(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SimpleParser(tokens)

    parser.removeErrorListeners()
    parser.addErrorListener(VerboseErrorListener())

    try:
        tree = parser.prog()
        print("✅ Entrada válida.")
        # Aplicar el listener personalizado
        walker = ParseTreeWalker()
        walker.walk(SimpleCustomListener(), tree)
    except Exception as e:
        print("⚠️ Excepción atrapada:", str(e))

# Pruebas
if __name__ == "__main__":
    casos = [
        ("=== Prueba 1 ===", "class A { int x; }"),
        ("=== Prueba 2 ===", "class A { int x; }"),
        ("=== Prueba 3 ===", "class B { int f(x) { x = 3; } }"),
        ("=== Prueba 4 ===", "class C { int f(a) { x = 3; } }"),
        ("=== Prueba 5 ===", "class D { int f(x) { x = 3;} }"),
        ("=== Prueba 6 ===", "class E { int f(a) { x = 3 + 4 + 5; } }"),
        ("=== Prueba 7 ===", "class F {  int f(a)  { x = 1; }}"),
        ("=== Prueba 8 ===", "class G { int x; }"),
        ("=== Prueba 9 ===", "class H { int f(x) { x = 3; } }"),
        ("=== Prueba 10 ===", "class I { int f(x) { } }")
    ]

    for titulo, entrada in casos:
        print(titulo)
        parse_input(entrada)
        print("-" * 50)
