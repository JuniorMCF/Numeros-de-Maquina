import os
import operacionesMachine as operaciones
import numbersMachine as numbersMachine

def menu():
    os.system('clear')
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
        total=0
        for i in range(4):
            total=total+numeros[i].cantidad_de_numeros()
            numeros[i].imprimirnumerosdemaquina()
        #for i in range(4):
        #    print "cantidad de numeros en el objeto:",i+1,numeros[i].cantidad_de_numeros()
        print "hay en total:\n",total,"numeros de maquina sin contar al 0, y sin considerar a los numeros con exponente -0 que son:",2*2**bits_mantiza," ,ya que no tiene sentido almacenarlos";
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
        print "1.-sumar 2 numeros   a + b:\n"
        print "2.-restar 2 numeros  a - b :\n"
        print "3.-multiplicar 2 numeros  a * b :\n"
        print "4.-dividir 2 numeros a \ b :\n"
        opcion=int(input("elija una opcion entre 1 y 4 >>\n"))
        if opcion==1:
            a=str(format(input("ingrese el valor de a >>"),'.16f'))
            b=str(format(input("ingrese el valor de b >>"),'.16f'))
            valor_real_suma=float(a)+float(b)
            #transformando a numero en maquina por aproximacion
            a_maquina=operaciones.busquedabinaria_redondeada(a,numeros)
            a_real=operaciones.de_maquina_a_real(a_maquina,bits_expo,bits_mantiza-1)
            b_maquina=operaciones.busquedabinaria_redondeada(b,numeros)
            b_real=operaciones.de_maquina_a_real(b_maquina,bits_expo,bits_mantiza-1)
            ##SUMA MAQUINA DE a_maquina y b_maquina
            
            print "suma real: ",valor_real_suma
            #print "suma en maquina: ",valor_maquina
        elif opcion==2:
            a=input("ingrese el valor de a >>")
            b=input("ingrese el valor de b >>")
            valor_real_resta=float(a)-float(b)
            #transformando a numero en maquina por aproximacion
            a_maquina=operaciones.busquedabinaria_redondeada(a,numeros)
            a_real=operaciones.de_maquina_a_real(a_maquina,bits_expo,bits_mantiza-1)
            b_maquina=operaciones.busquedabinaria_redondeada(b,numeros)
            b_real=operaciones.de_maquina_a_real(b_maquina,bits_expo,bits_mantiza-1)
            ##RESTA MAQUINA DE a_maquina y b_maquina

            print "suma real: ",valor_real_resta
            #print "suma en maquina: ",valor_maquina

        elif opcion==3:
            a=input("ingrese el valor de a >>")
            b=input("ingrese el valor de b >>")
        elif opcion==4:
            a=input("ingrese el valor del dividendo a >>")
            b=input("ingrese el valor del divisor b >>")
        else:
            break
        input("Has pulsado la opcion 4...\npulsa una tecla para continuar")
    elif opcionMenu==6:
        break
        input("Has pulsado la opcion 4...\npulsa una tecla para continuar")
    elif opcionMenu==0:
        break
        input("Has pulsado la opcion 4...\npulsa una tecla para continuar")
    else:
        print ("")
        input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")
