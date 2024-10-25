import unittest
from unittest.mock import patch
from cafetera import Vaso, Azucarero, Cafetera, MaquinaDeCafe

class TestVaso(unittest.TestCase):
    def test_crear_vaso(self):
        vaso = Vaso('pequeño', 3)
        self.assertEqual(vaso.tamaño, 'pequeño')
        self.assertEqual(vaso.cantidad_cafe, 3)

class TestAzucarero(unittest.TestCase):
    def setUp(self):
        self.azucarero = Azucarero(5)

    def test_usar_azucar(self):
        self.azucarero.usar_azucar(3)
        self.assertEqual(self.azucarero.cantidad_azucar, 2)
        self.azucarero.usar_azucar(2)
        self.assertEqual(self.azucarero.cantidad_azucar, 0)

    def test_no_hay_azucar(self):
        self.azucarero.usar_azucar(5)
        azucar = self.azucarero.usar_azucar(1)
        self.assertEqual(azucar, 0)

class TestCafetera(unittest.TestCase):
    def setUp(self):
        self.cafetera = Cafetera(10)

    @patch('builtins.print') 
    def test_usar_cafe(self, mock_print):
        self.assertTrue(self.cafetera.usar_cafe(5))
        self.assertEqual(self.cafetera.cantidad_cafe, 5)
        self.assertFalse(self.cafetera.usar_cafe(6))  

class TestMaquinaDeCafe(unittest.TestCase):
    def setUp(self):
        cafetera = Cafetera(20)
        azucarero = Azucarero(5)
        vasos_pequeños = [Vaso('pequeño', 3)] * 2 
        vasos_medianos = [Vaso('mediano', 5)] * 2 
        vasos_grandes = [Vaso('grande', 7)] * 2 
        self.maquina = MaquinaDeCafe(cafetera, azucarero, vasos_pequeños, vasos_medianos, vasos_grandes)

    @patch('builtins.print') 
    def test_preparar_cafe_con_vasos(self, mock_print):
        resultado = self.maquina.preparar_cafe('mediano', 2)
        self.assertTrue(resultado)
        self.assertEqual(len(self.maquina.vasos_medianos), 1) 

    @patch('builtins.print') 
    @patch('builtins.input', return_value='n')
    def test_preparar_cafe_sin_azucar(self, mock_input, mock_print):
        self.maquina.azucarero.usar_azucar(5)
        resultado = self.maquina.preparar_cafe('grande', 2)
        self.assertFalse(resultado)

    @patch('builtins.print')
    def test_no_hay_cafe(self, mock_print):
        self.maquina.cafetera.usar_cafe(20)
        resultado = self.maquina.preparar_cafe('pequeño', 1)
        self.assertFalse(resultado)

    @patch('builtins.print')
    @patch('builtins.input', return_value='s') 
    def test_continuar_con_restante_azucar(self, mock_input, mock_print):
        self.maquina.azucarero.usar_azucar(4) 
        resultado = self.maquina.preparar_cafe('grande', 2)
        self.assertTrue(resultado)  

    @patch('builtins.print') 
    def test_restar_vaso(self, mock_print):

        self.maquina.preparar_cafe('pequeño', 1)
        self.assertEqual(len(self.maquina.vasos_pequeños), 1) 
        self.maquina.preparar_cafe('pequeño', 1)
        self.assertEqual(len(self.maquina.vasos_pequeños), 0)  

    @patch('builtins.print') 
    def test_no_hay_vaso(self, mock_print):
       
        self.maquina.vasos_pequeños = []
     
        resultado = self.maquina.preparar_cafe('pequeño', 1)
        self.assertFalse(resultado)  

if __name__ == '__main__':
    unittest.main(verbosity=2)
