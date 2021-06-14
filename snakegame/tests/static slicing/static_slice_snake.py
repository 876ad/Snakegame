import curses
import random


run = True
playing = True
#score = 0

def collide_with_wall(snake):
    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw]:
        return 1
    else:
        return 0



def collide_with_self(snake):

    if snake[0] in snake[1:]:
        return 1
    else:
        return 0
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
        #snake body
        snake = [
            [snk_y, snk_x],
            [snk_y, snk_x-1],
            [snk_y, snk_x-2]
        ]

        key = curses.KEY_RIGHT

        while playing:
            next_key = w.getch()
            key = key if next_key == -1 else next_key


            new_head = [snake[0][0], snake[0][1]]

            if key == curses.KEY_DOWN:
                new_head[0] += 1
            if key == curses.KEY_UP:
                new_head[0] -= 1
            if key == curses.KEY_LEFT:
                new_head[1] -= 1
            if key == curses.KEY_RIGHT:
                new_head[1] += 1

            snake.insert(0, new_head)

            tail = snake.pop()
            w.addch(int(tail[0]), int(tail[1]), ' ')

            w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_LANTERN)

            if collide_with_self(snake) == 1:
                print('GAME OVER!')
                print('You ate yourself')
                
                run = False
                playing = False

            if collide_with_wall(snake) == 1:
                print('GAME OVER!')
                print('You hit a wall!')

                run = False
                playing= False
