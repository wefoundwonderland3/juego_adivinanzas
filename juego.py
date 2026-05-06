# Juego creado por [Tu Nombre] - Repaso de Git 
import random

def jugar():
    print(" --- ¡Adivina el Número! --- ")
    numero_secreto = random.randint(1, 10)
    intentos = 0
    
    while True:
        intento = int(input("Elige un número entre 1 y 10 (o 0 para salir): "))
        intentos += 1
        
        if intento == 0:
            print("Te rendiste. Suerte para la proxima.")
            break
        
        if intento == numero_secreto:
            print(f"¡Ganaste en {intentos} intentos!")
            break
        elif intento < numero_secreto:
            print("El número es mas alto.")
        else:
            print("El numero es mas bajo.")

if __name__ == "__main__":
    jugar()

