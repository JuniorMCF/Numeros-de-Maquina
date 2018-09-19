import numpy as np
import cambiodeBase as cb
import sys
#recibe como parametro una string y lo transforma a una lista en binario
def transformar_a_binario(numero):
    return cb.convert_numero_lista(numero)#convierte el numero a binario y lo devuelve en lista
def exponentebin_base10(exponente):
    exp_diez=0
    for i in range(len(exponente)):
        exp_diez+=exponente[i]*2**(len(exponente)-i-1)
    return exp_diez
def mantizabin_base10(mantiza):
#    mant_diez=0
#    for i in range(len(mantiza)):
#        mant_diez+=mantiza[i]*2**(len(mantiza)-i-1)
#    return mant_diez
    mant_diez=0
    for i in range(len(mantiza)):
        mant_diez+=mantiza[i]*2**(-i-1)
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

    count=0# contara si se agregaron todos los valores necesarios para mi mantiza en maquina
    for i in range(posUno+1,len(v_numero)):
        if v_numero[i] != '.' and len(mantiza_maquina)<bits_mantiza+1:
            mantiza_maquina.append(v_numero[i])
            count+=1

    if count<bits_mantiza+1:
        mantiza_maquina+=[0]*(bits_mantiza+1-count)

    return mantiza_maquina
def exponenteMaquina(pos_coma,pos_uno):
    #print "poscoma,posuno",pos_coma,pos_uno
    if pos_coma==1 and pos_uno==-1:
        exponente=-8182
        return exponente
    if pos_coma>pos_uno:
        exponente=pos_coma-pos_uno#valor del exponente
    else:
        exponente=pos_coma-pos_uno+1
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
def epsilon_maquina(tam_exp,tam_mant):
    epsilon_maquina=[]
    epsilon_maquina.append(0)#signo mantiza negativo
    epsilon_maquina.append(1)#signo exponente
    #print "tamanios",tam_exp,tam_mant
    for i in range(tam_exp):
        epsilon_maquina.append(1)
    for j in range(tam_mant):
        epsilon_maquina.append(0)
    return epsilon_maquina
def buscar_en_maquina_redondeo(obj,mantiza,exponente,maquina):
    bit_carry=mantiza.pop()#para la aproximacion
    #obtenemos las posiciones de los exponentes y mantizas en el respecrivo objeto
    aproximacion=[]
    aproximacion.append(obj.signo_mant)
    aproximacion.append(obj.signo_expo)

    #print aproximacion
    pos_e=obj.exp.tolist().index(exponente)
    pos_m=obj.mant.tolist().index(mantiza)
    #print "pos_e",pos_e
    #print "pos_m",pos_m

    if obj.signo_mant==1 and obj.signo_expo==0:#numero negativo con exponente positivo
        if pos_m<=obj.getlenmant() and pos_m>0 and bit_carry==1:
            pos_m-=1# debido a que si la mantiza es mas pequenia el numero es mas grande(en los negativos)
        if pos_m==0 and bit_carry==1:
            if pos_e>0 and pos_e<obj.getlenexp():
                pos_e-=1
            if pos_e==0:# en este caso se desborda al objeto 2 tomando el lugar de su ultima mantiza y primer exponente
                aproximacion.append(maquina[1].obtener_exponente(pos_e))
                aproximacion.append(maquina[1].obtener_mantiza(maquina[1].getlenmant()))
                return aproximacion
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        aproximacion.append(obj.obtener_exponente(pos_e))
        aproximacion.append(obj.obtener_mantiza(pos_m))

    if obj.signo_mant==1 and obj.signo_expo==1:
        if pos_m<=obj.getlenmant() and pos_m>0 and bit_carry==1:
            pos_m-=1# debido a que si la mantiza es mas pequenia el numero es mas grande(en los negativos)
        if pos_m==0 and bit_carry==1:
            if pos_e>0 and pos_e<obj.getlenexp():
                pos_e+=1
            if pos_e==obj.getlenexp():# este es mi 0 de maquina negativo (underflow)
                aproximacion.pop()#quitamos los valores para pedir el cero en maquina
                aproximacion.pop()
                aproximacion=cero_maquina(len(mantiza),len(exponente))
                return aproximacion
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        aproximacion.append(obj.obtener_exponente(pos_e))
        aproximacion.append(obj.obtener_mantiza(pos_m))

    if obj.signo_mant==0 and obj.signo_expo==1:
        if pos_m<=obj.getlenmant() and pos_m>0 and bit_carry==1:
            pos_m+=1# avanzo en las mantizas positivas
        if pos_m==obj.getlenmant() and bit_carry==1:
            if pos_e>0 and pos_e<obj.getlenexp():
                pos_e-=1
            if pos_e==0:# este caso conecta el objeto 3 con el objeto 4
                aproximacion.append(maquina[3].obtener_exponente(pos_e))
                aproximacion.append(maquina[3].obtener_mantiza(0))
                return aproximacion
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        aproximacion.append(obj.obtener_exponente(pos_e))
        aproximacion.append(obj.obtener_mantiza(pos_m))

    if obj.signo_mant==0 and obj.signo_expo==0:
        if pos_m<=obj.getlenmant() and pos_m>0 and bit_carry==1:
            pos_m+=1# avanzo en la mantizas positivas
        if pos_m==obj.getlenmant() and bit_carry==1:
            if pos_e>0 and pos_e<obj.getlenexp():
                pos_e+=1
            if pos_e==obj.getlenexp():# este caso es donde se desborda
                aproximacion.append(obj.obtener_exponente(pos_e))
                aproximacion.append(obj.obtener_mantiza(pos_m))
                return aproximacion
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        aproximacion.append(obj.obtener_exponente(pos_e))
        aproximacion.append(obj.obtener_mantiza(pos_m))
    return aproximacion
