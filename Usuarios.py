import curses, os #import the curses library
from curses import KEY_UP
from graphviz import Digraph, nohtml
from CircularDoble import CircularDoble

lista = CircularDoble()
lista = lista.getLista()


stdscr = curses.initscr() 
height = 25
width = 65
pos_y = 0
pos_x = 0
window = curses.newwin(height, width, pos_y, pos_x) 
window.keypad(True)     
curses.start_color()
curses.noecho()         
curses.curs_set(0)      
window.border(0)        
window.nodelay(True)    
nickname = ""
key = KEY_UP

window.addstr(5,10,"Presione key-up para seleccionar un usuario")
window.addstr(13,10,"<--")
window.addstr(13,50,"-->")
if lista.estaVacia():
    window.addstr(13,25,"La lista esta vacia")
else:    
    temp = lista.getInicio()
    window.addstr(13,25,str(temp.valor))
    temp = temp.sig
    while key != 27:    
        window.timeout(-1)    
        opcion = window.getch()
        if opcion == curses.KEY_UP: 
            nickname = temp.valor
            print(nickname)
            key = 27
        if opcion is not -1:  
            key = opcion  
        if lista.estaVacia():
            window.addstr(13,25,"La lista esta vacia")
        else:    
            window.addstr(13, 25, "               ")
            window.addstr(13,25,str(temp.valor))
            if opcion == curses.KEY_RIGHT:
                temp = temp.sig
            if opcion == curses.KEY_LEFT:
                temp = temp.ant
    

    
   





