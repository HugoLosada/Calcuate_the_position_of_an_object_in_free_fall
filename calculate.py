#Este programa va servir para calcular el área de un triángulo

def calcular_area(base,altura):
    area = base * altura / 2
    return area 

#Pido la base y la altura del triángulo
altura_input = float(input("Altura?: "))
base_input = float(input("Base?: "))
#guardo el area calculada por la función en una variable
area_calculada = calcular_area(base_input,altura_input)

#Pinto la base calculada 
print("El área calculada es:",area_calculada)