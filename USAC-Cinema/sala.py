class Sala:
    def __init__(self, numero_sala, capacidad):
        self.nombre_cine = "Cinepolis"
        self.numero_sala = numero_sala
        self.capacidad = capacidad

    def imprimir(self):
        print("---------------")
        print(f"Cine: {self.nombre_cine}")
        print(f"Número de sala: {self.numero_sala}")
        print(f"Capacidad: {self.capacidad}")

    def imprimir_sala(self):
        print("-------------------------------------------------------------")
        print(f"Número de sala: {self.numero_sala} Asientos: {self.capacidad}")
