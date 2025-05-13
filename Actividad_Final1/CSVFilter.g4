grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | aggregateStat
    | sortStat
    | limitStat
    | joinStat
    | groupStat
    | printStat
    ;

loadStat: 'load' STRING ';' ;

filterStat
    : 'filter' 'column' STRING OPERATOR value (LOGICAL_OP filterStat)? ';' 
    | 'filter' 'column' STRING K_BETWEEN value K_AND value ';'
    | 'filter' 'column' STRING K_IN '(' valueList ')' ';'
    | 'filter' 'column' STRING K_LIKE STRING ';'
    ;

valueList: value (',' value)* ;

aggregateStat
    : 'aggregate' AGGR_FUNC 'column' STRING ';'
    | 'aggregate' AGGR_FUNC 'column' STRING K_WHERE STRING OPERATOR value ';'
    ;

sortStat: 'sort' 'by' STRING sortOrder ';' ;

sortOrder: 'asc' | 'desc' ;

limitStat: 'limit' INT ';' ;

joinStat: 'join' STRING 'on' STRING '=' STRING ';' ;

groupStat: 'group' 'by' STRING ';' ;

printStat: 'print' ';' ;

value: STRING | INT | FLOAT | BOOLEAN ;

// Palabras clave
K_BETWEEN: 'between' ;
K_AND: 'and' ;
K_IN: 'in' ;
K_LIKE: 'like' ;
K_WHERE: 'where' ;

// Funciones de agregación
AGGR_FUNC: 'count' | 'sum' | 'average' | 'min' | 'max' ;

BOOLEAN: 'true' | 'false' ;
FLOAT: [0-9]+ '.' [0-9]+ ;
LOGICAL_OP: 'AND' | 'OR' ;
OPERATOR: '>=' | '<=' | '>' | '<' | '==' | '!=' | 'contains' ;
STRING: '"' (~["\r\n])* '"' ;
INT: [0-9]+ ;

COMMENT: '//' ~[\r\n]* -> skip ;
WS: [ \t\r\n]+ -> skip ;