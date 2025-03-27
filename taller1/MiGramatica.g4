grammar MiGramatica;

programa : sentencia+ EOF ;

sentencia : forLoop ';'
          | asignacion ';'
          | sentencia sentencia
          ;

forLoop : 'for' '(' inicializacion ';' condicion ';' actualizacion ')' '{' sentencia* '}' ;

inicializacion : ID '=' expresion ;

condicion : ID operadorComparacion expresion ;

actualizacion : ID operadorAsignacion expresion ;

asignacion : ID '=' expresion ;

expresion : expresion ('*' | '/') expresion #MulDiv
          | expresion ('+' | '-') expresion #AddSub
          | INT                            #Int
          | ID                             #Variable
          | '(' expresion ')'              #Parens
          ;

operadorComparacion : '<' | '>' | '==' | '!=' | '<=' | '>=' ;

operadorAsignacion : '=' | '+=' | '-=' | '*=' | '/=' ;

ID : [a-zA-Z][a-zA-Z0-9]* ;
INT : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
COMENTARIO : '//' .*? '\n' -> skip ;
