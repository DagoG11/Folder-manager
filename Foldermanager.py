import os
import shutil
from abc import ABC  # Se utiliza el módulo `abc` para definir clases abstractas

class FolderManager:  #Clase base para gestionar carpetas: crear, listar y eliminar.
   

    def __init__(self, base_path):  # Se define el constructor de la clase

        self.base_path = base_path  # Guarda la ruta base

        # Crea la ruta base si no existe
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
            print(f"Ruta base creada: {self.base_path}")
        else:
            print(f"Ruta base lista: {self.base_path}")

    def create_folder(self, folder_name):  # Crea una nueva carpeta dentro de la ruta base
                                            # folder_name: nombre de la carpeta a crear

        folder_path = os.path.join(self.base_path, folder_name)
        try:
            os.makedirs(folder_path)
            print(f"Carpeta '{folder_name}' creada exitosamente.")
        except FileExistsError:
            print(f"La carpeta '{folder_name}' ya existe.")
        except Exception as e:
            print(f"Error al crear la carpeta: {e}")

    def list_folders(self):   # Lista todas las carpetas dentro de la ruta base.

        try:
            folders = [d for d in os.listdir(self.base_path) 
                       if os.path.isdir(os.path.join(self.base_path, d))]
            print("Carpetas encontradas:")
            for folder in folders:
                print(f"- {folder}")
            return folders
        except Exception as e:
            print(f"Error al listar las carpetas: {e}")
            return []

    def delete_folder(self, folder_name): # Elimina una carpeta y todo su contenido dentro de la ruta base

        folder_path = os.path.join(self.base_path, folder_name)
        try:
            shutil.rmtree(folder_path)
            print(f"Carpeta '{folder_name}' eliminada exitosamente.")
        except FileNotFoundError:
            print(f"La carpeta '{folder_name}' no existe.")
        except Exception as e:
            print(f"Error al eliminar la carpeta: {e}")


class FileOrganizer(FolderManager, ABC):  # Clase abstracta para organizar archivos por extensión. Hereda de FolderManager.

    def __init__(self, base_path, extension):  # Constructor que recibe la ruta base y la extensión de archivo a organizar

        super().__init__(base_path)
        self.extension = extension

    def organize(self): # Organiza los archivos en la carpeta base según la extensión especificada  
    
        try:
            files = [f for f in os.listdir(self.base_path) 
                     if os.path.isfile(os.path.join(self.base_path, f)) and f.endswith(self.extension)]

            if not files:
                print(f"No se encontraron archivos con la extensión '{self.extension}'.")
                return

            folder_name = self.extension.lstrip('.').upper() + "_Files"
            self.create_folder(folder_name)
            folder_path = os.path.join(self.base_path, folder_name)

            for file in files:
                src = os.path.join(self.base_path, file)
                dst = os.path.join(folder_path, file)
                shutil.move(src, dst)
                print(f"Movido: {file} -> {folder_name}/")

            print(f"Organización completa. Archivos movidos a '{folder_name}'.")
        except Exception as e:
            print(f"Error al organizar los archivos: {e}")


# Clases especializadas con extensiones predeterminadas

class WordOrganizer(FileOrganizer): # FileOrganizer hereda de FolderManager donde obtiene los métodos para gestionar carpetas
    def __init__(self, base_path):
        super().__init__(base_path, ".docx")


class TextOrganizer(FileOrganizer):  # Se coloca FileOrganizer para evitar duplicar código
    def __init__(self, base_path):
        super().__init__(base_path, ".txt")


class PDFOrganizer(FileOrganizer): # Word, Text, , Excel heredan de FileOrganizer y indirectamente de FolderManager
    def __init__(self, base_path):
        super().__init__(base_path, ".pdf")


class ExcelOrganizer(FileOrganizer):
    def __init__(self, base_path):
        super().__init__(base_path, ".xlsx") # se usap polimorfismo para llamar el mismo metodo con diferentes comportamientos

if __name__ == "__main__":  # Pruebas de las clases y métodos definidos arriba
    base = r"C:\Users\Dagoberto\Desktop\Foldermanager"

    # Archivos de prueba
    test_files = [
        "prueba.docx",
        "ejemplo.pdf",
        "notas.txt",
        "datos.xlsx"
    ]

    print("🔎 Iniciando verificación de archivos...")

    # Crear archivos vacíos de prueba si no existen
    for file in test_files:
        path = os.path.join(base, file)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(f"Este es un archivo de prueba: {file}")
            print(f"✅ Archivo de prueba creado: {file}")
        else:   
            print(f"⚠️ El archivo ya existe: {file}")


    # Ejecutar los organizadores
    organizers = [
        WordOrganizer(base),
        TextOrganizer(base),
        PDFOrganizer(base),
        ExcelOrganizer(base)
    ]

    for org in organizers:
        print(f"➡ Organizando archivos con {org.__class__.__name__}...")
        org.organize()

    print("🎉 Proceso finalizado.")