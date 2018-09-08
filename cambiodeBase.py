#programa que cambia de base 2 a 10 y viceversa para un numero almacenado en una lista
import numpy as np
from collections import deque
import operacionesMachine as op
import math

def imprimirProcesoTransformacion(cocientes,residuos,cambioBase):
    for i in range(len(cocientes)-1,-1,-1):
        print cambioBase,"*",cocientes.pop(i),"+",residuos.pop(i)
def imprimirProcesoTransformacionDec(enteros,fracciones,cambioBase):
    for i in fracciones:
        print i
def parteEntera(numero):
    num=''.join(map(str,numero))#unimos la lista
    separar=num.split(".")#separamos en dos elementos separados por el "."
    if '.' not in numero:
        entero=int(num)
    else:
        entero=int(separar[0])#parte entera
    return entero
def parteDecimal(numero):
    num=''.join(map(str,numero))#unimos la lista
    separar=num.split(".")#separamos en dos elementos separados por el "."
    if '.' not in numero:
        decimal=0
    else:
        decimal=separar[1]#parte decimal
    return decimal
def transformacionEntera(numero,baseOriginal,cambioBase):
    residuos=[]#cola de residuos para la parte entera
    cocientes=[]#resultados de las divisiones sucesivas
    if numero==0:
        residuos.append(0)
    if numero<0:
        numero=-1*numero
    while (numero/cambioBase)!=0 or numero==1:
        residuos.append(numero%cambioBase)
        numero=numero/cambioBase
        cocientes.append(numero)
    residuos.reverse()
    residuosguardados=residuos[:]#hacemos un slicing de la lista residuos, ya que esta sera eliminada al desencolar en la impresion
    #imprimirProcesoTransformacion(cocientes,residuos,cambioBase)
    return residuosguardados
def transformacionDecimal(decimal,baseOriginal,cambioBase):
    max_enteros=[]#se pone en cola estos enteros para el resultado final
    fracc=[]#resultados para las multiplicaciones sucesivas
    decimal='0'+'.'+str(decimal)
    #decimal = float(decimal)
    v_decimal=[]
    decimal=list(decimal)

    for i in range(decimal.index('.')+1,len(decimal)):
        v_decimal.append(int(decimal[i]))

    while v_decimal not in fracc:
        fracc.append(v_decimal)
        v_decimal=[x*2 for x in v_decimal]
        for i in range(len(v_decimal)-1,0,-1):
            v_decimal[i-1]+=v_decimal[i]/10
            v_decimal[i]=v_decimal[i]%10
        max_enteros.append(v_decimal[0]/10)
        if v_decimal[0]>=10:
            v_decimal[0]=v_decimal[0]%10
        if all(v==0 for v in v_decimal):
            break

    enterosguardados=max_enteros[:]#hacemos un slicing de la lista
    #imprimirProcesoTransformacionDec(max_enteros,fracc,cambioBase)
    return enterosguardados
def listaDecimal_a_Binaria(numero,baseOriginal,cambioBase):
    enteroNumero=parteEntera(numero)#para trabajar el cambio de base en la parte entera
    fraccionNumero=parteDecimal(numero)#para trabajar la parte decial en el cambio de base
    enteroBinario=transformacionEntera(enteroNumero,baseOriginal,cambioBase)
    fraccionBinario=transformacionDecimal(fraccionNumero,baseOriginal,cambioBase)
    #enteroBinario.sort(reverse=True)
    numeroConvertido= enteroBinario+['.']+fraccionBinario
    #print numeroConvertido
    return numeroConvertido

def convert_numero_lista(numero):
    numerolist=list(numero)
    #print numerolist
    for i in range (0,len(numerolist)):
        if numerolist[i]!='.':
            if numerolist[i]=='-':
                numerolist[i]='-'
            else:
                numerolist[i]=int(numerolist[i])
        else:
            numerolist[i]='.'
    numeroConvertido=listaDecimal_a_Binaria(numerolist,10,2)
    return numeroConvertido
