
import os      # Provee funciones para interactuar con el sistema operativo 
import shutil  # Proporciona utilidades para copiar, mover y eliminar archivos y carpetas.

class FolderManager:
    """
    Clase base para gestionar carpetas: crear, listar y borrar.
    """

    def __init__(self, base_path):
        """
        Constructor que recibe la ruta base donde se trabajarán las carpetas.
        
        Args:
            base_path (str): Ruta base para crear, listar y borrar carpetas.
        """
        self.base_path = base_path

        # Si la ruta base no existe, la creamos
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
            print(f"Se creó la ruta base: {self.base_path}")
        else:
            print(f"Ruta base lista: {self.base_path}")

    def create_folder(self, folder_name):
        """
        Crea una carpeta dentro de la ruta base.
        
        Args:
            folder_name (str): Nombre de la carpeta a crear.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        try:
            os.makedirs(folder_path)  # Crear carpeta (y subcarpetas si hace falta).
            print(f"Se creó la carpeta '{folder_name}' correctamente.")
        except FileExistsError:
            print(f"La carpeta '{folder_name}' ya existe.")
        except Exception as e:
            print(f"Error al crear la carpeta: {e}")

    def list_folders(self):
        """
        Lista todas las carpetas dentro de la ruta base.
        
        Returns:
            list: Lista de carpetas dentro de la ruta base.
        """
        try:
            folders = [d for d in os.listdir(self.base_path) 
                       if os.path.isdir(os.path.join(self.base_path, d))]
            print("Carpetas encontradas:")
            for folder in folders:
                print(f"- {folder}")
            return folders
        except Exception as e:
            print(f"Error al listar carpetas: {e}")
            return []

    def delete_folder(self, folder_name):
        """
        Borra la carpeta especificada y todo su contenido dentro de la ruta base.
        
        Args:
            folder_name (str): Nombre de la carpeta a borrar.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        try:
            shutil.rmtree(folder_path)  # Eliminar carpeta con todo el contenido.
            print(f"Se eliminó la carpeta '{folder_name}' correctamente.")
        except FileNotFoundError:
            print(f"La carpeta '{folder_name}' no existe.")
        except Exception as e:
            print(f"Error al borrar la carpeta: {e}")

class WordOrganizer(FolderManager):
    """
    Clase que hereda de FolderManager para gestionar carpetas específicas de documentos Word.
    """

    def __init__(self, base_path):
        """
        Constructor que llama al constructor de la clase padre.
        
        Args:
            base_path (str): Ruta base para gestionar documentos Word.
        """
        super().__init__(base_path)

    def organize_by_extension(self, extension):
        """
        Organiza archivos en la carpeta base según su extensión.
        
        Args:
            extension (str): Extensión de archivo para organizar (e.g., '.docx').
        """
        try:
            files = [f for f in os.listdir(self.base_path) 
                     if os.path.isfile(os.path.join(self.base_path, f)) and f.endswith(extension)]
            if not files:
                print(f"No se encontraron archivos con la extensión '{extension}'.")
                return

            folder_name = extension.lstrip('.').upper() + "_Files"
            self.create_folder(folder_name)
            folder_path = os.path.join(self.base_path, folder_name)

            for file in files:
                src = os.path.join(self.base_path, file)
                dst = os.path.join(folder_path, file)
                shutil.move(src, dst)  # Mover archivo a la nueva carpeta.
                print(f"Movido: {file} -> {folder_name}/")

            print(f"Organización completa. Archivos movidos a '{folder_name}'.")
        except Exception as e:
            print(f"Error al organizar archivos: {e}")

class TextOrganizer(FolderManager):
    """
    Clase que hereda de FolderManager para gestionar carpetas específicas de documentos de texto.
    """

    def __init__(self, base_path):
        """
        Constructor que llama al constructor de la clase padre.
        
        Args:
            base_path (str): Ruta base para gestionar documentos de texto.
        """
        super().__init__(base_path)

    def organize_by_extension(self, extension):
        """
        Organiza archivos en la carpeta base según su extensión.
        
        Args:
            extension (str): Extensión de archivo para organizar (e.g., '.txt').
        """
        try:
            files = [f for f in os.listdir(self.base_path) 
                     if os.path.isfile(os.path.join(self.base_path, f)) and f.endswith(extension)]
            if not files:
                print(f"No se encontraron archivos con la extensión '{extension}'.")
                return

            folder_name = extension.lstrip('.').upper() + "_Files"
            self.create_folder(folder_name)
            folder_path = os.path.join(self.base_path, folder_name)

            for file in files:
                src = os.path.join(self.base_path, file)
                dst = os.path.join(folder_path, file)
                shutil.move(src, dst)  # Mover archivo a la nueva carpeta.
                print(f"Movido: {file} -> {folder_name}/")

            print(f"Organización completa. Archivos movidos a '{folder_name}'.")
        except Exception as e:
            print(f"Error al organizar archivos: {e}")

