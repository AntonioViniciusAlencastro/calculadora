import pytest
from calculadora.calculadora import somar_dois_numros, subtrair_dois_numros,multiplicar_dois_numros,dividir_dois_numros

def test_somr_dois_numeros():
    num1 = 5
    num2 = 7
    resultado_esperado = 12
    resultado_obtido = somar_dois_numros(num1,num2)

    assert resultado_esperado == resultado_obtido