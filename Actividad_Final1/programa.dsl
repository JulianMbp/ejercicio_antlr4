load "eventos.csv";
filter column "costo_entrada" > 100000;
filter column "tipo_evento" == "Concierto";
aggregate count column "id_evento";
aggregate average column "cantidad_asistentes";
aggregate sum column "costo_entrada";
print;