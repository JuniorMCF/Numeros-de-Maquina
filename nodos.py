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
        self.bits_expo=len(exponente[0])#
        self.bits_mantiza=len(mantiza[0])
        self.exp=exponente
        self.mant=mantiza
        self.signo_expo=signo_expo
        self.signo_mant=signo_mant
    def obtener_mantiza(self,pos):
        return self.mant[pos].tolist()
    def obtener_exponente(self,pos):
        return self.exp[pos].tolist()
    def getlenexp(self):
        return len(self.exp)
    def getlenmant(self):
        return len(self.mant)
    def index(self):
        if signo_mant==1 and signo_expo==0:
            return 0
        if signo_mant==1 and signo_expo==1:
            return 1
        if signo_mant==0 and signo_expo==1:
            return 2
        if signo_mant==0 and signo_expo==0:
            return 3
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
    def cantidad_de_numeros(self):
        return self.getlenexp()*self.getlenmant()
    def imprimirnumerosdemaquina(self):
        print "*******************************************************************************************************************"
        print "\n",self.mant_signo(),self.expo_signo(),"\n"
        print "*******************************************************************************************************************"
        for i in range(len(self.exp)):
            print "EXPONENTE: ",operaciones.exponentebin_base10(self.exp[i])
            for j in range(len(self.mant)):
                print "[",self.signo_mant,"]","[",self.signo_expo,"]",self.exp[i],self.mant[j]
