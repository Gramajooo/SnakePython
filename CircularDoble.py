import curses, os
from graphviz import Digraph, nohtml
class NodoDoble():
    def __init__(self, valor):
        self.sig = None
        self.ant = None
        self.valor = valor

class CircularDoble():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def estaVacia(self):
        return self.inicio is None

    def insertar_inicio(self, valor):
        nuevo = NodoDoble(valor)
        if self.estaVacia():
            nuevo.ant = self.fin
            nuevo.sig = self.inicio
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.inicio.ant = nuevo
            nuevo.sig = self.inicio
            self.inicio = nuevo
            self.fin.sig = nuevo
            self.inicio.ant = self.fin
        self.size += 1


    def obtener(self, index):
        tama = self.size
        if self.estaVacia():
            print("La lista esta vacia")
        else:
            actual = index
            if actual < 0:
                actual = tama
            elif actual > tama:
                actual = 0            
            temp = self.inicio
            contar = 0
            while(temp != None):
                if actual == contar:
                    window.addstr(13, 22, "                               ")
                    window.addstr(13,22,str("<- " + temp.valor + " ->"))
                temp = temp.sig
                if temp == self.fin.sig:
                    break
                contar +=1
    
    def prueba(self):
        temp = self.inicio
        posiy = 9
        while(temp != None):
            window.addstr(posiy,22,str(temp.valor))
            temp = temp.sig 
            posiy += 1
            if temp == self.fin.sig:
                break


    def graf2(self):      

        g = Digraph('CircularDoble', filename='grafica.dot', format='jpg' , node_attr={'shape': 'record', 'height': '.1'})
        temp = self.inicio
        while(temp != None):
            g.node(str(temp), nohtml('<f0> |<f1> ' + str(temp.valor) + '|<f2>'), )
            g.edge(str(temp), str(temp.sig))
            g.edge(str(temp), str(temp.ant))
            temp = temp.sig 
            if temp == self.fin.sig:
                break
                    
        g.save()
        os.system("dot grafica.dot -o imagen.jpg -Tjpg -Gcharset=utf8")

