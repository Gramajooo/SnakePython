import curses, os #import the curses library
from curses import KEY_UP
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


lista = CircularDoble()

#INSERCIONES AL INICIO
lista.insertar_inicio(str("Jimena-chan"))
lista.insertar_inicio(str("Dylan"))
lista.insertar_inicio(str("Shiro"))
lista.insertar_inicio(str("Valentina"))
lista.insertar_inicio(str("Phospholite"))

#lista.graf2()

#lista.obtener()
        

stdscr = curses.initscr() #initialize console
height = 25
width = 65
pos_y = 0
pos_x = 0
window = curses.newwin(height, width, pos_y, pos_x) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.start_color()
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
window.border(0)        #default border for our window
window.nodelay(True)    #return -1 when no key is pressed

key = KEY_UP

while key != 27:
    lista.prueba()
    window.timeout(-2)    
    opcion = window.getch()
    if opcion is not -1:  
        key = opcion  
curses.endwin()





