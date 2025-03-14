grammar MiGramatica;

// Regla principal: una secuencia de expresiones separadas por punto y coma.
programa: (expresion ';')+ ;

// Reglas de expresiones con prioridades para operaciones aritméticas.
expresion
    : ID '=' expresion                   # Assign   // Asignación de variables
    | expresion op=('*'|'/') expresion   # MulDiv    // Multiplicación y división
    | expresion op=('+'|'-') expresion   # AddSub    // Suma y resta
    | INT                                # Int       // Entero
    | ID                                 # Variable  // Identificador (variable)
    | '(' expresion ')'                  # Parens    // Uso de paréntesis para agrupar
    ;

// Reglas léxicas:
// Identificador: inicia con letra o guión bajo, seguido de letras, dígitos o guiones bajos.
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;

// Número entero: secuencia de dígitos.
INT : [0-9]+ ;

// Espacios en blanco: se omiten (skip).
WS  : [ \t\r\n]+ -> skip ;
