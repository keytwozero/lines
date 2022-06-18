walls = False
draw_bridges = False
player_color = [6,5] # Head, Lines
walls_colors = [4,13] # Centers, Walls
import pyxel
from random import randint
w, h = 33, 33
ww, hw = w + (w - 1), h + (h - 1)
regeneration = 2
hp_max = 5
chance_max = 20
class Windower:
	def __init__(self):
		self.restart()
		pyxel.init(ww, hw, fps=144)
		pyxel.run(self.update, self.draw)
	def restart(self):
		self.hp = hp_max
		self.pose = [h//2,w//2]
		self.death = False
		self.field = []
		for i in range(h):
			temp = []
			for j in range(w):
				m = [0,0,0,0]
				if not i:
					m[0] = 2
				if i == h-1:
					m[3] = 2
				if not j:
					m[1] = 2
				if j == w-1:
					m[2] = 2
				if walls:
					if not randint(0,chance_max) and m[0] != 2 and m[3] != 2:
						m[0] = 3
						m[3] = 3
					if not randint(0,chance_max) and m[1] != 2  and m[2] != 2:
						m[1] = 3
						m[2] = 3
				temp.append(m)
			self.field.append(temp)
	def move(self,pose_axis,pose_count,ca,cy,cx,cab):
		self.field[self.pose[0]   ][self.pose[1]   ][ca ] = 1
		self.field[self.pose[0]+cy][self.pose[1]+cx][cab] = 1
		self.pose[pose_axis] += pose_count
		wall = False
		can = 4
		for i in range(4):
			if self.field[self.pose[0]][self.pose[1]][i] in [1,3]:
				can -= 1
			elif self.field[self.pose[0]][self.pose[1]][i] == 2:
				can -= 1
				wall = True
		if not can:
			self.death = True
		if can < regeneration + 1:
			if not wall:
				self.hp = hp_max
			else:
				self.hp -= 1
		else:
			self.hp -= 1
		if self.hp == 0:
			self.death = True
	def update(self):
		if pyxel.btnp(pyxel.KEY_BACKSPACE):
			self.restart()
		if not self.death:
			if not self.field[self.pose[0]][self.pose[1]][1]:
				if pyxel.btnp(pyxel.KEY_LEFT):
					self.move(1,-1,			1,0,-1,2)
			if not self.field[self.pose[0]][self.pose[1]][2]:
				if pyxel.btnp(pyxel.KEY_RIGHT):
					self.move(1,1,			2,0,1,1)
			if not self.field[self.pose[0]][self.pose[1]][0]:
				if pyxel.btnp(pyxel.KEY_UP):
					self.move(0,-1,			0,-1,0,3)
			if not self.field[self.pose[0]][self.pose[1]][3]:
				if pyxel.btnp(pyxel.KEY_DOWN):
					self.move(0,1,			3,1,0,0)
	def draw(self):
		pyxel.cls(0)
		for i in range(len(self.field)):	
			for j in range(len(self.field[i])):
				have = False
				wall = False
				if draw_bridges:
					pyxel.pset(j*2,i*2,13)
				if self.field[i][j][0] == 3:
					pyxel.pset(j*2,i*2-1,walls_colors[1])
					wall = True
				if self.field[i][j][1] == 3:
					pyxel.pset((j*2)-1,i*2,walls_colors[1])
					wall = True
				if self.field[i][j][2] == 3:
					pyxel.pset((j*2)+1,i*2,walls_colors[1])
					wall = True
				if self.field[i][j][3] == 3:
					pyxel.pset(j*2,i*2+1,walls_colors[1])
					wall = True
				if wall:
					pyxel.pset(j*2,i*2,walls_colors[0])
				if self.field[i][j][0] == 1:
					pyxel.pset(j*2,i*2-1,player_color[1])
					have = True
				if self.field[i][j][1] == 1:
					pyxel.pset((j*2)-1,i*2,player_color[1])
					have = True
				if self.field[i][j][2] == 1:
					pyxel.pset((j*2)+1,i*2,player_color[1])
					have = True
				if self.field[i][j][3] == 1:
					pyxel.pset(j*2,i*2+1,player_color[1])
					have = True
				if have:
					pyxel.pset(j*2,i*2,player_color[1])
		if not self.death:
			pyxel.pset(self.pose[1]*2,self.pose[0]*2,player_color[0])
Windower()
