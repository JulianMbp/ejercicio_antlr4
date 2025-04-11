import json
from antlr4 import *
from JSONLexer import JSONLexer
from JSONParser import JSONParser
from JSONListener import JSONListener

class XMLEmitter(JSONListener):
    def __init__(self):
        self.xml_map = {}

    def getXML(self, ctx):
        return self.xml_map.get(ctx, '')

    def setXML(self, ctx, value):
        self.xml_map[ctx] = value

    def exitString(self, ctx):
        self.setXML(ctx, ctx.getText().strip('"'))

    def exitAtom(self, ctx):
        self.setXML(ctx, ctx.getText())

    def exitPair(self, ctx):
        tag = ctx.STRING().getText().strip('"')
        val = self.getXML(ctx.value())
        self.setXML(ctx, f"<{tag}>{val}</{tag}>\n")

    def exitAnObject(self, ctx):
        contenido = ''.join(self.getXML(p) for p in ctx.pair())
        indentado = self.indentar(contenido)
        self.setXML(ctx, f"<objeto>\n{indentado}</objeto>\n")

    def exitArrayOfValues(self, ctx):
        body = ''.join(f"<element>{self.getXML(v)}</element>\n" for v in ctx.value())
        indentado = self.indentar(body)
        self.setXML(ctx, indentado)

    def exitJson(self, ctx):
        self.setXML(ctx, self.getXML(ctx.getChild(0)))

    def indentar(self, texto, nivel=1):
        tab = "  " * nivel
        return ''.join(f"{tab}{line}\n" for line in texto.strip().splitlines())

# -----------------------------------------
# 🔍 VALIDACIÓN BÁSICA DEL JSON
# -----------------------------------------
def validar_json(diccionario, path="root"):
    if not isinstance(diccionario, dict):
        raise ValueError(f"{path}: No es un objeto JSON válido.")
    for clave, valor in diccionario.items():
        if not isinstance(clave, str):
            raise ValueError(f"{path}: Clave no válida ({clave})")
        if isinstance(valor, dict):
            validar_json(valor, f"{path}.{clave}")
        elif isinstance(valor, list):
            for i, item in enumerate(valor):
                if isinstance(item, dict):
                    validar_json(item, f"{path}.{clave}[{i}]")

# -----------------------------------------
# 🚀 MAIN
# -----------------------------------------
def main():
    # ✅ Validar JSON antes de procesar
    with open("t.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
        validar_json(datos)

    # ✅ Leer con ANTLR y convertir a XML
    input_stream = FileStream("t.json", encoding='utf-8')
    lexer = JSONLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = JSONParser(stream)
    tree = parser.json()

    listener = XMLEmitter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    with open("salida.xml", "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<root>\n')
        f.write(listener.getXML(tree))
        f.write('</root>\n')

    print("✅ XML generado en 'salida.xml'")

if __name__ == '__main__':
    main()
