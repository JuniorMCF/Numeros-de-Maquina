import numpy as np
import math
import operacionesMachine as operaciones
class NumeroMaquina:
    tipo = 'NumeroMaquina'
    #bits_expo=0
    #bits_mantiza=0
    #exp=0
    #mant=0
    #signo_expo=-1
    #signo_mant=-1
    def __init__(self,exponente,mantiza,signo_mant,signo_expo):
        self.bits_expo=len(exponente)#
        self.bits_mantiza=int(math.sqrt(len(mantiza)))
        self.exp=exponente
        self.mant=mantiza
        self.signo_expo=signo_expo
        self.signo_mant=signo_mant
    def index_exp(self,x):
        r= self.exp
        s=np.array(r)
        pos=list(s).index(x)
        return pos
    def index_mant(self,x):
        r= self.mant
        s=np.array(r)
        pos=list(s).index(x)
        return pos
    def getlenexp(self):
        return len(self.exp)
    def getlenmant(self):
        return len(self.mant)
    def imprimirObjeto(self):
        #imprimimos las caracteristicas del objeto
        print "\ntipo de dato:",self.tipo
        print "signo del exponente:",
        self.expo_signo()
        print "signo de la mantiza:",
        self.mant_signo()
        #imprimimos los datos que contiene el objeto
        print "exponentes:\n",self.exp
        print "mantizas:\n",self.mant
    def mant_signo(self):
        if self.signo_mant==1:
            self.temp_mantiza="MANTIZA: Negativa(-)"
        if self.signo_mant==0:
            self.temp_mantiza="MANTIZA: Positiva(+)"
        return self.temp_mantiza
    def expo_signo(self):
        if self.signo_expo==1:
            self.temp_signo="EXPONENTE: Negativo(-)"
        if self.signo_expo==0:
            self.temp_signo="EXPONENTE: Positivo(+)"
        return self.temp_signo
    def imprimirnumerosdemaquina(self):
        print "*******************************************************************************************************************"
        print "\n",self.expo_signo(),self.mant_signo(),"\n"
        print "*******************************************************************************************************************"
        for i in range(len(self.exp)):
            print "EXPONENTE: ",operaciones.exponentebin_base10(self.exp[i])
            for j in range(len(self.mant)):
                print "[",self.signo_expo,"]","[",self.signo_mant,"]",self.exp[i],self.mant[j]
