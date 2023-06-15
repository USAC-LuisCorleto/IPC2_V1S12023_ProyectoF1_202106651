class Película:
    pelis_fav = []
    def __init__(self, nombre_categoria, titulo, director, año_pelicula, fecha_funcion, hora_funcion):
        self.nombre_categoria = nombre_categoria
        self.titulo = titulo
        self.director = director
        self.año_pelicula = año_pelicula
        self.fecha_funcion = fecha_funcion
        self.hora_funcion = hora_funcion

    def imprimir(self):
        print("----------------")
        print(f"Categoría: {self.nombre_categoria}")
        print(f"Título: {self.titulo}")
        print(f"Director: {self.director}")
        print(f"Año: {self.año_pelicula}")
        print(f"Fecha: {self.fecha_funcion}")
        print(f"Hora: {self.hora_funcion}")

    def imprimir_pelis(self):
        print("------------------------")
        print(f"Película: {self.titulo}")

    def imprimir_funciones(self):
        print("--------------------------------------------------------------------------")
        print(f"Película: {self.titulo} | Fecha de la función: {self.fecha_funcion} | Hora de la función: {self.hora_funcion}")