def buscar_en_maquina_truncamiento(obj,mantiza,exponente,maquina):
    bit_carry=mantiza.pop()#para el truncamiento consideraremos este bit 0
    bit_carry=0 # forzamos nuestro carry a 0
    #obtenemos las posiciones de los exponentes y mantizas en el respecrivo objeto
    truncamiento=[]
    truncamiento.append(obj.signo_mant)
    truncamiento.append(obj.signo_expo)

    pos_e=obj.exp.tolist().index(exponente)
    pos_m=obj.mant.tolist().index(mantiza)
    #print "pos_e",pos_e
    #print "pos_m",pos_m

    if obj.signo_mant==1 and obj.signo_expo==0:#numero negativo con exponente positivo
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        truncamiento.append(obj.obtener_exponente(pos_e))
        truncamiento.append(obj.obtener_mantiza(pos_m))

    if obj.signo_mant==1 and obj.signo_expo==1:
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        truncamiento.append(obj.obtener_exponente(pos_e))
        truncamiento.append(obj.obtener_mantiza(pos_m))

    if obj.signo_mant==0 and obj.signo_expo==1:
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        truncamiento.append(obj.obtener_exponente(pos_e))
        truncamiento.append(obj.obtener_mantiza(pos_m))

    if obj.signo_mant==0 and obj.signo_expo==0:
        if bit_carry==0:
            pos_e=pos_e#no hay aproximacion
            pos_m=pos_m#no hay aproximacion
        truncamiento.append(obj.obtener_exponente(pos_e))
        truncamiento.append(obj.obtener_mantiza(pos_m))
    return truncamiento
def check_overflow(signo_numero,signo_expo,bin_exponente,bits_expo):#e : exponente maquina
    if len(bin_exponente)>bits_expo:
        if signo_numero==0:
            if signo_expo==0:
                return 0#overflow
            if signo_expo==1:
                return -1#undeflow
        if signo_numero==1:
            if signo_expo==0:
                return 0#overflow
            if signo_expo==1:
                return -1#undeflow
    else:
        return 1
def de_maquina_a_lista(numero_maquina):
    numero_lista=[]
    numero_lista.append(numero_maquina[0])
    numero_lista.append(numero_maquina[1])
    for i in numero_maquina[2]:
        numero_lista.append(i)
    for j in numero_maquina[3]:
        numero_lista.append(j)
    return numero_lista
def de_maquina_a_real(lista,long_exp,long_mant):
    signo_mantiza=lista[0]
    signo_exponente=lista[1]
    exponente=lista[2:2+long_exp]
    exponente_real=exponentebin_base10(exponente)
    if signo_exponente==1:
        exponente_real=-1*exponente_real
    mantiza=lista[2+long_exp:2+long_exp+long_mant]
    base_maquina=[1]+mantiza
    base_real=mantizabin_base10(base_maquina)
    if signo_mantiza==1:
        base_real=-1*base_real
    numero=base_real*2**exponente_real
    #print "base",base_real
    #print "exponente",exponente_real
    return numero

