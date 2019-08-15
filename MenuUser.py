import curses, os 
from curses import KEY_UP

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

key = KEY_UP

window.addstr(9,22,'1. New User')   
window.addstr(10,22,'2. Choose User')    

while key != 27:
    window.timeout(-1)    
    opcion = window.getch()
    if opcion is not -1:  
        key = opcion        

    if opcion == ord('1'):
        os.system("python Snake.py")        
    elif opcion == ord('2'):
        os.system("python Usuarios.py")  
    else:
        window.addstr(17,22,'Invalido')
        window.timeout(1000) 
        window.getch()
        window.addstr(17,22,'         ')





     