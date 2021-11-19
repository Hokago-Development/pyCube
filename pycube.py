from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
from random import randint

game = Ursina()
window.borderless = False
window.exit_button.enabled = False

noise = PerlinNoise(octaves=3, seed=randint(1,1000000000))

# block class
class Voxel(Button):
    def __init__(self, position):
        super().__init__(
            parent=scene,
            model='cube',
            color=color.rgb(0,128,0),
            origin_y=0.5,
            position=position
        )
    
    # place and destroy blocks
    def input(self, key):
        if self.hovered:
            if key == 'right mouse down':
                voxel = Voxel(position=self.position + mouse.normal)
            if key == 'left mouse down':
                destroy(self)

def input(key):
    if key == 'escape':
        quit()

# generation
for z in range(25):
    for x in range(25):
        y = noise([x * 0.02,z * 0.02])
        y = math.floor(y * 7.5)
        voxel = Voxel(position=(x,y,z))

sky = Sky()
player = FirstPersonController()

game.run()