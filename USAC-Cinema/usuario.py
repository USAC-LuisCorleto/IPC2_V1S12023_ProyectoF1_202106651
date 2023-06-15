class Usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contraseña):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contraseña = contraseña
        self.historialBoletos = []
        self.peliculasFavoritas = []

    def imprimir(self):
        print("------------------")
        print(f"Rol: {self.rol}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")

    def imprimir_pelis_favs(self):
        for pelicula in self.peliculasFavoritas:
            print(pelicula)