from SimpleListener import SimpleParserListener

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