class PDFOrganizer(FolderManager):
    """
    Clase que hereda de FolderManager para gestionar carpetas específicas de documentos PDF.
    """

    def __init__(self, base_path):
        """
        Constructor que llama al constructor de la clase padre.
        
        Args:
            base_path (str): Ruta base para gestionar documentos PDF.
        """
        super().__init__(base_path)

    def organize_by_extension(self, extension):
        """
        Organiza archivos en la carpeta base según su extensión.
        
        Args:
            extension (str): Extensión de archivo para organizar (e.g., '.pdf').
        """
        try:
            files = [f for f in os.listdir(self.base_path) 
                     if os.path.isfile(os.path.join(self.base_path, f)) and f.endswith(extension)]
            if not files:
                print(f"No se encontraron archivos con la extensión '{extension}'.")
                return

            folder_name = extension.lstrip('.').upper() + "_Files"
            self.create_folder(folder_name)
            folder_path = os.path.join(self.base_path, folder_name)

            for file in files:
                src = os.path.join(self.base_path, file)
                dst = os.path.join(folder_path, file)
                shutil.move(src, dst)  # Mover archivo a la nueva carpeta.
                print(f"Movido: {file} -> {folder_name}/")

            print(f"Organización completa. Archivos movidos a '{folder_name}'.")
        except Exception as e:
            print(f"Error al organizar archivos: {e}")

class ExcelOrganizer(FolderManager):
    """
    Clase que hereda de FolderManager para gestionar carpetas específicas de documentos Excel.
    """

    def __init__(self, base_path):
        """
        Constructor que llama al constructor de la clase padre.
        
        Args:
            base_path (str): Ruta base para gestionar documentos Excel.
        """
        super().__init__(base_path)

    def organize_by_extension(self, extension):
        """
        Organiza archivos en la carpeta base según su extensión.
        
        Args:
            extension (str): Extensión de archivo para organizar (e.g., '.xlsx').
        """
        try:
            files = [f for f in os.listdir(self.base_path) 
                     if os.path.isfile(os.path.join(self.base_path, f)) and f.endswith(extension)]
            if not files:
                print(f"No se encontraron archivos con la extensión '{extension}'.")
                return

            folder_name = extension.lstrip('.').upper() + "_Files"
            self.create_folder(folder_name)
            folder_path = os.path.join(self.base_path, folder_name)

            for file in files:
                src = os.path.join(self.base_path, file)
                dst = os.path.join(folder_path, file)
                shutil.move(src, dst)  # Mover archivo a la nueva carpeta.
                print(f"Movido: {file} -> {folder_name}/")

            print(f"Organización completa. Archivos movidos a '{folder_name}'.")
        except Exception as e:
            print(f"Error al organizar archivos: {e}")
    def organize_by_extension(self, extension):
        # Organiza archivos en la carpeta base según su extensión.
        #
        # Args:
        #   extension (str): Extensión de archivo para organizar (e.g., '.docx').
        try:
            files = [f for f in os.listdir(self.base_path) 
                     if os.path.isfile(os.path.join(self.base_path, f)) and f.endswith(extension)]
            if not files:
                print(f"No se encontraron archivos con la extensión '{extension}'.")
                return

            folder_name = extension.lstrip('.').upper() + "_Files"
            self.create_folder(folder_name)
            folder_path = os.path.join(self.base_path, folder_name)

            for file in files:
                src = os.path.join(self.base_path, file)
                dst = os.path.join(folder_path, file)
                shutil.move(src, dst)  # Mover archivo a la nueva carpeta.
                print(f"Movido: {file} -> {folder_name}/")

            print(f"Organización completa. Archivos movidos a '{folder_name}'.")
        except Exception as e:
            print(f"Error al organizar archivos: {e}")

