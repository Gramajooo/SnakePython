import curses, os 
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from graphviz import Digraph, nohtml
from random import randint, uniform,random
from ListaDoble import ListaDoble

lista = ListaDoble()

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
ranx = randint(2,57)
rany = randint(2,17)
window.addch(rany, ranx, '+') 
auxrx = randint(2,57)
auxry = randint(2,17)
window.addch(auxry, auxrx, '*') 

arreglo = []
for i in range(3):
    arreglo = [[pos_y,pos_x+i]]
    lista.insertar_inicio(arreglo)
    window.addch(pos_y, pos_x+i, '#')
pos_x = 7

while key != 27:                
    
    window.timeout(100)         
    keystroke = window.getch() 
    if keystroke is not  -1:    
        key = keystroke 

    if pos_x == ranx and pos_y == rany:           
        score +=1
        window.addstr(0,3," Score: " + str(score) + " ")
        ranx = randint(2,57)
        rany = randint(2,17)
        window.addch(rany, ranx, '+') 
        window.addch(auxry, auxrx, '*') 
        arreglo = [[pos_y, pos_x+1]] 
        lista.insertar_inicio(arreglo)
    if pos_x == auxrx and pos_y == auxry:           
        score -=1
        window.addstr(0,3," Score: " + str(score) + " ")
        auxrx = randint(2,57)
        auxry = randint(2,17)
        window.addch(auxry, auxrx, '*')
        if score < 0:
            os.system("python GameOver.py")  
        if lista.getSize() > 3:
            aux = lista.getFinal()
            aux2 = aux[0]
            window.addch(aux2[0], aux2[1], " ")     
            lista.eliminarCola() 
        
    if pos_x == 1:           #Izquierda
        pos_x = 57    
    if pos_x == 58:           #Derecha   
        pos_x = 1 
    if pos_y == 1:            #Arriba
        pos_y = 17
    if pos_y == 18:            #Abajo 
        pos_y = 1
        
    if key == KEY_RIGHT: 
        pos_x +=1                
        arreglo = [[pos_y, pos_x]]         
        lista.insertar_inicio(arreglo)
        window.addch(pos_y,pos_x,'#') 
        aux = lista.getFinal()
        aux2 = aux[0]
        window.addch(aux2[0], aux2[1], " ")     
        lista.eliminarCola()
    elif key == KEY_LEFT:               
        pos_x -=1                
        arreglo = [[pos_y, pos_x]]         
        lista.insertar_inicio(arreglo)
        window.addch(pos_y,pos_x,'#') 
        aux = lista.getFinal()
        aux2 = aux[0]
        window.addch(aux2[0], aux2[1], " ") 
        lista.eliminarCola()                
    elif key == KEY_UP:                 
        pos_y -=1                
        arreglo = [[pos_y, pos_x]]         
        lista.insertar_inicio(arreglo)
        window.addch(pos_y,pos_x,'#') 
        aux = lista.getFinal()
        aux2 = aux[0]
        window.addch(aux2[0], aux2[1], " ")
        lista.eliminarCola()                   
    elif key == KEY_DOWN:               
        pos_y +=1                
        arreglo = [[pos_y, pos_x]]         
        lista.insertar_inicio(arreglo)
        window.addch(pos_y,pos_x,'#') 
        aux = lista.getFinal()
        aux2 = aux[0]
        window.addch(aux2[0], aux2[1], " ")  
        lista.eliminarCola()          


lista.graf2()