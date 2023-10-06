#Este programa va a consistir en un bot que responda a las preguntas que le hacemos.
name = input("Hola, como te llamas? ")
texto1 = f"Hola, {name}, encantado de conocerte"
input(texto1)
text2 = f"Cuantos años tienes {name}? "
age = int(input(text2))
#Ponemos el int para convertir el texto a entero para despues poder poner la condición
if age == 18:
   condición1= f"ahhh,{name}  eres mayor de edad, que bien!"
   print(condición1)
elif age  >= 50:
   condición2 = f"vaya {name}... eres viejo"
   print(condición2)
#utilizamos if elif y e else para dar una condicion, si su edad es 18 dira una cosa, pero si es mayor de 50 se añadira otra frase.
else:
     condición3 = f"Ahhh, osea que aún eres jovén {name}"
     print(condición3)
text3 = "Y de donde eres?: " 
origen = str(input(text3))
if origen == "Madrid":
    print("ahhh, como yo, a mi me crearon aquí ;)")
else:
    print("Estás lejos de casa ehhhh ")
hobby = "Y que haces en tu tiempo libre?: "
input(hobby)
text4 = "Ahhh, que guay, y solo haces eso?: "
condición4 = str(input(text4))
if condición4 == "Si":
    print("vaya vago")
else:
    print("ahhh, muy bien, ya pensé que eras un vago")