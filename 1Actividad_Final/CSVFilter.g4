grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | printStat
    ;

loadStat: 'load' STRING ';' ;
filterStat: 'filter' expr ';' ;
printStat: 'print' ';' ;

expr
    : expr AND expr
    | expr OR expr
    | '(' expr ')'
    | 'column' STRING OPERATOR INT
    ;

AND: 'AND';
OR: 'OR';
OPERATOR: '>' | '<' | '==' | '!=' | '>=' | '<=' ;

STRING: '"' (~["\r\n])* '"' ;
INT: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;
