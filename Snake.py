import curses, os #import the curses library
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library
from graphviz import Digraph, nohtml
from random import randint, uniform,random

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
#lista.insertar_inicio(100)

#OBTENER EL VALOR DE ELEMENTO DE LA LISTA
#lista.obtener(3)

#ELIMINAR POR POSICION
#lista.eliminar(7)

#GRAFICAR
#lista.graf2()


stdscr = curses.initscr() 
height = 20
width = 60
pos_y = 0
pos_x = 0
window = curses.newwin(height, width, pos_y, pos_x) 
window.keypad(True)     
curses.noecho()         
curses.curs_set(0)      
window.border(0)        
window.nodelay(True)    

key = KEY_RIGHT         
pos_x = 5               
pos_y = 5               

score = 0 
user = "Jimena-chan"

window.addstr(0,3," Score: " + str(score) + " ")  
window.addstr(0,17," SNAKE RELOADED ")  
window.addstr(0,37," User: " + user + " ")  
window.addch(pos_y,pos_x,'#')   
ranx = randint(5,55)
rany = randint(5,17)
window.addch(rany, ranx, '+') 

comiendo = 3


cabezax=0
cabezay=0
while key != 27:                
    
    window.timeout(1000)         
    keystroke = window.getch() 
    if keystroke is not  -1:    
        key = keystroke 

    if pos_x == ranx and pos_y == rany:           
        score +=1
        window.addstr(0,3," Score: " + str(score) + " ")
        ranx = randint(2,55)
        rany = randint(2,17)
        window.addch(rany, ranx, '+') 
        comiendo +=1
    if pos_x == 0 and pos_y > 0 :           #Izquierda
        window.addch(pos_y, pos_x, '|') 
        pos_x = 58    
    if pos_x == 59 and pos_y > 0:           #Derecha
        window.addch(pos_y, pos_x, '|')       
        pos_x = 2 
    if pos_x >0 and pos_y == 19:            #Abajo
        window.addch(pos_y, pos_x, '-') 
        pos_y = 2
    if pos_y == 0 and pos_x > 0:            #Arriba
        window.addch(pos_y, pos_x, '-')
        window.addstr(0,3," Score: " + str(score) + " ")  
        window.addstr(0,17," SNAKE RELOADED ")  
        window.addstr(0,37," User: " + user + " ")  
        pos_y = 18

    for i in range(comiendo): 
        if key == KEY_LEFT or key == KEY_RIGHT:
            window.addch(pos_y,pos_x+i,' ')
            window.addch(pos_y,pos_x-i,' ') 
        if key == KEY_UP or key == KEY_DOWN:
            window.addch(pos_y+i,pos_x,' ') 
            window.addch(pos_y-i,pos_x,' ')    
        
    if key == KEY_RIGHT:                
        pos_x = pos_x + 1               
    elif key == KEY_LEFT:               
        pos_x = pos_x - 1               
    elif key == KEY_UP:                 
        pos_y = pos_y - 1               
    elif key == KEY_DOWN:               
        pos_y = pos_y + 1
    for i in range(comiendo):
        if key == KEY_LEFT:
            window.addch(pos_y,pos_x+i,'#')
        if key == KEY_RIGHT:
            window.addch(pos_y,pos_x-i,'#')
        if key == KEY_UP:
            window.addch(pos_y+i,pos_x,'#')  
        if key == KEY_DOWN:
            window.addch(pos_y-i,pos_x,'#')             

