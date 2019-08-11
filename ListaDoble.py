
import os
from graphviz import Digraph, nohtml

class NodoDoble():
    def __init__(self, valor):
        self.sig = None
        self.ant = None
        self.valor = valor

class ListaDoble():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def estaVacia(self):
        return self.inicio is None

    def insertar_final(self, valor):
        nuevo = NodoDoble(valor)
        if self.estaVacia():
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.fin.sig = nuevo
            nuevo.ant = self.fin
            self.fin = nuevo
        self.size +=1

    def insertar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if self.estaVacia():
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.inicio.ant = nuevo
            nuevo.sig = self.inicio
            self.inicio = nuevo
        self.size += 1

    def insertar_pos(self, index, valor):
        nuevo = NodoDoble(valor)
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            if index >= 0 and index <= self.size:
                temp = self.inicio
                contar = 0
                if index == 0:
                    self.insertar_inicio(valor)
                    self.size +=1
                else:
                    if index == self.size-1:
                        self.insertar_final(valor)
                        self.size +=1
                    else:
                        while(temp.sig != None):   
                            if contar == index:
                                nuevo.ant = temp.ant
                                temp.ant.sig = nuevo
                                nuevo.sig = temp
                                temp.ant = nuevo                              
                                self.size += 1
                            temp = temp.sig
                            contar += 1
            else:
                print("Invalido")
    
    def eliminar(self, index):
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            if index >= 0 and index <= self.size:
                temp = self.inicio
                contar = 0
                if index == 0:
                        self.inicio = self.inicio.sig
                        self.inicio.ant = None
                        self.size -= 1
                else:
                    if index == self.size-1:
                        self.fin = self.fin.ant
                        self.fin.sig = None
                        self.size -= 1
                    while(temp.sig != None):   
                        if contar == index:
                            temp.sig.ant = temp.ant
                            temp.ant.sig = temp.sig
                            self.size -= 1
                        temp = temp.sig
                        contar += 1
                    
            else:
                print("Invalido")

    def obtener(self, index):
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            temp = self.inicio
            contar = 0
            while(temp != None):
                if index == contar:
                    print(temp.valor)
                temp = temp.sig
                contar +=1


    def graf2(self):      

        g = Digraph('ListaDoble', filename='grafica.dot', format='jpg' , node_attr={'shape': 'record', 'height': '.1'})
        temp = self.inicio
        while(temp != None):
            g.node(str(temp), nohtml('<f0> |<f1> '+str(temp.valor)+'|<f2>'))
            g.edge(str(temp),str(temp.sig))
            g.edge(str(temp),str(temp.ant))
            temp = temp.sig 
     
        g.save()
        os.system("dot grafica.dot -o imagen.jpg -Tjpg -Gcharset=utf8")


lista = ListaDoble()

#INSERCIONES AL INICIO
lista.insertar_inicio(100)
lista.insertar_inicio(200)
lista.insertar_inicio(300)
lista.insertar_inicio(400)
lista.insertar_inicio(500)

#INSERCIONES AL FINAL
lista.insertar_final(10)
lista.insertar_final(20)
lista.insertar_final(30)
lista.insertar_final(40)
lista.insertar_final(50)

#GRAFICAR
lista.graf2()

#INSERTAR EN POSICION
lista.insertar_pos(3,777)
lista.insertar_pos(8,999)

#GRAFICAR
lista.graf2()

#OBTENER EL VALOR DE ELEMENTO DE LA LISTA
lista.obtener(3)

#ELIMINAR POR POSICION
lista.eliminar(7)

#GRAFICAR
lista.graf2()


