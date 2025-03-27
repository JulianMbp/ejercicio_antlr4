if __name__ is not None and "." in __name__:
    from .MiGramaticaParser import MiGramaticaParser
    from .MiGramaticaVisitor import MiGramaticaVisitor
else:
    from MiGramaticaParser import MiGramaticaParser
    from MiGramaticaVisitor import MiGramaticaVisitor

class TreeVisitor(MiGramaticaVisitor):
    def __init__(self):
        self.nivell = 0

    def visitExpr(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            print(" " * self.nivell + 
                  MiGramaticaParser.symbolicNames[l[0].getSymbol().type] +
                  '(' + l[0].getText() + ')')
        else:  # len(l) == 3
            print(' ' * self.nivell + 'MAS(+)')
            self.nivell += 1
            self.visit(l[0])
            self.visit(l[2])
            self.nivell -= 1