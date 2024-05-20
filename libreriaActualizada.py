import json
"Clase que representa una librería"
""" Atributos:
        libros (list): Lista que almacena los libros en la librería.
"""
class Libreria:
    def __init__(self):
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        """
        Añade un libro a la librería.
        
        Variables:
            titulo (str): Título del libro.
            autor (str): Autor del libro.
            genero (str): Género del libro.
            anio (int): Año de publicación del libro.

        Returns:
            str: Mensaje indicando que el libro fue añadido.
        """
        self.libros.append({'titulo': titulo, 'autor': autor, 'genero': genero, 'anio': anio})
        return "Libro añadido"

    def buscar_libro(self, titulo):
        """
        Busca un libro por título.
        
        Variables:
            titulo (str): Título del libro a buscar.

        Returns:
            list: Lista de libros que coinciden con el título proporcionado.
        """
        return [libro for libro in self.libros if libro['titulo'].lower() == titulo.lower()]

    def buscar_por_autor(self, autor):
        """
        Busca libros por autor.
        
        Variables:
            autor (str): Autor de los libros a buscar.

        Returns:
            list: Lista de libros escritos por el autor proporcionado.
        """
        return [libro for libro in self.libros if autor.lower() in libro['autor'].lower()]

    def eliminar_libro(self, titulo):
        """
        Elimina un libro por título.
        
        Variables:
            titulo (str): Título del libro a eliminar.

        Returns:
            str: Mensaje indicando si el libro fue eliminado o no encontrado.
        """
        original_count = len(self.libros)
        self.libros = [libro for libro in self.libros if libro['titulo'].lower() != titulo.lower()]
        return "Libro eliminado" if len(self.libros) < original_count else "Libro no encontrado"

    def guardar_libros(self, archivo):
        """
        Guarda los libros en un archivo JSON.
        
        Variables:
            archivo (str): Nombre del archivo JSON donde se guardarán los libros.

        Returns:
            str: Mensaje indicando que los libros fueron guardados.
        """
        with open(archivo, 'w') as f:
            json.dump(self.libros, f)
        return "Libros guardados"

    def cargar_libros(self, archivo):
        """
        Carga los libros desde un archivo JSON.
        
        Variables:
            archivo (str): Nombre del archivo JSON del que se cargarán los libros.

        Returns:
            str: Mensaje indicando que los libros fueron cargados.
        """
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"
    def obtener_generos(self):
        """
        Obtiene una lista de todos los géneros únicos presentes en la librería.

        Returns:
            list: Lista de géneros únicos.
        """
        return list(set(libro['genero'] for libro in self.libros))

mi_libreria = Libreria()
mi_libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
mi_libreria.guardar_libros('libreria.json')
print(mi_libreria.cargar_libros('libreria.json'))
print(mi_libreria.buscar_por_autor("Gabriel García Márquez"))


