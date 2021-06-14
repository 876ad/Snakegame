import curses
import random


run = True
playing = True

while run:

    if playing:
        #curses initialize screen
        s = curses.initscr()
        #cursor invisible
        curses.curs_set(0)
        #width and height
        sh, sw = s.getmaxyx()
        #create window
        w = curses.newwin(sh, sw, 0, 0)
        #take input
        w.keypad(1)
        w.timeout(100)

        snk_x = sw/4
        snk_y = sh/2
        
