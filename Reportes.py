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

key = 0

window.addstr(9,22,'1. Snake Report')   
window.addstr(10,22,'2. Score Report')   
window.addstr(11,22,'3. Scoreboard Report')   
window.addstr(12,22,'4. Users Reports')   

while key != 27:
    window.timeout(-1)    
    opcion = window.getch()
    if opcion is not -1:  
        key = opcion        


    if opcion == ord('1'):
        os.system("imagen1.jpg")  
    if opcion == ord('2') :
        os.system("imagen2.jpg") 
    if opcion == ord('3'):
        os.system("imagen3.jpg") 
    if opcion == ord('4'):
        os.system("imagen4.jpg")      
    else:
        window.addstr(17,22,'Invalido')
        window.timeout(1000) 
        window.getch()
        window.addstr(17,22,'         ')





     