from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Game")
background = transform.scale(image.load("background.jpg"), (700, 500))
sprite1 = transform.scale(image.load('ch1.png'),(100, 100))
sprite2 = transform.scale(image.load('ch2.png'),(100, 100))
clock = time.Clock()
FPS = 60
game = True
x1 = 100
y1 = 100
x2 = 200
y2 = 200
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        y1 -= 10
    if keys_pressed[K_s] and y2 < 395:
        y2 += 10
    if keys_pressed[K_DOWN]:
        y1 += 10
    if keys_pressed[K_w] and y2 < 395:
        y2 -= 10
    if keys_pressed[K_LEFT]:
        x1 -= 10
    if keys_pressed[K_a] and y2 < 395:
        x2 -= 10
    if keys_pressed[K_RIGHT]:
        x1 += 10
    if keys_pressed[K_d] and y2 < 395:
        x2 += 10
    display.update()
    clock.tick(FPS)
    
    
    