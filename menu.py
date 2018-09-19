import os
import operacionesMachine as operaciones
import numbersMachine as numbersMachine

def menu():
    #os.system('clear')
    print "#####################################################################"
    print "Selecciona una opcion:\n"
    print "\t 1.-Establecer los parametros para los numeros de maquina:\n"
    print "\t 2.-Mostrar los numeros de maquina:\n"
    print "\t 3.-Epsilon de maquina:\n"
    print "\t 4.-Aproximacion y truncamiento de un numero real:\n"
    print "\t 5.-Operaciones basicas (+,-,*,/):\n"
    print "\t 6.-Algunas aproximaciones de Taylor:\n"
    print "\t 0.-Salir"
    print "#####################################################################"
while True:
    # Mostramos el menu
    menu()
    opcionMenu = int(input("inserta un numero valor >> "))

    if opcionMenu==1:
        #os.system('clear')
        bits_expo=int(input("ingrese los bits disponibles para los exponentes en maquina ( 2 - 10 )\n"))
        bits_mantiza=int(input("ingrese los bits disponibles para las mantizas  ( 4 - 18 )\n"))
        numeros=numbersMachine.generarNumerosMaquina(bits_expo,bits_mantiza)#creacion de los numeros de maquina
        input("Has pulsado la opcion 1...\npulsa una tecla para continuar")
    elif opcionMenu==2:
        #os.system('clear')
        for i in range(4):
            numeros[i].imprimirnumerosdemaquina()
        input("Has pulsado la opcion 2...\npulsa una tecla para continuar")
    elif opcionMenu==3:
        #os.system('clear')
        eps=operaciones.epsilon_maquina(bits_expo,bits_mantiza)
        epsilon_real=operaciones.de_maquina_a_real(eps,bits_expo,bits_mantiza)
        print "El epsilon de maquina es:\n\n",format(epsilon_real,'.12f')
        input("Has pulsado la opcion 3...\npulsa una tecla para continuar")
    elif opcionMenu==4:
        #os.system('clear')
        numero=str(format(input("ingrese un numero real:\n\n"),'.16f'))
        numero_redondeado=operaciones.busquedabinaria_redondeada(numero,numeros)
        print "redondeado en maquina\n\n",numero_redondeado
        v=operaciones.de_maquina_a_real(numero_redondeado,bits_expo,bits_mantiza-1)
        print "real por redondeo en maquina\n\n",format(v,'.16f')
        numero_truncado=operaciones.busquedabinaria_truncada(numero,numeros)
        print "truncado en maquina\n\n",numero_truncado
        v2=operaciones.de_maquina_a_real(numero_truncado,bits_expo,bits_mantiza-1)
        print "real por truncamiento en maquina\n\n",format(v2,'.16f')
        input("Has pulsado la opcion 4...\npulsa una tecla para continuar")
    elif opcionMenu==5:
        break
        #os.system('clear')
    elif opcionMenu==6:
        break
        #os.system('clear')
    elif opcionMenu==0:
        break
    else:
        print ("")
        input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
