import numpy as np
import cambiodeBase as cb
#recibe como parametro una string y lo transforma a una lista en binario
def transformar_a_binario(numero):
    return cb.convert_numero_lista(numero)#convierte el numero a binario y lo devuelve en lista
def exponentebin_base10(exponente):
    exp_diez=0
    for i in range(len(exponente)):
        exp_diez+=exponente[i]*2**(len(exponente)-i-1)
    return exp_diez
def mantizabin_base10(mantiza):
    mant_diez=0
    for i in range(len(mantiza)):
        mant_diez+=mantiza[i]*2**(len(mantiza)-i-1)
    return mant_diez
def pos_coma_en_numero(numero):
    if '.' not in numero:
        return -1
    else:
        return numero.index('.')
def pos_uno_en_numero(numero):#recibe un array de digitos binarios y busca la posicion del primer 1
    i=0
    posUno=-1
    while i<len(numero):
        if numero[i]==1:
            posUno=i
            i=len(numero)
        i+=1
    return posUno
def signoExponente(numero):
    if int(numero)<0:
        signo_expo=1
    else:
        signo_expo=0
    return signo_expo
def signoNumero(numero):
    if numero[0]=='-':
        signo_numero=1
    else:
        signo_numero=0
    return signo_numero
def transformar_a_exponente_maquina(numero):#recibe un string y devuelve el numero en una lista binaria
    if int(numero)<0:
        numero=-1*int(numero)
        x=transformar_a_binario(str(numero))
    else:
        x=transformar_a_binario(numero)
    if x[len(x)-2]=='.':
        x.pop()
        x.pop()
        return x
    else:
        return x
def transformar_a_mantiza_maquina(v_numero,bits_mantiza):#recibe un array del numero en binario y toma desde el primer 1 hasta el tamanio de la mantiza
    posUno=pos_uno_en_numero(v_numero)
    mantiza_maquina=[]
    tam=bits_mantiza+posUno
    for i in range(posUno,len(v_numero)):
        if v_numero[i] != '.' and len(mantiza_maquina)<bits_mantiza+1:
            mantiza_maquina.append(v_numero[i])
        if i<tam+1:
            valor_actual=i
    tam=valor_actual+1-posUno

    if tam<bits_mantiza+1:
        mantiza_maquina+=[0]*(bits_mantiza+1-tam)

    return mantiza_maquina
def exponenteMaquina(pos_coma,pos_uno):
    exponente=pos_coma-pos_uno+1#valor del exponente
    return exponente
def posicion_del_objeto(signo_numero,signo_expo):
    if signo_numero==1 and signo_expo==0:
        return 0
    if signo_numero==1 and signo_expo==1:
        return 1
    if signo_numero==0 and signo_expo==1:
        return 2
    if signo_numero==0 and signo_expo==0:
        return 3
def buscar_en_maquina(obj,mantiza,exponente):
    carrie=mantiza.pop()#para la aproximacion
    print type(obj.exp)
    if len(exponente)<len(obj.exp[0]):
        exponente=[0]*(len(obj.exp[0])-len(exponente))+exponente
    #ya tenemos el exponente y la mantiza lista para la busqueda
    pos_e=obj.exp.tolist().index(exponente)
    pos_m=obj.mant.tolist().index(mantiza)
    print "sds",pos_e, pos_m
    if obj.signo_mant==1 and obj.signo_expo==0:
        a=0#1er casos
    if obj.signo_mant==1 and obj.signo_expo==1:
        a=0#2do casos
    if obj.signo_mant==0 and obj.signo_expo==1:
        a=0#3er casos
    if obj.signo_mant==0 and obj.signo_expo==0:
        a=0

    return 0
def busquedabinaria(numero,numerosmaquina):#recibe un string
    v_numero=transformar_a_binario(numero)# se transforma el numero a binario y se almacena en una lista
    signo_numero=signoNumero(numero)#guardo el signo del numero 0 positivo , 1 negativo
    print ("numero\n"),v_numero
    print "signo numero:",signo_numero
    exponente=str(exponenteMaquina(pos_coma_en_numero(v_numero),pos_uno_en_numero(v_numero)))#

    signo_expo=signoExponente(exponente)#obtenemos el signo del exponente 0 o 1

    bin_exponente=transformar_a_exponente_maquina(exponente)#transformamos el exponente a lista binaria, se le quita el signo si es negativo

    bin_mantiza=transformar_a_mantiza_maquina(v_numero,numerosmaquina[0].bits_mantiza)
    print ("mantiza en binario\n"),bin_mantiza
    x=posicion_del_objeto(signo_numero,signo_expo)
    print ("exponente real:\n"),exponente
    print ("signo del exponente (positivo=0) (negativo=1):\n"),signo_expo
    print ("exponente en binario\n"),bin_exponente
    aproximacion=buscar_en_maquina(numerosmaquina[x],bin_mantiza,bin_exponente)
    print ("aproximacion:\n"),aproximacion

    return v_numero
