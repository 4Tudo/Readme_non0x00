# main.py
from ursina import *
from components import *
from direct.filter.CommonFilters import CommonFilters

app = Ursina()
window.color = color.black
filters = CommonFilters(app.win,app.cam)
filters.set_msaa(samples=100)
filters.set_bloom(size='large')
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
CircleGenerate()
camera.z = -3

def update():
    print(f'Loading scene: {len(scene.entities)} | {int(len(scene.entities)/576*100)}%')

app.run()