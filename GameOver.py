import curses, os 

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
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

z=2
window.addstr(3,2, "     ##########      #       ######      #######  ##########", curses.color_pair(z) | curses.A_BOLD)
window.addstr(4,2, "   ###########      ##      #######    ########  ##########", curses.color_pair(z) | curses.A_BOLD)
window.addstr(5,2, "  ####            ####     ########  #########  ####      ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(6,2, " #### ######    ##  ##    ####  #######  ####  ##########", curses.color_pair(z) | curses.A_BOLD)
window.addstr(7,2, "####   ####   ########   ####   #####   ####  ####      ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(8,2, "##########  ###    ###  ####           ####  ##########", curses.color_pair(z) | curses.A_BOLD)
window.addstr(9,2, " ######## ###      ### ####           ####  ##########", curses.color_pair(z) | curses.A_BOLD)

window.addstr(12,2, "       #######    ####     #### ##########  ########    ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(13,2, "     #########   ####    ####  ##########  ##########  ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(14,2, "   ####   ####  ####   ####   ####        ####   #### ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(15,2, "  ####   ####  ####  ####    ##########  ########### ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(16,2, " ####   ####  #### ####     ####        #########   ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(17,2, " #########   ########      ##########  ####   #### ", curses.color_pair(z) | curses.A_BOLD)
window.addstr(18,2, "  ######    ######        ##########  ####   #### ", curses.color_pair(z) | curses.A_BOLD)



while key != 27:
    z=3
    window.timeout(100)    
    opcion = window.getch()
    window.addstr(3,2, "     ##########      #       ######      #######  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(4,2, "   ###########      ##      #######    ########  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(5,2, "  ####            ####     ########  #########  ####      ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(6,2, " #### ######    ##  ##    ####  #######  ####  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(7,2, "####   ####   ########   ####   #####   ####  ####      ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(8,2, "##########  ###    ###  ####           ####  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(9,2, " ######## ###      ### ####           ####  ##########", curses.color_pair(z) | curses.A_BOLD)

    window.addstr(12,2, "       #######    ####     #### ##########  ########    ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(13,2, "     #########   ####    ####  ##########  ##########  ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(14,2, "   ####   ####  ####   ####   ####        ####   #### ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(15,2, "  ####   ####  ####  ####    ##########  ########### ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(16,2, " ####   ####  #### ####     ####        #########   ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(17,2, " #########   ########      ##########  ####   #### ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(18,2, "  ######    ######        ##########  ####   #### ", curses.color_pair(z) | curses.A_BOLD) 
    if opcion is not -1:  
        key = opcion 
          
           
    window.timeout(100)    
    window.getch() 
    z=2
    window.addstr(3,2, "     ##########      #       ######      #######  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(4,2, "   ###########      ##      #######    ########  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(5,2, "  ####            ####     ########  #########  ####      ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(6,2, " #### ######    ##  ##    ####  #######  ####  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(7,2, "####   ####   ########   ####   #####   ####  ####      ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(8,2, "##########  ###    ###  ####           ####  ##########", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(9,2, " ######## ###      ### ####           ####  ##########", curses.color_pair(z) | curses.A_BOLD)

    window.addstr(12,2, "       #######    ####     #### ##########  ########    ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(13,2, "     #########   ####    ####  ##########  ##########  ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(14,2, "   ####   ####  ####   ####   ####        ####   #### ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(15,2, "  ####   ####  ####  ####    ##########  ########### ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(16,2, " ####   ####  #### ####     ####        #########   ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(17,2, " #########   ########      ##########  ####   #### ", curses.color_pair(z) | curses.A_BOLD)
    window.addstr(18,2, "  ######    ######        ##########  ####   #### ", curses.color_pair(z) | curses.A_BOLD)

os.system("python Menu.py")  