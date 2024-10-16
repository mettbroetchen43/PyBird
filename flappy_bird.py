from ursina import *

app = Ursina()
Sky()
bird = Animation('assets/bird_blue', scale=2, collider='box')

camera.orthographic = True
camera.fov = 30

def update():
    bird.y = bird.y - 0.07
    for pipe in pipes:
        pipe.x = pipe.x - 0.05
    if bird.y < -10 or bird.y > 10 or bird.intersects().hit:
        quit() 

def input(key):
    if key == 'space':
        bird.y = bird.y + 2

    if key == 'q':
        quit()

pipes = []

pipe = Entity(model='quad', 
              color=color.green, 
              texture='white_cube',
              position=(20, 10),
              scale=(3, 15, 1),
              collider='box')

def createPipes():
    newY = random.randint(4, 12)
    newPipe = duplicate(pipe, y=newY)
    newPipe2 = duplicate(pipe, y=newY-23)
    pipes.append(newPipe)
    pipes.append(newPipe2)
    invoke(createPipes, delay=5)
    
    
createPipes()
app.run()
