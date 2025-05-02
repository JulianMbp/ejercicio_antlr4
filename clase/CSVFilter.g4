grammar CSVFilter;

prog: stat+ ;

stat
    : loadStat
    | filterStat
    | printStat
    ;

loadStat:   'load' STRING ';' ;
filterStat: 'filter' 'column' STRING OPERATOR NUMBER ';' ;
printStat:  'print' ';' ;

OPERATOR: '>' | '<' | '>=' | '<=' | '==' | '!=' ;
STRING: '"' (~["\r\n])* '"' ;
NUMBER: [0-9]+ ('.' [0-9]+)? ;

WS: [ \t\r\n]+ -> skip ;