import numpy as np
import cambiodeBase as cb
from nodos import NumeroMaquina
##METODOS QUE GENERAN LOS NUMEROS DE MAQUINA
def generaExponentes(bits_expo):#recibe la cantidad de bits disponibles para la base y genera los exponentes
    exponentes_enteros=np.arange(2**bits_expo)#genero todos los nueros posibles para mis exponentes
    expMachine=[]#lista vacia para los exponentes en maquina en binario
    for i in exponentes_enteros:
        x=cb.transformacionEntera(int(i),10,2)#transformo el elemento i de exponentes_enteros de base 10 a base 2
        t=bits_expo-len(x)#calculamos el tamanio de x por si no se iguala al tamanio de los bits disponibles
        if t>0:
            x=[0]*t + x #agregamos 0 a la izquierda para completar el tamanio de bits
            expMachine.append(x)#agrego cada elemento en binario a la lista
            del(x)
        else:
            expMachine.append(x)
            del(x)
    return expMachine

def generaMantizas(bits_mantiza):#recibe la cantida de bits disponibles para la mantiza y genera los numeros posibles
    mantizas_enteras=np.arange(2**bits_mantiza)#genero todos los nueros posibles para mis mantizas
    mantizasMachine=[]#lista vacia para los exponentes en maquina en binario
    for i in mantizas_enteras:
        x=cb.transformacionEntera(int(i),10,2)#transformo el elemento i de exponentes_enteros de base 10 a base 2
        t=bits_mantiza-len(x)#calculamos el tamanio de x por si no se iguala al tamanio de los bits disponibles
        if t>0:
            x=[0]*t + x #agregamos 0 a la izquierda para completar el tamanio de bits
            mantizasMachine.append(x)#agrego cada elemento en binario a la lista
            del(x)
        else:
            mantizasMachine.append(x)
            del(x)
    return mantizasMachine

def generarNumerosMaquina(bits_expo,bits_mantiza):
    exponentes=np.array(generaExponentes(bits_expo))
    mantizas=np.array(generaMantizas(bits_mantiza))
    #print len(mantizas)
    #print len(exponentes)
    lista_de_numeros_maquina=[]

    numeros_nega_expo_posi = NumeroMaquina(exponentes,mantizas,1,0)#numeros negativos con exponentes positivos
    lista_de_numeros_maquina.append(numeros_nega_expo_posi)

    numeros_nega_expo_nega = NumeroMaquina(exponentes[1:],mantizas,1,1)#numeros negativos con exponentes negativos
    lista_de_numeros_maquina.append(numeros_nega_expo_nega)

    numeros_posi_expo_nega = NumeroMaquina(exponentes[1:],mantizas,0,1)#numeros positivos con exponentes negativos
    lista_de_numeros_maquina.append(numeros_posi_expo_nega)

    numeros_posi_expo_posi = NumeroMaquina(exponentes,mantizas,0,0)#numeros positivos con exponentes positivos
    lista_de_numeros_maquina.append(numeros_posi_expo_posi)
    #numeros_posi_expo_posi.imprimirObjeto()
    #numeros_posi_expo_nega.imprimirObjeto()
    #numeros_nega_expo_posi.imprimirObjeto()
    #numeros_nega_expo_nega.imprimirObjeto()
    return lista_de_numeros_maquina
