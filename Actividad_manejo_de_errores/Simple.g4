grammar Simple;

prog: classDef+ ;

classDef
    : 'class' ID '{' member+ '}' 
    ;

member
    : 'int' ID ';'                                       
    | 'int' ID '(' ID ')' '{' stat* '}'                  
    ;

stat
    : expr ';'                                           
    | ID '=' expr ';'                                    
    ;

expr
    : expr op=('*'|'/') expr      # MulDiv
    | expr op=('+'|'-') expr      # AddSub
    | ID '(' expr ')'             # FuncCall
    | INT                         # Int
    | ID                          # Variable
    | '(' expr ')'                # Parens
    ;

INT : [0-9]+ ;
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;
WS  : [ \t\r\n]+ -> skip ;
