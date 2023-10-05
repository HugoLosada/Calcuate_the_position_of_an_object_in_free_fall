#En este programa vamos a crear tres variables, posición tiempo y velocidad 
initial_height = float(input("Enter initial height: "))
#Pongo esto para que sea el usuario el que elija el valor de la posición
gravity = 9.81
initial_velocity = float(input("Enter initial velocity: "))
time = float(input("Enter time: "))
#hacemos lo mismo con el tiempo y con la velocidad
position = initial_height + initial_velocity * time - 1/2 * gravity * time**2
#Ponemos la formula para calcular la posición final. Para poner el elevado utilizamos el doble asterísco
print("The position is: ",position)
#Por último ponemos ponemos esto para que el programa nos delvuela el valor