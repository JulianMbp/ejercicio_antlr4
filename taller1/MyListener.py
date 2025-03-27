from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitIfElse(self, ctx):
        print("🔍 Se detectó un bloque IF-ELSE")

    def exitAssign(self, ctx):
        print("✍️ Asignación detectada:", ctx.getText())

    def exitCondicionSimple(self, ctx):
        print("⚠️ Condición con variable:", ctx.ID().getText(), ctx.op.text, ctx.INT().getText())
        
    def exitForLoop(self, ctx):
        print("🔄 Se detectó un bucle FOR:", ctx.getText())
        
    def exitInicializacion(self, ctx):
        print("🏁 Inicialización detectada:", ctx.getText())
        
    def exitCondicion(self, ctx):
        print("🔍 Condición detectada:", ctx.getText())
        
    def exitActualizacion(self, ctx):
        print("⏫ Actualización detectada:", ctx.getText())