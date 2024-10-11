from facadehelper import *

facade = FacadeHelper()
    
palabras = ["Hola", "Mundo", "Gato"]
    
for palabra in palabras:
    traduccion = facade.traducir_palabra(palabra)
    mayusculas = facade.convertir_a_mayusculas(palabra)
    minusculas = facade.convertir_a_minusculas(palabra)
        
    print(f"Palabra: {palabra}")
    print(f"Traducción: {traduccion}")
    print(f"Mayúsculas: {mayusculas}")
    print(f"Minúsculas: {minusculas}")
