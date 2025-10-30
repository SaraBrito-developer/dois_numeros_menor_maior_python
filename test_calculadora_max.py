# -*- coding: utf-8 -*-
import unittest

from calculadora_max import encontrar_maior

class TestEncontrarMaior(unittest.TestCase):
    
    def test_primeiro_numero_maior(self):
        """Testa se o primeiro número é reconhecido como maior"""
        self.assertEqual(encontrar_maior(10, 3), 10)

    def test_segundo_numero_maior(self):
        """Testa se o segundo número é reconhecido como maior"""
        self.assertEqual(encontrar_maior(3, 10), 10)

    def test_numeros_iguais(self):
        """Testa o que acontece quando os números são iguais"""
        self.assertEqual(encontrar_maior(10, 10), 10)

    def test_com_numeros_negativos(self):
        """Testa com dois números negativos"""
        self.assertEqual(encontrar_maior(-10, -5), -5)

    def test_negativo_e_positivo(self):
        """Testa um número negativo e um positivo"""
        self.assertEqual(encontrar_maior(-10, 5), 5)

    def test_com_zero(self):
        """Testa um número contra o zero"""
        self.assertEqual(encontrar_maior(0, -5), 0)

if __name__ == '__main__':
    unittest.main()
