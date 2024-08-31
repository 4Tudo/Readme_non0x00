import time

from ursina import *
from direct.filter.CommonFilters import CommonFilters
from components import *
app = Ursina()

window.color = color.black

window.fps_counter.visible = False
window.entity_counter.visible = False
window.exit_button.visible = False
window.collider_counter.visible = False
window.fullscreen = True

filters = CommonFilters(app.win,app.cam)
filters.set_msaa(samples=128)
filters.set_bloom(size='large',intensity=1,blend=(0.6,0.8,0.6,0))

name = Text(
    text='NoName',
    parent=Entity(model='quad',alpha=0),
    x=-1+abs(0.6--1)/2,
    y=-0.5+1/2+0.05,
    scale=4,
)
sub = Text(
    text='0x00',
    parent=Entity(model='quad',alpha=0),
    x=-1+abs(0.6--1)/2+0.15,
    y=-0.5+1/2+0.05-0.1,
    scale=2,
)
hobbies = Text(
    text='Codes | Games | Decorations ',
    parent=Entity(model='quad',alpha=0),
    x=-1+abs(0.6--1)/2-0.13,
    y=-0.5+1/2+0.05-0.15,
    scale=2,
)

for i in range(50):
    Entity(
        model='quad',
        texture='square_01.png',
        scale=2.5-i/10,
        rotation=(0,0,360/50*i),
        alpha=i/8,
    )
for i in range(50):
    Entity(
        model='quad',
        texture='circle_01.png',
        scale=2.5-i/10,
        rotation=(0,0,360/50*i),
        alpha=i/3,
    )


camera.z = -4
shot = False
last = time.time()
def update():
    global shot
    print(f'Loading scene: {len(scene.entities)} | {int(len(scene.entities)/126*100)}%')
    if len(scene.entities)/126 >= 1 and not shot and time.time() >= last + 10:
        print('output')
        app.screenshot()
        shot = True
app.run()