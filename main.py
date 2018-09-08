import numpy as np
import numbersMachine as numbersMachine
import operacionesMachine as operaciones
def main():
    #bits_expo=int(input("ingrese los bits disponibles para los exponentes en maquina\n"))
    #bits_mantiza=int(input("ingrese los bits disponibles para las mantizas\n"))
    bits_expo=2
    bits_mantiza=4

    numeros=numbersMachine.generarNumerosMaquina(bits_expo,bits_mantiza)#crea una lista con 4 objetos tipo "NumeroMaquina"
    for i in range(4):
        numeros[i].imprimirnumerosdemaquina()

    numero=str(input("ingrese un numero real:\n"))
    numero_aprox=operaciones.busquedabinaria(numero,numeros)#metodo que aproxima nuestro numero ingresado por teclado a un numero en maquina

main()
