import unittest
from libreriaActualizada import Libreria  # Suponiendo que el archivo principal se llama libreria.py


class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()

    def test_anadir_libro(self):
        # Caso típico
        self.assertEqual(self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967), "Libro añadido")
        # Caso extremo: Título vacío
        self.assertEqual(self.libreria.anadir_libro("", "Gabriel García Márquez", "Novela", 1967), "Libro añadido")
        # Caso extremo: Año negativo
        self.assertEqual(self.libreria.anadir_libro("Rayuela", "Julio Cortázar", "Novela", -1963), "Libro añadido")

    def test_buscar_libro(self):
        # Caso típico
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.buscar_libro("Cien años de soledad"), [{'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez', 'genero': 'Novela', 'anio': 1967}])
        # Caso extremo: Título no encontrado
        self.assertEqual(self.libreria.buscar_libro("Rayuela"), [])

    def test_buscar_por_autor(self):
        # Caso típico
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.buscar_por_autor("Gabriel García Márquez"), [{'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez',
        'genero': 'Novela', 'anio': 1967}])
        # Caso extremo: Autor no encontrado
        self.assertEqual(self.libreria.buscar_por_autor("Mario Vargas Llosa"), [])

    def test_eliminar_libro(self):
        # Caso típico
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")
        # Caso extremo: Libro no encontrado
        self.assertEqual(self.libreria.eliminar_libro("Rayuela"), "Libro no encontrado")

    def test_guardar_cargar_libros(self):
        # Caso típico
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.guardar_libros('test_libreria.json')
        self.assertEqual(self.libreria.cargar_libros('test_libreria.json'), "Libros cargados")
        self.assertEqual(self.libreria.buscar_por_autor("Gabriel García Márquez"), [{'titulo': 'Cien años de soledad', 
        'autor': 'Gabriel García Márquez', 'genero': 'Novela', 'anio': 1967}])
        # Caso extremo: Archivo no encontrado
        self.assertEqual(self.libreria.cargar_libros('archivo_inexistente.json'), "Archivo no encontrado")


if __name__ == '__main__':
    unittest.main()
