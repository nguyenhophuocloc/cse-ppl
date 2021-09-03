class StaticCheck(Visitor):
    #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o):
        o={}
        for decl in ctx.decl:
            self.visit(decl,o)
        for stmt in ctx.stmts:
            self.visit(stmt,o)
    #name:str
    def visitVarDecl(self,ctx:VarDecl,o):
        o[ctx.name]=''
    #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o): #nghiên cứu lại ở dây
        """
        typ1=self.visit(ctx.lhs,o)
        typ2=self.visit(ctx.rhs,o)
        if typ1=='' and typ2=='':
            raise TypeCannotBeInferred(ctx)
        elif typ1=='' and typ2!='':
            typ1=typ2
            o[ctx.lhs.name]=typ2
        elif typ1!='' and typ2=='':
            typ2=typ1
            o[ctx.rhs.name]=typ1
        elif typ1!=typ2:
            raise TypeMismatchInStatement(ctx)
        """        
        type2 = self.visit(ctx.rhs, o)
        type1 = self.visit(ctx.lhs, o)
        if type2 == '' and type1 == '':
            raise TypeCannotBeInferred(ctx)
        elif type2 == '' and type1 != '':
            type2 = type1
            o[ctx.rhs.name] = type2
        elif type2 != '' and type1 == '':
            type1 = type2
            o[ctx.lhs.name] = type1
        else:
            if type1 != type2:
                raise TypeMismatchInStatement(ctx)
     #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o):
        typ1=self.visit(ctx.e1,o)
        typ2=self.visit(ctx.e2,o)
        op=ctx.op
        if op in ['+','-','*','/']:
            if typ1=='':
                typ1='int'
                o[ctx.e1.name]=typ1
            if typ2=='':
                typ2='int'
                o[ctx.e2.name]=typ2
            if typ1!='int' or typ2!='int':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        if op in ['>','=']:
            if typ1=='':
                typ1='int'
                o[ctx.e1.name]=typ1
            if typ2=='':
                typ2='int'
                o[ctx.e2.name]=typ2
            if typ1!='int' or typ2!='int':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        if op in ['>.','=.']:
            if typ1=='':
                typ1='float'
                o[ctx.e1.name]=typ1
            if typ2=='':
                typ2='float'
                o[ctx.e2.name]=typ2
            if typ1!='float' or typ2!='float':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        if op in ['+.','-.','*.','/.']:
            if typ1=='':
                typ1='float'
                o[ctx.e1.name]=typ1
            if typ2=='':
                typ2='float'
                o[ctx.e2.name]=typ2
            if typ1!='float' or typ2!='float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        if op in ['&&','||','>b','=b']:
            if typ1=='':
                typ1='bool'
                o[ctx.e1.name]=typ1
            if typ2=='':
                typ2='bool'
                o[ctx.e2.name]=typ2
            if typ1!='bool' or typ2!='bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'

    def visitUnOp(self,ctx:UnOp,o):
        typ=self.visit(ctx.e,o)
        op=ctx.op
        if op=='-':
            if typ=='':
                typ='int'
                o[ctx.e.name]=typ
            if typ!='int':
                raise TypeMismatchInExpression(ctx)
            return 'int'
        if op=='-.':
            if typ=='':
                typ='float'
                o[ctx.e.name]=typ
            if typ!='float':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        if op=='!':
            if typ=='':
                typ='bool'
                o[ctx.e.name]=typ
            if typ!='bool':
                raise TypeMismatchInExpression(ctx)
            return 'bool'
        if op=='i2f':
            if typ=='':
                typ='int'
                o[ctx.e.name]=typ
            if typ!='int':
                raise TypeMismatchInExpression(ctx)
            return 'float'
        if op=='floor':
            if typ=='':
                typ='float'
                o[ctx.e.name]=typ
            if typ!='float':
                raise TypeMismatchInExpression(ctx)
            return 'int'

    def visitIntLit(self,ctx:IntLit,o):
        return 'int' 

    def visitFloatLit(self,ctx,o):
        return 'float'

    def visitBoolLit(self,ctx,o):
        return 'bool'
    #name
    def visitId(self,ctx,o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]  #type
        