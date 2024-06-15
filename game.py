import pgzrun
import random
WIDTH=400
HEIGHT=400
TITLE='ALIEN GAME'
message=''
alien=Actor('alien')
alien.pos=200,200
def draw():
    global message
    screen.fill('green')
    alien.draw()
    screen.draw.text(message, center=(300,20),color='orange', fontsize=40)

def placealien():
    alien.x=random.randint(50,350)
    alien.y=random.randint(50,350)

def on_mouse_down(pos):
    global message
    print(pos)
    if alien.collidepoint(pos): 
        placealien()
        message='Good Shot'
    else: 
        message='Try again'
    


pgzrun.go()