from MiGramaticaVisitor import MiGramaticaVisitor
from MiGramaticaParser import MiGramaticaParser

class EvalVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.variables = {}
        
    def visitPrograma(self, ctx):
        result = None
        for i in range(ctx.getChildCount() - 1):  # -1 para ignorar EOF
            if isinstance(ctx.getChild(i), MiGramaticaParser.SentenciaContext):
                result = self.visit(ctx.getChild(i))
        return self.variables
    
    def visitSentencia(self, ctx):
        result = None
        for i in range(ctx.getChildCount()):
            if not ctx.getChild(i).getText() == ';':
                result = self.visit(ctx.getChild(i))
        return result
    
    def visitForLoop(self, ctx):
        # Ejecutar inicialización
        self.visit(ctx.inicializacion())
        
        # Evaluar condición inicial
        continuar = self.evaluarCondicion(ctx.condicion())
        
        # Mientras la condición sea verdadera
        while continuar:
            # Ejecutar el cuerpo del bucle
            for i in range(ctx.getChildCount()):
                if isinstance(ctx.getChild(i), MiGramaticaParser.SentenciaContext):
                    self.visit(ctx.getChild(i))
            
            # Ejecutar la actualización
            self.visit(ctx.actualizacion())
            
            # Reevaluar la condición
            continuar = self.evaluarCondicion(ctx.condicion())
            
        print(f"Ciclo for completado. Variables: {self.variables}")
        return None
    
    def evaluarCondicion(self, ctx):
        var = ctx.ID().getText()
        op = ctx.operadorComparacion().getText()
        valor_expr = self.visit(ctx.expresion())
        
        if var not in self.variables:
            self.variables[var] = 0
            
        valor_var = self.variables[var]
        
        if op == '<':
            return valor_var < valor_expr
        elif op == '>':
            return valor_var > valor_expr
        elif op == '==':
            return valor_var == valor_expr
        elif op == '!=':
            return valor_var != valor_expr
        elif op == '<=':
            return valor_var <= valor_expr
        elif op == '>=':
            return valor_var >= valor_expr
        return False
    
    def visitInicializacion(self, ctx):
        var = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.variables[var] = valor
        print(f"Inicialización: {var} = {valor}")
        return valor
    
    def visitActualizacion(self, ctx):
        var = ctx.ID().getText()
        op = ctx.operadorAsignacion().getText()
        valor_expr = self.visit(ctx.expresion())
        
        if var not in self.variables:
            self.variables[var] = 0
            
        if op == '=':
            self.variables[var] = valor_expr
        elif op == '+=':
            self.variables[var] += valor_expr
        elif op == '-=':
            self.variables[var] -= valor_expr
        elif op == '*=':
            self.variables[var] *= valor_expr
        elif op == '/=':
            self.variables[var] /= valor_expr
            
        print(f"Actualización: {var} {op} {valor_expr}, ahora {var} = {self.variables[var]}")
        return self.variables[var]
    
    def visitAsignacion(self, ctx):
        var = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.variables[var] = valor
        print(f"Asignación: {var} = {valor}")
        return valor
    
    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        
        if op == '*':
            return left * right
        else:  # op == '/'
            if right == 0:
                print("Error: División por cero")
                return 0
            return left / right
    
    def visitAddSub(self, ctx):
        left = self.visit(ctx.expresion(0))
        right = self.visit(ctx.expresion(1))
        op = ctx.getChild(1).getText()
        
        if op == '+':
            return left + right
        else:  # op == '-'
            return left - right
    
    def visitInt(self, ctx):
        return int(ctx.getText())
    
    def visitVariable(self, ctx):
        var = ctx.getText()
        if var not in self.variables:
            print(f"Variable '{var}' no inicializada, se asume 0")
            self.variables[var] = 0
        return self.variables[var]
    
    def visitParens(self, ctx):
        return self.visit(ctx.expresion()) 