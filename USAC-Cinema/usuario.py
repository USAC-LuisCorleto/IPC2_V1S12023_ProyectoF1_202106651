class Usuario:
    def __init__(self, rol, nombre, apellido, telefono, correo, contraseña):
        self.rol = rol
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.contraseña = contraseña

    def imprimir(self):
        print(f"Rol: {self.rol}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")