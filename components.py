# components.py
import random

from ursina import *
import time

class Circle(Entity):
    def __init__(
            self,
            offset=Vec2(1, 1),
            scale_offset=Vec2(1, 1),
            color=color.gray,
            debug=False
    ):
        super().__init__(
            model='quad',
            scale=(
                random.random() * scale_offset[0],
                random.random() * scale_offset[1]

            ),
            position=(
                random.random() * offset[0],
                random.random() * offset[1]
            ),
            color=color,
            alpha=0.6
        )
        if debug:
            self.texture = 'circle_02.png'
        else:
            self.texture = 'circle_02.png'
        self.origin = (0, 0.4, 0)
        self.z = 30.001

class CircleGenerate(Entity):
    def __init__(self,debug=False, **kwargs):
        super().__init__()
        self.aniLast = time.time()
        self.loops = 0
        self.max = 100

        self.debug = debug

    def update(self):
        for i in range(5):
            Circle(
                offset=Vec2(20, 20),
                scale_offset=Vec2(150, 150),
                debug=self.debug
            )
        self.aniLast = time.time()
        self.loops += 1
        if self.loops >= self.max:
            destroy(self)
            return


class CodeText(Entity):
    def __init__(self):
        super().__init__()
        self.main_text = Text(
            text=open('./main.py','r').read(),
            alpha=0.2,
            parent=Entity(),
            position=(random.uniform(-1, -0.5), random.uniform(0.4, 0.2))
        )
        self.components = Text(
            text=open('./components.py','r').read(),
            alpha=0.2,
            parent=Entity(),
            position=(random.uniform(0,0.5),random.uniform(0.4,0.2))
        )
        self.github = Text(
            text='open source on https://github.com/4Tudo/Readme_non0x00',
            alpha=0.4,
            parent=Entity(),
            position=(random.uniform(0,0.1),random.uniform(0.3,0))
        )
    def input(self,event):
        if event == 'space':
            CodeText()
            destroy(self.main_text)
            destroy(self.components)
            destroy(self.github)
            destroy(self)

if __name__ == '__main__':
    app = Ursina()
    camera.z = -4
    CodeText()
    app.run()