import os

libros= []
libros_prestados= []


def registrar():
    try:
        titulo= input("Ingrese el titulo: ")
        autor= input("Ingrese el autor: ")
        fecha_public= input("Ingrese el año de publicacion: ")
        sku= input("Ingrese las primeras 6 letras del nombre del libro, 3 primeras letras del autor y año de publicacion (sin espacios): ").lower()
        if titulo == "" or autor == "" or fecha_public == "":
            print("faltó algun dato por ingresar")
        else:
            libro= {
                'titulo': titulo,
                'autor' : autor,
                'fecha_public' : fecha_public,
                'sku': sku
            }
            libros.append(libro)
            print("Su libro se ha registardo exitosamente")

        
    except ValueError:
        print("Dato erroneo")

def prestar():
    nombre= input("Ingrese el nombre del usuario: ")
    titulo1= input("Ingrese el titulo del libro: ")
    fecha_prestamo= input("Ingrese la fecha del prestamo: ")
    sku= input("Ingrese las primeras 6 letras del nombre del libro, 3 primeras letras del autor y año de publicacion (sin espacios): ").lower()
    if not sku in libros:
        print("El libro no existe")
    elif sku in libros:
        print("eL libro ya fue prestado")
    else:
        libro_prestado= {
            'titulo1': titulo1,
            'nombre': nombre,
            'fecha_prestamo': fecha_prestamo
        }
        libros_prestados.append(libro_prestado)
    print("Puede llevarse el libro")
         
def listar():
    print("Titulo\t\tAutor\t\tAño de publicacion\t\tSKU")
    for libro in libros:
        print(f"{libro['titulo']}\t\t{libro['autor']}\t\t{libro['fecha_public']}\t\t{libro['sku']}")

def imprimir():
    with open ('prestamos.txt', 'w') as archivo:
        archivo.write("Usuario\t\t\tTitulo\t\t\tFecha del prestamo")
        for libro in libros_prestados:
            archivo.write(f"{libros_prestados['nombre']}\t\t\t{libros_prestados['titulo1']}\t\t\t{libros_prestados['fecha_prestamo']}\t\t\t")
    print("Su archivo se ha generado nexitosamente en ", os.getcwd())


def menu():
    while True:
        try:
            print("---------MENU---------")
            print("1. Registrar libro")
            print("2. Prestar libro")
            print("3. Listar todos los libros")
            print("4. Imprimir reporte de préstamos")
            print("5. Salir del Programa")

            op= int(input("Ingrese una opcion del menu: "))
            if op == 1:
                registrar()
            elif op == 2:
                prestar()
            elif op == 3:
                listar()
            elif op == 4:
                imprimir()
            elif op == 5:
                print("Programa finalizado\n Desarrollado por Luisa Espinoza\n RUN: 28.157.163-k")
                break
            else: 
                print("Opcion fuera de rango")
        
        except ValueError:
            print("Error dato invalido")