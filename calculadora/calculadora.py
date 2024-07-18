from ast import Return

def somar_dois_numros(num1, num2):
     return num1 + num2

def subtrair_dois_numros(num1, num2):
    return num1 - num2

def multiplicar_dois_numros(num1, num2):
    return num1 * num2

def dividir_dois_numros(num1, num2):
     try:
        return num1 / num2
     except(ZeroDivisionError):
          return 'Divisão por zero invalida'
    
