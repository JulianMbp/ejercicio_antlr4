load "empleados.csv";
filter column "edad" > 25;
aggregate count column "id";
aggregate average column "salario";
aggregate sum column "dias_laborados";
print;