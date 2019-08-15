import curses, os, csv 
from curses import KEY_UP
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

key = 0

window.addstr(9,22,'1. Play')   
window.addstr(10,22,'2. Scoreboard')   
window.addstr(11,22,'3. User Selection')   
window.addstr(12,22,'4. Reports')   
window.addstr(13,22,'5. Bulk Loading')  

while key != 27:
    window.timeout(-1)    
    opcion = window.getch()
    if opcion is not -1:  
        key = opcion        

    if opcion == ord('1'):
        os.system("python Snake.py")        
    elif opcion == ord('2'):
        window.addstr(17,22,'                           ')
        #os.system("python Scoreboard.py")
    elif opcion == ord('3'):
        os.system("python Usuarios.py")  
    elif opcion == ord('4'):
        os.system("python Reportes.py")
    elif opcion == ord('5'):
        lista.cargamasiva()
        window.addstr(17,22,'Cargado correctamente')
        window.timeout(1000) 
        window.getch()
        window.addstr(17,22,'                           ')
    else:
        window.addstr(17,22,'Invalido')
        window.timeout(1000) 
        window.getch()
        window.addstr(17,22,'         ')

curses.endwin()





     