def busquedabinaria_redondeada(numero,numerosmaquina):#recibe un string
    v_numero=transformar_a_binario(numero)# se transforma el numero a binario y se almacena en una lista
    signo_numero=signoNumero(numero)#guardo el signo del numero 0 positivo , 1 negativo
    #print ("numero\n"),v_numero
    #print "signo numero:",signo_numero
    exponente=str(exponenteMaquina(pos_coma_en_numero(v_numero),pos_uno_en_numero(v_numero)))#
    #print v_numero
    signo_expo=signoExponente(exponente)#obtenemos el signo del exponente 0 o 1
    #print "exp",exponente
    bin_exponente=transformar_a_exponente_maquina(exponente)#transformamos el exponente a lista binaria, se le quita el signo si es negativo

    bin_mantiza=transformar_a_mantiza_maquina(v_numero,numerosmaquina[0].bits_mantiza)
    #print ("mantiza en binario\n"),bin_mantiza
    x=posicion_del_objeto(signo_numero,signo_expo)
    #print ("exponente real:\n"),exponente
    #print ("signo del exponente (positivo=0) (negativo=1):\n"),signo_expo
    #print ("exponente en binario\n"),bin_exponente
    # verifico que el exponente en binario tenga por lo menos el tamanio de bits de mi exponente en maquina
    if len(bin_exponente)<numerosmaquina[x].bits_expo:
        bin_exponente=[0]*(numerosmaquina[x].bits_expo-len(bin_exponente))+bin_exponente
    flag=check_overflow(signo_numero,signo_expo,bin_exponente,numerosmaquina[x].bits_expo)#si flag es -1 underflow si flag es 0 overflow si es diferente hace la busqueda
    #print "flag",flag
    if flag==1:## en este caso hacemos la busqueda
        aproximacion=buscar_en_maquina_redondeo(numerosmaquina[x],bin_mantiza,bin_exponente,numerosmaquina)
    if flag==0:
        print "OVERFLOW"
        sys.exit()
    if flag==-1:## aqui el numero se desbordo hacia 0, como no existe 0 en notacion normalizada se devolvera un caso especial
        aprox=epsilon_maquina(numerosmaquina[0].bits_expo,numerosmaquina[0].bits_mantiza)
    if flag!=-1:
        aprox=de_maquina_a_lista(aproximacion)
    #print "v_numero",v_numero
    return aprox

def busquedabinaria_truncada(numero,numerosmaquina):#recibe un string
    v_numero=transformar_a_binario(numero)# se transforma el numero a binario y se almacena en una lista
    signo_numero=signoNumero(numero)#guardo el signo del numero 0 positivo , 1 negativo
    #print ("numero\n"),numero
    #print "signo numero:",signo_numero
    exponente=str(exponenteMaquina(pos_coma_en_numero(v_numero),pos_uno_en_numero(v_numero)))#
    #print v_numero
    signo_expo=signoExponente(exponente)#obtenemos el signo del exponente 0 o 1
    #print "exp",exponente
    bin_exponente=transformar_a_exponente_maquina(exponente)#transformamos el exponente a lista binaria, se le quita el signo si es negativo

    bin_mantiza=transformar_a_mantiza_maquina(v_numero,numerosmaquina[0].bits_mantiza)
    #print ("mantiza en binario\n"),bin_mantiza
    x=posicion_del_objeto(signo_numero,signo_expo)
    #print ("exponente real:\n"),exponente
    #print ("signo del exponente (positivo=0) (negativo=1):\n"),signo_expo
    #print ("exponente en binario\n"),bin_exponente
    # verifico que el exponente en binario tenga por lo menos el tamanio de bits de mi exponente en maquina
    if len(bin_exponente)<numerosmaquina[x].bits_expo:
        bin_exponente=[0]*(numerosmaquina[x].bits_expo-len(bin_exponente))+bin_exponente
    flag=check_overflow(signo_numero,signo_expo,bin_exponente,numerosmaquina[x].bits_expo)#si flag es -1 underflow si flag es 0 overflow si es diferente hace la busqueda
    #print "flag",flag
    if flag==1:## en este caso hacemos la busqueda
        truncamiento=buscar_en_maquina_truncamiento(numerosmaquina[x],bin_mantiza,bin_exponente,numerosmaquina)
    if flag==0:
        print "OVERFLOW"
        sys.exit()
    if flag==-1:## aqui el numero se desbordo hacia 0, como no existe 0 en notacion normalizada se devolvera un caso especial
        truncado=epsilon_maquina(numerosmaquina[0].bits_expo,numerosmaquina[0].bits_mantiza)
    if flag!=-1:
        truncado=de_maquina_a_lista(truncamiento)
    #print "v_numero",v_numero
    return truncado
