class Cliente:
    def __init__(self, nombre, apellido, telefono, gmail):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.gmail = gmail

    def solicitar_turno(self):
        print(f"{self.nombre} {self.apellido} solicitó un turno")

    def recibir_diagnostico(self, diagnostico):
        mensaje = f"Cliente {self.nombre} {self.apellido} recibió el diagnóstico: {diagnostico}"
        print(mensaje)
        return mensaje


# Se dejan dos líneas vacías entre clases
class Vehiculo:
    def __init__(self, patente, marca):
        self.patente = patente
        self.marca = marca

    def mostrar_info(self):
        print(f"Patente: {self.patente}, Marca: {self.marca}")


class Auto(Vehiculo):
    def __init__(self, patente, marca, puertas):
        super().__init__(patente, marca)
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Puertas: {self.puertas}")


class Moto(Vehiculo):
    def __init__(self, patente, marca, cilindrada):
        super().__init__(patente, marca)
        self.cilindrada = cilindrada
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f"Cilindrada: {self.cilindrada}")


# Bloque de ejecución (al final)
print("--- DATOS DEL CLIENTE ---")
cliente1 = Cliente("Priscila", "Toledano", "2991234567", "priscila@gmail.com")
cliente1.recibir_diagnostico("El auto tiene fallos en los frenos")

print("\n--- DATOS DE LOS VEHÍCULOS ---")
auto1 = Auto("ABC123", "Toyota", 4)
moto1 = Moto("XYZ789", "Honda", "150cc")
auto1.mostrar_info()
print("-----")
moto1.mostrar_info()

