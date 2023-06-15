from usuario import Usuario
from lista_enlazada import ListaEnlazadaSimple
from pelicula import Película
from listad_enlazadac import ListaEnlazadaCircularDoble
from sala import Sala
from listad_enlazada import ListaEnlazadaDoble

admin = "202106651"
contraseña = "3082203580607"
ListaSimple = ListaEnlazadaSimple()
ListaDobleCircular = ListaEnlazadaCircularDoble()
ListaDoble = ListaEnlazadaDoble()
incremento = 0
pels_favoritas = []

#Método para el menú
def mostrar_menu():
    print("--------------------------------")
    print("--BIENVENIDO AL MENÚ DE CINEMA--")
    print("Elija una opción")
    print("[1]. Iniciar sesión.")
    print("[2]. Registrarse.")
    print("[3]. Ver listado de películas.")

opcion_valida = False

while True:
    while not opcion_valida:
        mostrar_menu()
        opcion = input()

        #Selección de la opción "Iniciar sesión"
        if opcion=="1":
            print("--------------------------------------------------")
            print("--USTED SE ENCUENTRA EN LA OPCiÓN INICIAR SESIÓN--")
            opcion_valida = True
            print("Ingrese los datos correspondientes")
            print("Usuario: ")
            usuarioIniciarSesion = input()
            print("Contraseña: ")
            contraseñaIniciarSesion = input()

            #Condicional para identificar que es el administrador
            if contraseñaIniciarSesion==contraseña and usuarioIniciarSesion==admin:
                while True:
                    print("---------------------------------------")
                    print("--BIENVENIDO AL MENÚ DE ADMINISTRADOR--")
                    print("Elija una opción")
                    print("[1]. Gestionar usuarios")
                    print("[2]. Gestionar Categorías y películas")
                    print("[3]. Gestionar salas.")
                    print("[4]. Cerrar sesión.")
                    opcion_menuAdmin = input()

                    #Selección de la opción gestionar usuarios
                    if opcion_menuAdmin == "1":
                        while True:
                            print("-----------------------------------------------------")
                            print("Usted se encuentra en la opción 'Gestionar usuarios'.")
                            print("Elija una opción")
                            print("[1]. Editar usuario.")
                            print("[2]. Crear usuario.")
                            print("[3]. Eliminar usuario.")
                            print("[4]. Cargar usuario.")
                            print("[5]. Regresar.")
                            opcion_gestionUsuario = input()

                            #Selección de la opción "Editar usuario"
                            if opcion_gestionUsuario == "1":
                                print("----------------------------")
                                print("Usted va a editar un usuario")
                                print("Ingrese el correo: ")
                                correoEdit = input()
                                print("Ingrese la contraseña: ")
                                contraseñaEdit = input()
                                ListaSimple.editar_usuario(correoEdit, contraseñaEdit)

                            #Selección de la opción "Crear usuario"
                            elif opcion_gestionUsuario == "2":
                                print("---------------------------")
                                print("Usted va a crear un usuario")
                                Rol="Cliente"
                                print("Ingrese su nombre: ")
                                nombre_usuario = input()
                                print("Ingrese su apellido: ")
                                apellido_usuario = input()
                                print("Ingrese su teléfono: ")
                                teléfono_usuario = input()
                                print("Ingrese su correo: ")
                                correo_usuario = input()
                                print("Ingrese una contraseña: ")
                                contraseña_usuario = input()
                                usuario = Usuario(Rol, nombre_usuario, apellido_usuario, teléfono_usuario, correo_usuario, contraseña_usuario)
                                ListaSimple.add(usuario)
                                print("Usuario agregado exitosamaente.")
                                ListaSimple.generar_archivo_XML()
                            
                            #Selección de la opción "Eliminar usuario"
                            elif opcion_gestionUsuario == "3":
                                print("------------------------------")
                                print("Usted va a eliminar un usuario")
                                print("Ingrese el correo: ")
                                correoElim = input()
                                print("Ingrese la contraseña: ")
                                contraseñaElim = input()
                                ListaSimple.eliminar_usuario(correoElim, contraseñaElim)
                            
                            #Selección de la opción "Cargar usuario"
                            elif opcion_gestionUsuario == "4":
                                print("--------------------------------------------------------------------------")
                                print("Usted va a cargar un usuario o usuarios por medio de un archivo XML.")
                                print("Ingrese el nombre del archivo XML tal y como está en su lista de archivos.")
                                nombre_archivo = input()
                                ListaSimple.cargar_xml(nombre_archivo)
                            
                            #Selección de la opción "Regresar al menú administrador"
                            elif opcion_gestionUsuario == "5":
                                print("-----------------------------------")
                                print("Regresando al menú administrador...")
                                break

                    #Selección de la opción "Gestión de Categorías y películas"
                    elif opcion_menuAdmin == "2":
                        while True:
                            print("-----------------------------------------------------")
                            print("Usted se encuentra en la opción 'Gestionar Categorías y Películas'.")
                            print("Elija una opción")
                            print("[1]. Editar Categorías y Películas.")
                            print("[2]. Crear Categorías y Películas.")
                            print("[3]. Eliminar Categorías y Películas.")
                            print("[4]. Cargar Categorías y Películas.")
                            print("[5]. Regresar.")
                            opcion_gestionPeliculas = input()

                            #Selección Editar categorías
                            if opcion_gestionPeliculas == "1":
                                ListaDobleCircular.editar_categorias_peliculas()

                            #Selección Crear categorías y películas    
                            if opcion_gestionPeliculas == "2":
                                print("---------------------------------------")
                                print("Usted va a crear Categorías y Películas")
                                print("Ingrese el nombre de la categoría ya existente o cree una nueva: ")
                                nombre_cat = input()
                                print("Ingrese el título de la película: ")
                                titulo_pel = input()
                                print("Ingrese el nombre del director de la película: ")
                                nombre_director = input()
                                print("Ingrese el año en el que fue lanzada la película: ")
                                año_pelicula = input()
                                print("Ingrese la fecha de la función: ")
                                fecha_func = input()
                                print("Ingrese la hora de la función: ")
                                hora_func = input()
                                pelicula = Película(nombre_cat, titulo_pel, nombre_director, año_pelicula, fecha_func, hora_func)
                                ListaDobleCircular.add(pelicula)
                                ListaDobleCircular.guardar_en_xml()
                                print("--------------------------------------------")
                                print("Categoría y Películas añadidas correctamente")
                                ListaDobleCircular.Imprimir()
                                
                            #Selección Eliminar categorías y películas
                            if opcion_gestionPeliculas == "3":
                                print("--------------------------------------------")
                                print("Usted va a eliminar una Categoría o Película")
                                cat_elim = input("Ingrese el nombre de la categoría a eliminar: ")
                                pel_elim = input("Ingrese el nombre de la película a eliminar: ")
                                ListaDobleCircular.eliminar_pelicula(cat_elim, pel_elim)

                            #Selección Cargar o leer categorías y películas
                            if opcion_gestionPeliculas == "4":
                                print("---------------------------------------------------------------------")
                                print("Usted va a cargar categorías y películas por medio de un archivo XML.")
                                print("Ingrese el nombre del archivo XML tal y como está en su lista de archivos.")
                                nombre_archivoCatPel = input()
                                ListaDobleCircular.cargar_xml(nombre_archivoCatPel)
                            
                            if opcion_gestionPeliculas == "5":
                                print("-------------------------------")
                                print("Regresando al menú principal...")
                                break

                    #Selección de la opción "Gestión de Salas"
                    elif opcion_menuAdmin == "3":
                        while True:
                            print("------------------------------------------------")
                            print("Usted se encuentra en la opción Gestión de salas")
                            print("[1]. Editar Salas.")
                            print("[2]. Crear Salas.")
                            print("[3]. Eliminar Salas.")
                            print("[4]. Cargar Salas.")
                            print("[5]. Regresar.")
                            opcion_gestionSalas = input()
                            
                            #Selección Editar Salas
                            if opcion_gestionSalas == "1":
                                print("--------------------------")
                                print("Usted va a editar una sala")
                                sala_edit = input("Ingrese el número de la sala a editar: ")
                                nuevos_asientos = input("Ingrese el número de asientos: ")
                                ListaDoble.editar_salas(sala_edit, nuevos_asientos)
                                print("--------------------------")
                                print("Sala editada correctamente")

                            #Selección Crear Salas
                            if opcion_gestionSalas == "2":
                                incremento+=1
                                print("-------------------------")
                                print("Usted va a crear una sala")
                                no_sala = f"#USACIPC2_202106651_{incremento}"
                                print("Ingrese el número de asientos disponibles en la sala: ")
                                asientos = input()

                                sala = Sala(no_sala, asientos)
                                ListaDoble.add(sala)
                                print("Sala agregada correctamente")
                                ListaDoble.Imprimir()
                                ListaDoble.guardar_en_xml()

                            #Selección Eliminar Salas.
                            if opcion_gestionSalas == "3":
                                print("----------------------------")
                                print("Usted va a eliminar una sala")
                                sala_elim = input("Ingrese el número de la sala a eliminar: ")
                                ListaDoble.eliminar_sala(sala_elim)
                                print("----------------------------")
                                print("Sala eliminada correctamente")

                            #Selección Cargar o Leer XML
                            if opcion_gestionSalas == "4":
                                print("----------------------------------------------------")
                                print("Usted va a cargar Salas por medio de un archivo XML.")
                                nombre_archivoSalas = input("Ingrese el nombre del archivo XML tal y como está en su lista de archivos: ")
                                ListaDoble.cargar_xml(nombre_archivoSalas)

                            if opcion_gestionSalas == "5":
                                print("-------------")
                                print("Regresando...")
                                break

                    #Selección de la opción "Cerrar sesión"
                    elif opcion_menuAdmin == "4":
                        print("------------------")
                        print("Cerrando sesión...")
                        break
            
            #Función que retorna el usuario ingresado si lo encuentra en alguno de los nodos de la lista.
            usuario_encontrado = ListaSimple.buscar_usuario(usuarioIniciarSesion, contraseñaIniciarSesion)
            if usuario_encontrado is not None:
                while True:
                    print("---------------------------------")
                    print("--BIENVENIDO AL MENÚ DE USUARIO--")
                    print("Elija una opción")
                    print("[1]. Ver listado de películas.")
                    print("[2]. Listado de películas favoritas.")
                    print("[3]. Comprar boletos.")
                    print("[4]. Historial de boletos comprados.")
                    print("[5]. Cerrar sesión.")
                    opcion_menUsuario = input()

                    if opcion_menUsuario == "1":
                        print("---------------------------------")
                        print("Listado de pelícuals disponibles:")
                        ListaDobleCircular.Imprimir()

                    if opcion_menUsuario == "2":
                        while True:
                            print("-------------------------------")
                            print("Elija una opción: ")
                            print("[1]. Agregar película a favoritos.")
                            print("[2]. Ver listado de favoritos.")
                            print("[3]. Regresar.")
                            opcion_pelisFavs = input()

                            if opcion_pelisFavs == "1":
                                print("-----------------------------------------")
                                print("Películas que puede agregar a favoritos: ")
                                ListaDobleCircular.Imprimir_pelis()
                                print("----------------------------------")
                                pelicula_fav_agregar = input("Ingresa el nombre de la película: ")
                                
                                nodo_actual = ListaDobleCircular.cabeza
                                pelicula_encontrada = False

                                while True:
                                    if nodo_actual.dato.titulo == pelicula_fav_agregar:
                                        pelicula_encontrada = True
                                        break

                                    nodo_actual = nodo_actual.siguiente

                                    if nodo_actual == ListaDobleCircular.cabeza:
                                        break
                                if pelicula_encontrada:
                                    usuario_encontrado.peliculasFavoritas.append(pelicula_fav_agregar)
                                    print("--------------------------------------------")
                                    print("Película agregada a favoritos correctamente.")
                                else:
                                    print("----------------------")
                                    print("La película no existe.")

                            if opcion_pelisFavs == "2":
                                print("---------------------")
                                print("Películas favoritas: ")
                                if len(usuario_encontrado.peliculasFavoritas) == 0:
                                    print("---------------------------------------------------")
                                    print("No tiene películas favoritas agregadas actualmente.")
                                else:
                                    usuario_encontrado.imprimir_pelis_favs()

                            if opcion_pelisFavs == "3":
                                print("-------------")
                                print("Regresando...")
                                break
                    
                    if opcion_menUsuario == "3":
                        print("----------------------------------------------")
                        print("Usted va a comprar un boleto para una función.")
                        ListaDobleCircular.Imprimir_funciones_compra()
                        print("-------------------------------------------")
                        funcion_compra = input("Seleccione la función a la que desea asistir: ")
                        fechaFuncion_compra = input("Seleccione la fecha de la función a la que desea asistir: ")
                        horaFuncion_compra = input("Seleccione la hora a la que desea asistir: ")

                        nodo_actual = ListaDobleCircular.cabeza

                        pelicula_encontrada = False
                        fecha_encontrada = False
                        hora_encontrada = False

                        while nodo_actual is not None:
                            if nodo_actual.dato.titulo == funcion_compra and nodo_actual.dato.fecha_funcion == fechaFuncion_compra and nodo_actual.dato.hora_funcion == horaFuncion_compra:
                                pelicula_encontrada = True
                                break

                            nodo_actual = nodo_actual.siguiente

                            if nodo_actual == ListaDobleCircular.cabeza:
                                break

                        if pelicula_encontrada:
                            print("------------------------------------")
                            print("Salas disponibles: ")
                            ListaDoble.Imprimir_sala()
                            print("-------------------------------------------------------")
                            sala_seleccion = input("Ingrese el nombre de la sala en donde verá la función: ")
                            sala_encotrada = ListaDoble.obtener_sala_encontrada(sala_seleccion)
                            print("----------------------")
                            print("Asientos disponibles: ")
                            sala_encotrada.imprimir_asientos()
                            print("----------------------------------------------------------------")
                            asiento_selección = input("Seleccione un asiento dentro del rango de capacidad disponible: ")
                            asiento_selección = int(asiento_selección)
                            if 1 <= asiento_selección <= int(sala_encotrada.capacidad):
                                print("--------------------------------")
                                print("¿Desea agregar su número de NIT?")
                                print("[1]. Sí.")
                                print("[2]. No.")
                                opcin_NIT = input()

                                if opcin_NIT == "1":
                                    print("-------------------------")
                                    nit = input("Ingrese su número de NIT: ")
                                    direccion = input("Ingrese su dirección: ")
                                    boletos = input("Ingrese la cantidad de boletos: ")
                                    total = int(boletos*35)
                                    usuario_encontrado.historialBoletos.append({
                                    'Nombre': usuario_encontrado.nombre,
                                    'Apellido': usuario_encontrado.apellido,
                                    'Teléfono': usuario_encontrado.telefono,
                                    'Correo': usuario_encontrado.correo, 
                                    'Fecha': fechaFuncion_compra, 
                                    'Hora': horaFuncion_compra, 
                                    'Sala': sala_seleccion,
                                    'Asiento': str(asiento_selección), 
                                    'Boletos': boletos, 
                                    'Total': str(total), 
                                    'NIT': nit, 
                                    'Dirección': direccion, 
                                    })
                                    print("------------------------------")
                                    print("Compra realizada éxitosamente.")
                                
                                if opcin_NIT == "2":
                                    nit = "C/F"
                                    direccion = input("Ingrese su dirección: ")
                                    boletos = input("Ingrese la cantidad de boletos: ")
                                    total = boletos*35
                                    usuario_encontrado.historialBoletos.append({
                                    'Nombre': usuario_encontrado.nombre + "\n",
                                    'Apellido': usuario_encontrado.apellido + "\n",
                                    'Teléfono': usuario_encontrado.telefono + "\n",
                                    'Correo': usuario_encontrado.correo + "\n",
                                    'Función': funcion_compra + "\n",
                                    'Fecha': fechaFuncion_compra + "\n",
                                    'Hora': horaFuncion_compra + "\n",
                                    'Sala': sala_seleccion + "\n",
                                    'Asiento': str(asiento_selección) + "\n",
                                    'Boletos': boletos + "\n",
                                    'Total': str(total) + "\n",
                                    'NIT': nit + "\n",
                                    'Dirección': direccion + "\n"
                                    })
                                    print("------------------------------")
                                    print("Compra realizada éxitosamente.")
                            else:
                                print("El asiento seleccionado se encuentra fuera del rango de capacidad.")
                                break

                        else:
                            print("--------------------------------------------")
                            print("Algún dato no coincide, vuelva a intentarlo.")
                            break

                    if opcion_menUsuario == "4":
                        print("--------------------------------")
                        print("Historial de boletos comprados: ")
                        usuario_encontrado.imprimir_historia()
                        

                    if opcion_menUsuario == "5":
                        print("------------------")
                        print("Cerrando sesión...")
                        break

            #Si el usuario no fue encontrado simplemente sale de la condición y debe volver a intentarlo.
            else:
                print("-----------------------------------------")
                print("--SU USUARIO NO SE ENCUENTRA REGISTRADO--")
                print("Regresando al menú principal...")
                break
        
        #Selección de la opción "Registrarse"
        elif opcion=="2":
            while  True:
                opcion_valida = True
                Rol = "Cliente"
                print("-----------------------------------------------")
                print("--USTED SE ENCUENTRA EN LA OPCIÓN REGISTRARSE--")
                print("Ingrese su nombre: ")
                nombre_usuario = input()
                print("Ingrese su apellido: ")
                apellido_usuario = input()
                print("Ingrese su teléfono: ")
                teléfono_usuario = input()
                print("Ingrese su correo: ")
                correo_usuario = input()
                print("Ingrese una contraseña: ")
                contraseña_usuario = input()
                usuario = Usuario(Rol, nombre_usuario, apellido_usuario, teléfono_usuario, correo_usuario, contraseña_usuario)
                ListaSimple.add(usuario)
                print("Usuario registrado correctamente.")
                ListaSimple.Imprimir()

                print("------------------------------")
                print("¿Desea registrar otro usuario?")
                print("[1]. Sí")
                print("[2]. No")
                reg = input()
                if reg == "2":
                    ListaSimple.generar_archivo_XML()
                    break
                elif reg == "1":
                    continue
        
        #Selección ver listado de películas
        elif opcion=="3":
            print("--USTED SE ENCUENTRA EN LA OPCIÓN VER LISTADO DE PELÍCULAS--")
            ListaDobleCircular.Imprimir()
            opcion_valida = True

        else:
            print("Opción inválida, vuelva a intentarlo.")
            mostrar_menu()
            opcion = input()
    opcion_valida=False