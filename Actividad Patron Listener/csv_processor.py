import csv
import json
from collections import Counter

class CSVProcessor:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.rows = []
        self.header = []
        self.emptyFieldCount = 0

    def cargar_datos(self):
        with open(self.archivo_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.header = reader.fieldnames
            for fila in reader:
                self.rows.append(fila)
                self.emptyFieldCount += sum(1 for valor in fila.values() if valor.strip() == "")

    def limpiar_montos(self):
        for fila in self.rows:
            if "Cantidad" in fila:
                fila["Cantidad"] = fila["Cantidad"].replace('$', '').replace(',', '').replace('"', '').strip()

    def contar_meses(self):
        meses = [fila["Fecha"].split("-")[1] for fila in self.rows if "Fecha" in fila and fila["Fecha"]]
        conteo = Counter(meses)
        print("Conteo de meses:", conteo)

    def detectar_repetidas(self):
        vistas = set()
        for fila in self.rows:
            clave = tuple(fila.items())
            if clave in vistas:
                print("Fila repetida:", fila)
            else:
                vistas.add(clave)

    def validar_cantidad(self):
        for i, fila in enumerate(self.rows):
            valor = fila.get("Cantidad", "").replace('$','').replace(',','').strip()
            if not valor.replace('.', '', 1).isdigit():
                print(f"[!] Cantidad inválida en fila {i + 1}: {valor}")

    def exportar_json(self, filename="output.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.rows, f, indent=2, ensure_ascii=False)

    def mostrar_estadisticas(self):
        print(f"\nTotal de campos vacíos: {self.emptyFieldCount}")
        self.contar_meses()

# ----------- USO -------------
if __name__ == "__main__":
    processor = CSVProcessor("data.csv")  # Cambia si tu archivo se llama diferente
    processor.cargar_datos()
    processor.limpiar_montos()
    processor.detectar_repetidas()
    processor.validar_cantidad()
    processor.mostrar_estadisticas()
    processor.exportar_json("limpio.json")
