import os
from datetime import datetime

def pedir_dato(texto):
    directorio_actual = os.getcwd()
    directorio_actual = directorio_actual + " > "
    dato=(input(directorio_actual + texto))
            
    return dato

def mostrar_menu():
    print("  GESTOR DE ARCHIVOS Y CARPETAS")
    print(f"Ruta actual: {os.getcwd()}")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información del archivo")
    print("7. Salir")

def listar_contenido():
    # Lista archivos y carpetas del directorio actual
    try:
        elementos = os.listdir(os.getcwd())
        if len(elementos) == 0:
            print("El directorio está vacío.")
            return
        print("\nContenido del directorio:")
        for elemento in sorted(elementos):
            if os.path.isdir(elemento):
                tipo = "[CARPETA]"
            else:
                tipo = "[ARCHIVO]"
            print(f"  {tipo} {elemento}")
    except PermissionError:
        print("Error: no tienes permisos para listar este directorio.")
    except OSError as e:
        print(f"Error al listar el contenido: {e}")
    

def crear_directorio():
    # Crea una nueva carpeta
    nombre = pedir_dato("Nombre del nuevo directorio: ")
    if nombre is None:
        return
    try:
        os.mkdir(nombre)
        print(f"Directorio '{nombre}' creado correctamente.")
    except FileExistsError:
        print(f"Error: ya existe un elemento llamado '{nombre}'.")
    except PermissionError:
        print("Error: no tienes permisos para crear el directorio aquí.")
    except FileNotFoundError:
        print("Error: la ruta indicada no es correcta.")
    except OSError as e:
        print(f"Error al crear el directorio: {e}")
    

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    nombre = pedir_dato("Nombre del nuevo archivo: ")
    if nombre is None:
        return
    if os.path.exists(nombre):
        print(f"Error: ya existe un elemento llamado '{nombre}'.")
        return
    contenido = pedir_dato("Contenido inicial: ")
    try:
        archivo = open(nombre, "w", encoding="utf-8")
        archivo.write(contenido + "\n")
        archivo.close()
        print(f"Archivo '{nombre}' creado correctamente.")
    except PermissionError:
        print("Error: no tienes permisos para crear el archivo aquí.")
    except FileNotFoundError:
        print("Error: la ruta indicada no es correcta.")
    except OSError as e:
        print(f"Error al crear el archivo: {e}")
    

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    nombre = pedir_dato("Nombre del archivo donde escribir: ")
    if nombre is None:
        return
    if not os.path.exists(nombre):
        print(f"Error: el archivo '{nombre}' no existe.")
        return
    if os.path.isdir(nombre):
        print(f"Error: '{nombre}' es una carpeta, no un archivo.")
        return
    texto = pedir_dato("Texto a añadir: ")
    try:
        archivo = open(nombre, "a", encoding="utf-8")
        archivo.write(texto + "\n")
        archivo.close()
        print("Texto añadido correctamente.")
    except PermissionError:
        print("Error: no tienes permisos para escribir en este archivo.")
    except OSError as e:
        print(f"Error al escribir en el archivo: {e}")



def eliminar_elemento():
    # Elimina un archivo o carpeta
    nombre = pedir_dato("Nombre del archivo o directorio a eliminar: ")
    if nombre is None:
        return
    if not os.path.exists(nombre):
        print(f"Error: '{nombre}' no existe.")
        return

    confirmacion = pedir_dato(f"¿Seguro que quieres eliminar '{nombre}'? (s/n): ").lower()
    if confirmacion != "s":
        print("Operación cancelada.")
        return
    try:
        if os.path.isdir(nombre):
            os.rmdir(nombre)
            print(f"Directorio '{nombre}' eliminado correctamente.")
        else:
            os.remove(nombre)
            print(f"Archivo '{nombre}' eliminado correctamente.")
    except PermissionError:
        print("Error: no tienes permisos para eliminar este elemento.")
    except OSError:
        print("Error: no se pudo eliminar. Si es una carpeta, debe estar vacía.")


def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    nombre = pedir_dato("Nombre del archivo o directorio: ")
    if nombre is None:
        return
    if not os.path.exists(nombre):
        print(f"Error: '{nombre}' no existe.")
        return
    try:
        if os.path.isdir(nombre):
            tipo = "Carpeta"
        else:
            tipo = "Archivo"
        tamano = os.path.getsize(nombre)
        fecha = datetime.fromtimestamp(os.path.getmtime(nombre))

        print(f"\nInformación de '{nombre}':")
        print(f"  Tipo: {tipo}")
        print(f"  Tamaño: {tamano} bytes")
        print(f"  Última modificación: {fecha.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"  Ruta completa: {os.path.abspath(nombre)}")
    except PermissionError:
        print("Error: no tienes permisos para ver la información.")
    except OSError as e:
        print(f"Error al obtener la información: {e}")
    

def main():
    # Bucle principal del programa
    dentro = True

    while dentro: 
        mostrar_menu()
        opcion_elegida=(int(pedir_dato("Indica una opción: ")))

        match(opcion_elegida):
                    case 1: listar_contenido()
                    case 2: crear_directorio ()
                    case 3: crear_archivo ()
                    case 4: escribir_en_archivo ()
                    case 5: eliminar_elemento ()
                    case 6: mostrar_informacion ()
                    case 7: dentro = False

    print ("Hasta pronto MariCarmen")
                

main()