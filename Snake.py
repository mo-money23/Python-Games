from numpy import append
import pygame as pg
import time  
import random

pg.init()

wht = (255,255,255)
blk = (0,0,0)
gr = (0,255,0)
rd = (255,0,0)
bl = (0,0,255)

win_w = 600
win_h = 400
win = pg.display.set_mode((win_w,win_h))
pg.display.set_caption('Snake Game by ur Dad')

clock = pg.time.Clock()

snk_block = 10
snk_speed = 20

font_style = pg.font.SysFont("bahnschrift", 20)
score_font = pg.font.SysFont("comicsansms", 30)

def urScore(score):
    val = score_font.render("Your Score: " + str(score), True, bl)
    win.blit(val, [0,0])


def ourSnake(snk_block, snk_lst):
    for i in snk_lst:
        pg.draw.rect(win, gr, [i[0], i[1], snk_block, snk_block])
        

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [win_w/11,win_h/3])
    
def gameLoop():
    gameOver = False
    gameClose = False
    
    x1 = win_w/2
    y1 = win_h/2
    
    x1_change = 0
    y1_change = 0
    
    snk_list = []
    length_snk = 1
    
    foodx = round(random.randrange(0, win_w - snk_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_h - snk_block) / 10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            win.fill(wht)
            message("L bro get good! Press Q to quit or C to try again lol", rd)
            pg.display.update()
            
            for i in pg.event.get():
                if i.type == pg.KEYDOWN:
                    if i.key == pg.K_q:
                        gameOver = True
                        gameClose = False
                    if i.key == pg.K_c:
                        gameLoop()
            
            
        for i in pg.event.get():
            if i.type == pg.QUIT:
                gameOver = True
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_LEFT:
                    x1_change = -snk_block
                    y1_change = 0
                elif i.key == pg.K_RIGHT:
                    x1_change = snk_block
                    y1_change = 0
                elif i.key == pg.K_UP:
                    x1_change = 0
                    y1_change = -snk_block
                elif i.key == pg.K_DOWN:
                    x1_change = 0
                    y1_change = snk_block
        if x1 >= win_w or x1 < 0 or y1 >= win_h or y1 < 0:
            gameClose = True
                
        x1 += x1_change
        y1 += y1_change
        win.fill(blk)
        pg.draw.rect(win,rd,[foodx,foody,snk_block,snk_block])
        snk_head = []
        snk_head.append(x1)
        snk_head.append(y1)
        snk_list.append(snk_head)
        if len(snk_list) > length_snk:
            del snk_list[0]
            
        for i in snk_list[:-1]:
            if i == snk_head:
                gameClose = True
                
        
        ourSnake(snk_block, snk_list)
        urScore(length_snk - 1)
        
        pg.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_w - snk_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_h - snk_block) / 10.0) * 10.0
            length_snk += 1
        
        clock.tick(snk_speed)
    
    pg.quit()
    quit()
    
gameLoop()