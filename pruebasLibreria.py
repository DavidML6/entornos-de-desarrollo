import unittest
from libreriaActualizada import Libreria  # Suponiendo que el archivo principal se llama libreria.py

class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()

    def test_anadir_libro(self):
        self.assertEqual(self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967), "Libro añadido")

    def test_buscar_libro(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.buscar_libro("Cien años de soledad"), [{'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'genero': 'Novela', 'anio': 1967}])

    def test_buscar_por_autor(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.buscar_por_autor("Gabriel García Márquez"), [{'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'genero': 'Novela', 'anio': 1967}])

    def test_eliminar_libro(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.assertEqual(self.libreria.eliminar_libro("Cien años de soledad"), "Libro eliminado")

    def test_guardar_cargar_libros(self):
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.guardar_libros('test_libreria.json')
        self.assertEqual(self.libreria.cargar_libros('test_libreria.json'), "Libros cargados")
        self.assertEqual(self.libreria.buscar_por_autor("Gabriel García Márquez"), [{'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez', 'genero': 'Novela', 'anio': 1967}])


if __name__ == '__main__':
    unittest.main()
