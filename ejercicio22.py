"""
    @reroes
    Programación Funcional: 
        Funciones Puras
        Efectos Secundarios
"""

valor_global = 3

def multiplicacion(n):
    """
        return n**2
    """
    valor_local = n**valor_global

    return valor_local

print(multiplicacion(10))
