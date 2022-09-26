import pygame, sys, random, time
from pygame.locals import *
SCREEN_RECT = Rect(0, 0,640, 480)
a =[[0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0],
    [0,0,0,2,1,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]
l =[[[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]]
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RECT.size)
    pygame.display.set_caption("わーい、オセロだぁ～")
    clock = pygame.time.Clock()
    j,g,k,f,y,u,r = 0,0,0,0,0,0,0
    while True:
        clock.tick(10)
        screen.fill((0,0,100))
        font = pygame.font.SysFont("hg正楷書体pro", 30)
        if k == 0:
            text1 = font.render("黒のターン", True, (255,255,255))
        if k == 1:
            text1 = font.render("白のターン", True, (255,255,255))
        text3 = font.render("VS 人", True, (255,255,255))
        text4 = font.render("VS com(笑)", True, (255,255,255))
        screen.blit(text3, (300, 300))
        screen.blit(text4, (300, 350))
        pygame.draw.rect(screen,(255,255,255),Rect(300,300,170,30),1)
        pygame.draw.rect(screen,(255,255,255),Rect(300,350,170,30),1)
        pygame.draw.rect(screen,(255,255,255),Rect(5,5,240,240),1)
        pygame.draw.rect(screen,(255,255,255),Rect(35,5,180,240),1)
        pygame.draw.rect(screen,(255,255,255),Rect(65,5,120,240),1)
        pygame.draw.rect(screen,(255,255,255),Rect(95,5,60,240),1)
        pygame.draw.rect(screen,(255,255,255),Rect(125,5,1,240),1)
        pygame.draw.rect(screen,(255,255,255),Rect(5,5,240,240),1)
        pygame.draw.rect(screen,(255,255,255),Rect(5,35,240,180),1)
        pygame.draw.rect(screen,(255,255,255),Rect(5,65,240,120),1)
        pygame.draw.rect(screen,(255,255,255),Rect(5,95,240,60),1)
        pygame.draw.rect(screen,(255,255,255),Rect(5,125,240,1),1)
        pygame.draw.rect(screen,(255,255,255),Rect(5,5,240,240),1)
        x,w = 0,0
        for i in range(8):
            for v in range(8):
                l[i][v] = [0,0,0,0,0,0,0,0]
                if a[i][v] == 0:
                    for p in range(8):
                        if p == 0:
                            q = v
                        elif p == 1:
                            q = 7-v
                        elif p == 2:
                            q = i
                        elif p == 3:
                            q = 7-i
                        elif p == 4:
                            if i > v:
                                q = v
                            if i <= v:
                                q = i
                        elif p == 5:
                            if i > 7-v:
                                q = 7-v
                            if i <= 7-v:
                                q = i
                        elif p == 6:
                            if i < v:
                                q = 7-v
                            if i >= v:
                                q = 7-i
                        elif p == 7:
                            if 7-i > v:
                                q = v
                            if 7-i <= v:
                                q = 7-i
                        for e in range(q):
                            if p == 0:
                                f = a[i][v-1-e]
                            elif p == 1:
                                f = a[i][v+1+e]
                            elif p == 2:
                                f = a[i-1-e][v]
                            elif p == 3:
                                f = a[i+1+e][v]
                            elif p == 4:
                                f = a[i-1-e][v-1-e]
                            elif p == 5:
                                f = a[i-1-e][v+1+e]
                            elif p == 6:
                                f = a[i+1+e][v+1+e]
                            elif p == 7:
                                f = a[i+1+e][v-1-e]
                            if k == 0:
                                if f == 0:
                                    break
                                if f == 2:
                                    g += 1
                                if f == 1:
                                    j = 1
                                    break
                            if k == 1:
                                if f == 0:
                                    break
                                if f == 2:
                                    j = 1
                                    break
                                if f == 1:
                                    g += 1
                        if g >= 1 and j == 1:
                            l[i][v][p] = g
                        g,j = 0,0
                if a[i][v] == 0:
                    pygame.draw.rect(screen,(0,255,0),Rect(6+30*v,6+30*i,28,28))
                if a[i][v] == 1:
                    pygame.draw.rect(screen,(0,0,0),Rect(6+30*v,6+30*i,28,28))
                    w += 1
                if a[i][v] == 2:
                    pygame.draw.rect(screen,(255,255,255),Rect(6+30*v,6+30*i,28,28))
                    x += 1
                if not l[i][v] == [0,0,0,0,0,0,0,0]:
                    pygame.draw.rect(screen,(255,0,0),Rect(17+30*v,17+30*i,5,5))
        if l == [[[0]*8]*8]*8:
            if k == 0:
                k = 1
                y += 1
            elif k == 1:
                k = 0
                y += 1
            if y >= 2:
                text1 = font.render("黒 "+str(w)+" 白 "+str(x), True, (255,255,255))
                if w > x:
                    v = "黒 win"
                if w == x:
                    v = "draw"
                if w < x:
                    v = "白 win"
                text2 = font.render(v, True, (255,255,255))
                screen.blit(text2, (300, 150))
        screen.blit(text1, (300, 100))
        pygame.display.update()
        if u == 1 and k == 1:
            c = random.randint(0,7)
            b = random.randint(0,7)
            if not l[c][b] == [0,0,0,0,0,0,0,0]:
                time.sleep(0.2)
                a[c][b] = 2
                for d in range(l[c][b][0]):
                    a[c][b-1-d] = 2
                for d in range(l[c][b][1]):
                    a[c][b+1+d] = 2
                for d in range(l[c][b][2]):
                    a[c-1-d][b] = 2
                for d in range(l[c][b][3]):
                    a[c+1+d][b] = 2
                for d in range(l[c][b][4]):
                    a[c-1-d][b-1-d] = 2
                for d in range(l[c][b][5]):
                    a[c-1-d][b+1+d] = 2
                for d in range(l[c][b][6]):
                    a[c+1+d][b+1+d] = 2
                for d in range(l[c][b][7]):
                    a[c+1+d][b-1-d] = 2
                k = 0
                y = 0
                r = 0
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 300 < event.pos[0] < 470 and 300 < event.pos[1] < 330:
                        u = 0
                    if 300 < event.pos[0] < 470 and 350 < event.pos[1] < 380:
                        u = 1
                    if not (k == 1 and u == 1):
                        b,z = divmod(event.pos[0]-5,30)
                        c,z = divmod(event.pos[1]-5,30)
                    if 0 <= b <= 7 and 0 <= c <= 7 and k == 0 and r == 0:
                        if not l[c][b] == [0,0,0,0,0,0,0,0]:
                            a[c][b] = 1
                            for d in range(l[c][b][0]):
                                a[c][b-1-d] = 1
                            for d in range(l[c][b][1]):
                                a[c][b+1+d] = 1
                            for d in range(l[c][b][2]):
                                a[c-1-d][b] = 1
                            for d in range(l[c][b][3]):
                                a[c+1+d][b] = 1
                            for d in range(l[c][b][4]):
                                a[c-1-d][b-1-d] = 1
                            for d in range(l[c][b][5]):
                                a[c-1-d][b+1+d] = 1
                            for d in range(l[c][b][6]):
                                a[c+1+d][b+1+d] = 1
                            for d in range(l[c][b][7]):
                                a[c+1+d][b-1-d] = 1
                            k = 1
                            y = 0
                            r = 1
                    elif 0 <= b <= 7 and 0 <= c <= 7 and k == 1 and r == 0:
                        if not l[c][b] == [0,0,0,0,0,0,0,0]:
                            a[c][b] = 2
                            for d in range(l[c][b][0]):
                                a[c][b-1-d] = 2
                            for d in range(l[c][b][1]):
                                a[c][b+1+d] = 2
                            for d in range(l[c][b][2]):
                                a[c-1-d][b] = 2
                            for d in range(l[c][b][3]):
                                a[c+1+d][b] = 2
                            for d in range(l[c][b][4]):
                                a[c-1-d][b-1-d] = 2
                            for d in range(l[c][b][5]):
                                a[c-1-d][b+1+d] = 2
                            for d in range(l[c][b][6]):
                                a[c+1+d][b+1+d] = 2
                            for d in range(l[c][b][7]):
                                a[c+1+d][b-1-d] = 2
                            k = 0
                            y = 0
                            r = 1
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
if __name__ == '__main__':
    main()