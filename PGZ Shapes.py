import pgzrun

WIDTH = 800
HEIGHT = 600

def draw():
    screen.fill("red")
    r1 = Rect((150,150) ,(400,200))
    screen.draw.rect(r1,"Green")
    screen.draw.circle((400,300),50,"yellow") 
    r2 = Rect((150,75),(200,200))
    screen.draw.filled_rect(r2,"white")
    screen.draw.line((200,200) ,(400,200),"brown")
pgzrun.go()