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
    | 'filter' 'column' STRING 'between' value 'and' value ';'
    | 'filter' 'column' STRING 'in' '(' valueList ')' ';'
    | 'filter' 'column' STRING 'like' STRING ';'
    ;

valueList: value (',' value)* ;

aggregateStat
    : 'aggregate' aggregateType 'column' STRING ';'
    | 'aggregate' aggregateType 'column' STRING 'where' filterCondition ';'
    ;

filterCondition: STRING OPERATOR value (LOGICAL_OP filterCondition)? ;

sortStat: 'sort' 'by' STRING sortOrder ';' ;

sortOrder: 'asc' | 'desc' ;

limitStat: 'limit' INT ';' ;

joinStat: 'join' STRING 'on' STRING '=' STRING ';' ;

groupStat: 'group' 'by' STRING ';' ;

printStat: 'print' ';' ;

aggregateType
    : 'count'
    | 'sum'
    | 'average'
    | 'min'
    | 'max'
    | 'between'
    ;

value: STRING | INT | FLOAT | BOOLEAN ;

BOOLEAN: 'true' | 'false' ;
FLOAT: [0-9]+ '.' [0-9]+ ;
LOGICAL_OP: 'AND' | 'OR' ;
OPERATOR: '>=' | '<=' | '>' | '<' | '==' | '!=' | 'contains' ;
STRING: '"' (~["\r\n])* '"' ;
INT: [0-9]+ ;

COMMENT: '//' ~[\r\n]* -> skip ;
WS: [ \t\r\n]+ -> skip ;