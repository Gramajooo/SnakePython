import os
from graphviz import Digraph, nohtml

class NodoPi():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sig = None


class Pila():
    def __init__(self):
        self.cabeza = None

    def push(self,x,y):
        nuevo = NodoPi(x, y)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            nuevo.sig = self.cabeza
            self.cabeza = nuevo

    def impri(self):
        temp = self.cabeza
        if temp is None:
            print("La pila esta vacia")
        else:
            while temp is not None:                
                temp = temp.sig
                print(temp.x, ",", temp.y)

    def peek(self):
        if self.cabeza is None:
            print("Esta vacia")
        else:
            print("quitar: " + str(self.cabeza.x + "," + self.cabeza.y))

    def graf2(self):      

        g = Digraph('Pila', filename='grafica2.dot',  format='jpg' , node_attr={'shape': 'record', 'height': '.1'})
        temp = self.cabeza
        g.graph_attr['rankdir'] = 'LR'
        while(temp != None): 
                       
            g.node(str(temp), nohtml('<f0> |<f1> '+str(temp.x)+','+str(temp.y)+'|<f2>'))
            g.edge(str(temp),str(temp.sig))
            temp = temp.sig 
     
        g.save()
        os.system("dot grafica2.dot -o imagen2.jpg -Tjpg -Gcharset=utf8")
        



