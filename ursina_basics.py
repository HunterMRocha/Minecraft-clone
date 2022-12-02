from ursina import *								# Import the ursina engine - need pip install ursina & python version 3.6>

class Test_cube(Entity):							# class that inherits Entity from Ursina 
	def __init__(self):
		super().__init__(							# call super to inintialize Entity 
			model='cube',							# set model type 
			color=color.white,						# set color using color. 
			texture='white_cube', 					# this texture is built into ursina
			rotation = Vec3(45, 45, 45)				# rotate entity by creating a Vector with Vec3(x, y, z)
		)

class Test_button(Button): 
	def __init__(self):
		super().__init__(
			parent=scene,
			model='cube', 
			texture='brick', 
			color=color.blue,
			highlight_color=color.red,
			pressed_color=color.lime,
		)

	def input(self, key):
		if self.hovered:
			if key == 'left mouse down':
				print('button pressed')


def update(): 										# update() automatically called every frame in Ursina
	if held_keys['a']:								# use held_keys to check for keyboard input 
		test_square.x -= 1 * time.dt				# move entity x * time.dt - build into Ursina


app = Ursina()										# Initialise your Ursina app


test_square = Entity(
				model = 'quad', 
				color = color.red, 
				scale = (1, 4),
				position=(5, 1)
			)

sans = Entity(
		model = 'quad', 
		texture='assets/sans.png'
	)

test_cube = Test_button()

# run usina app
app.run()