import random

from ursina import * # pip install ursina 
from ursina.prefabs.first_person_controller import FirstPersonController


# create instance of app and add border to window
app = Ursina(borderless=False)

# window.fps_counter.enabled = False
# window.exit_button.visable = False
window.title = "Minecraft Clone"

# load assets
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)
block_pick = 'grass'
block_choices = {
	'grass' : load_texture('assets/grass_block.png'),
	'stone' : load_texture('assets/stone_block.png'),
	'brick' : load_texture('assets/brick_block.png'),
	'dirt' : load_texture('assets/dirt_block.png'),
}

# ursina automatically calls update() function every frame
def update(): 
	global block_pick
	# check keyboard input - held_keys is built into ursina
	if held_keys['1']:
		block_pick = 'grass'
	if held_keys['2']:
		block_pick = 'stone'
	if held_keys['3']:
		block_pick = 'brick'
	if held_keys['4']:
		block_pick = 'dirt'
	# animating hand when placing block down
	if held_keys['left mouse'] or held_keys['right mouse']: 
		hand.active()
	else: 
		hand.passive()
	

# box class - inherits Button class
class Voxel(Button):
	def __init__(self, position=(0,0,0), texture=block_choices['grass']):
		super().__init__(
			# need parent=scene to make obj visable
			parent=scene, 
			position=position,
			model='assets/block', 
			origin_y=0.5,
			texture=texture,
			color=color.color(0,0, random.uniform(0.9,1)),
			# highlight_color=color.lime
			scale=0.5
		)

	def input(self, key):
		global block_pick
		# self.hovered is built into Button class
		if self.hovered: 
			if key == 'left mouse down': 
				punch_sound.play()
				# make new box 
				Voxel(position=self.position + mouse.normal, texture = block_choices[block_pick])

			if key == 'right mouse down': 
				punch_sound.play()
				destroy(self)

class Sky(Entity): 
	def __init__(self): 
		super().__init__(
			parent=scene,
			model='sphere',
			texture=sky_texture,
			scale=100,
			double_sided=True
		)


class Hand(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui, 
			model = 'assets/arm', 
			texture = arm_texture, 
			scale = 0.1, 
			rotation = Vec3(100, -14.0), 
			position = Vec2(0.4, -0.5)
		)

	def active(self):
		self.position = Vec2(0.3, -0.5)
		self.rotation = Vec3(80, -5.0)
	def passive(self): 
		self.position = Vec2(0.4, -0.6)
		self.rotation = Vec3(100, -14.0)
       

# create 10x10 floor
for z in range(10): 
	for x in range(10): 
		voxel = Voxel(position=(x,0,z))

# create player aka camera, sky, and hand 
player = FirstPersonController()
sky = Sky()
hand = Hand()

# run app
app.run()