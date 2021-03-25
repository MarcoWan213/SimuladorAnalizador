import re
#Se abre el archivo a utilizar colocando la ruta en donde se encuentra la carpeta de pruebas 
# y del nombre de la puebra que se ejecutara. 
f = open ('C:/Users/Marco/Documents/Pruebas/prueba1.jar','r')
mensaje = f.read() 
f.close()
sMs = mensaje.split()
 
#Declaración la primera condición para del tipo primitivo entero
if sMs[0] == "int" :
    #x = re.findall(r"int [a-zA-Z] = \d+;|int [a-zA-Z] = \d+ [\+\-\/\*] \d+;", mensaje)
    #Declaración de la expresión regular para encontrar cualquier valor númerico entero(INT)
    if re.findall(r"int ([a-zA-Z]\w+|[a-zA-Z]+) = \d+;|int ([a-zA-Z]\w+|[a-zA-Z]+) = \d+ [\+\-\/\*] \d+;", mensaje):
        print("Ejecución Exitosa")
    else:
        #Mensaje de error en ingresar un valor de tipo int incorrecto
        print("Error Asignación de tipo int incorrecta")
#Declaración de la condición del tipo primitivo double 
elif sMs[0] == "double" :
#Condición if con la declaración de la expresión regular para encontrar cualquier valor numerico de tipo double 
    if re.findall(r"double ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d);|double ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d) [\+\-\/\*] (\d+\.\d+|\d);", mensaje):
        print("Ejecución Exitosa ")
    else:
    #Imprimir o arrojar un mensaje de error al encontrar un valor declarado de tipo double de manera incorrecta
        print("Error Asignación de tipo double incorrecta")
#Declaración de la condición del tipo primitivo string 
elif sMs[0] == "String":
    #Declaración de la condición if con la expresión regular correspondiente para encontrar cualquier varibales que 
    #sea de tipo string.
    if re.findall(r"String ([a-zA-Z]\w+|[a-zA-Z]+) = ((\"\w+\s+\w+\")|(\"\w+\s+\")|(\"\w+\"));|String ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = ((\"\w+\s+\w+\")|(\"\w+\s+\")|(\"\w+\"));", mensaje):
       #Si el archivo se encuentra correctamente con alguna estructura string, se imprimira el siguiente texto
        print("Ejecución Exitosa")
    else:
        #De lo contrario de imprimira este mensaje en donde indique que fue asignado de manera incorrecta la variable string
        print("Error Asignación de tipo String incorrecta")
  #Declaración de la condición del tipo primitivo boolean 
elif sMs[0] == "boolean":
    #Declaración de la condición if y la expresión regular que encuentre los datos de tipo boolean 
    if re.findall(r"boolean ([a-zA-Z]\w+|[a-zA-Z]+) = \d+ ([\>\<]|==|!=) \d+;|boolean ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = \d+ ([\>\<]|==|!=) \d+;", mensaje):
       #Si la asignación de la variable fue declarada correctamente dentro de la prueba, arrojara el siguiente texto de aprovación
        print("Ejecución Exitosa")
    else:
        #De lo contrario se imprimira el siguiente mensaje en donde nos indica que hubo un error al momento de asignarle el valor
        print("Error Asignación de tipo boolean incorrecta")
 #Declaración del tipo de dato primitivo float 
elif sMs[0] == "float":
    #Condición con la expresión regular que encuentre cualquier dato que corresponda al tipo de variable float
    if re.findall(r"float ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d);|float ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d) [\+\-\/\*] (\d+\.\d+|\d);|float ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d+);|float ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d) [\+\-\/\*] (\d+\.\d+|\d);", mensaje):
        #Si la declaración del dato de tipo float ha sido realizado de manera correcta imprimira el siguiente mensaje
        print("Ejecución Exitosa")
    else:
        #De lo cotrario imprimira el siguiente texto cuando la declaración de tipo float no corraponda a este tipo de variable
        print("Error Asignación de tipo float incorrecta")
else:
    #Mensaje de error cuando ningun tipo de dado ha sido ingresado de manera correcta
    print ("Error Asignación de tipo incorrecta")
