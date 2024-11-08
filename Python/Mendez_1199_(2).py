print(" ")
print("Mendez Sanchez Maria Guadalupe Yazmin 1199 3W")
print(" ")
def nota(calif):           #Definir la nota con la calificacion y regresar mensaje
    #Agregar condiciones y agregar mensajes
    if calif <= 5:           
        return "SUSPENSO"     
    elif calif <=6:           
        return "SUFICIENTE"   
    elif calif <=7:           
        return "BIEN"  
    elif calif <=8:  
        return "NOTABLE"  
    elif calif <=9 <=10:  
        return "SOBRESALIENTE"  
    else:
        print("NOTA NO VALIDA")  
calif=int(input("Ingresa tu calificacion: "))  #Solicitar la calificacion
print(" ")
mensaje= nota(calif)                           #Declarar variavle
print(mensaje)                                 #Imprimir la variable del mensaje
print(" ")
