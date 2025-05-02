load "empleados.csv";
filter column "edad" > 30;
filter column "salario" >= 1000;
filter colimn "dias_laborados" == 14;
print;