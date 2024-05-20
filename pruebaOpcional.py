import unittest
from libreriaActualizada import Libreria

class TestLibreria(unittest.TestCase):
    def setUp(self):
        self.libreria = Libreria()

    # Métodos de prueba existentes...

    def test_obtener_generos(self):
        # Añadimos algunos libros con diferentes géneros
        self.libreria.anadir_libro("Cien años de soledad", "Gabriel García Márquez", "Novela", 1967)
        self.libreria.anadir_libro("El Aleph", "Jorge Luis Borges", "Ficción", 1949)
        self.libreria.anadir_libro("El Quijote", "Miguel de Cervantes", "Novela", 1605)
        # Verificamos que el método obtener_generos devuelva una lista con los géneros únicos
        generos = self.libreria.obtener_generos()
        self.assertCountEqual(generos, ["Novela", "Ficción"])
        # Verificamos explícitamente que la lista de géneros contiene el género "Novela"
        self.assertIn("Novela", generos)
        # Imprimimos la lista de géneros para verla en la salida
        print("Lista de géneros:", generos)


if __name__ == '__main__':
    unittest.main()
