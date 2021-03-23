import re

f = open ('C:/Users/Marco/Documents/Pruebas/prueba1.jar','r')
mensaje = f.read()
f.close()
sMs = mensaje.split()

if sMs[0] == "int" :
    #x = re.findall(r"int [a-zA-Z] = \d+;|int [a-zA-Z] = \d+ [\+\-\/\*] \d+;", mensaje)
    if re.findall(r"int ([a-zA-Z]\w+|[a-zA-Z]+) = \d+;|int ([a-zA-Z]\w+|[a-zA-Z]+) = \d+ [\+\-\/\*] \d+;", mensaje):
        print("Ejecución Exitosa")
    else:
        print("Error Asignación de tipo int incorrecta")
elif sMs[0] == "double" :
    if re.findall(r"double ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d);|double ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d) [\+\-\/\*] (\d+\.\d+|\d);", mensaje):
        print("Ejecución Exitosa ")
    else:
        print("Error Asignación de tipo double incorrecta")
elif sMs[0] == "String":
    if re.findall(r"String ([a-zA-Z]\w+|[a-zA-Z]+) = ((\"\w+\s+\w+\")|(\"\w+\s+\")|(\"\w+\"));|String ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = ((\"\w+\s+\w+\")|(\"\w+\s+\")|(\"\w+\"));", mensaje):
        print("Ejecución Exitosa")
    else:
        print("Error Asignación de tipo String incorrecta")
elif sMs[0] == "boolean":
    if re.findall(r"boolean ([a-zA-Z]\w+|[a-zA-Z]+) = \d+ ([\>\<]|==|!=) \d+;|boolean ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = \d+ ([\>\<]|==|!=) \d+;", mensaje):
        print("Ejecución Exitosa")
    else:
        print("Error Asignación de tipo boolean incorrecta")
elif sMs[0] == "float":
    if re.findall(r"float ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d);|float ([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d) [\+\-\/\*] (\d+\.\d+|\d);|float ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d+);|float ([a-zA-Z]\w+|[a-zA-Z]+);\n([a-zA-Z]\w+|[a-zA-Z]+) = (\d+\.\d+|\d) [\+\-\/\*] (\d+\.\d+|\d);", mensaje):
        print("Ejecución Exitosa")
    else:
        print("Error Asignación de tipo float incorrecta")
else:
    print ("Error Asignación de tipo incorrecta")
