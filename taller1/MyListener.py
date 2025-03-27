from MiGramaticaListener import MiGramaticaListener

class MyListener(MiGramaticaListener):
    def exitForLoop(self, ctx):
        print(f"Detectado bucle for: {ctx.getText()}")
        
    def exitInicializacion(self, ctx):
        var = ctx.ID().getText()
        expr = ctx.expresion().getText()
        print(f"Inicialización detectada: {var} = {expr}")
        
    def exitCondicion(self, ctx):
        var = ctx.ID().getText()
        op = ctx.operadorComparacion().getText()
        expr = ctx.expresion().getText()
        print(f"Condición detectada: {var} {op} {expr}")
        
    def exitActualizacion(self, ctx):
        var = ctx.ID().getText()
        op = ctx.operadorAsignacion().getText()
        expr = ctx.expresion().getText()
        print(f"Actualización detectada: {var} {op} {expr}")
        
    def exitAsignacion(self, ctx):
        var = ctx.ID().getText()
        expr = ctx.expresion().getText()
        print(f"Asignación detectada: {var} = {expr}") 