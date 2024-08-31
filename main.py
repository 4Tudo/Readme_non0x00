# awa
# main.py
from ursina import *
from components import *
from direct.filter.CommonFilters import CommonFilters

app = Ursina()
window.color = color.black

window.fps_counter.visible = False
window.entity_counter.visible = False
window.exit_button.visible = False
window.collider_counter.visible = False
window.fullscreen = True

filters = CommonFilters(app.win,app.cam)
filters.set_msaa(samples=128)   # 128x WTF?!
filters.set_bloom(size='large',intensity=1,blend=(0.6,0.8,0.6,0))
# EditorCamera()
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

circle1 = Entity(
    model='quad',
    texture='circle_01.png',
    scale=3
)
black_hold = Entity(
    model='quad',
    texture='bh_x4.png',
    scale=30,
    z=30
)
for i in range(50):
    Entity(
        model='quad',
        texture='square_01.png',
        scale=2.5,
        rotation=(0,0,360/50*i),
        alpha=i/10
    )

class Letterbox(Entity):
    def __init__(self,type):
        super().__init__()
        self.model='quad'
        self.color=color.black
        if type == 'upper':
            self.y = 2
        if type == 'under':
            self.y = -2
        self.scale = (18,3.2)
        self.state = 'up'
        self.loop = 2
        self.aniLast = time.time()
        self.z = 0

lb1 = Letterbox(type='under')
lb2 = Letterbox(type='upper')


CircleGenerate()
camera.z = -3
CodeText()
shot = False
def update():
    global shot
    print(f'Loading scene: {len(scene.entities)} | {int(len(scene.entities)/585*100)}%')
    if len(scene.entities)/585 >= 1 and not shot:
        print('output')
        app.screenshot()
        shot = True

app.run()