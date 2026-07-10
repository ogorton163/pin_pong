from pygame import *

window = display.set_mode((700, 500))
display.set_caption("pig_pong")
window.fill((110,90,255))
cloc = time.Clock()

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    cloc.tick()
    display.update()