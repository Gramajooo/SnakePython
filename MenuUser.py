import curses, os #import the curses library
from curses import KEY_UP

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

window.addstr(9,22,'1. New User')   
window.addstr(10,22,'2. Choose User')    

while key != 27:
    window.timeout(-2)    
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
curses.endwin()




     