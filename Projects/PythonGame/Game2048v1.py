# -*- coding: utf8 -*-
#------------------------------------------  
# 作者：李热热
# 名称：2048游戏
# 版本号：
# 0.1
# 0.2 补充上下左右按键的各自函数
# 0.3 增加对Mac系统的支持
#------------------------------------------ 
import random
import time
import os
import


class Game2048:
	"""docstring for Game2048"""

	#初始化矩阵
	v = [[0,0,0,0],
	     [0,0,0,0],
	     [0,0,0,0],
	     [0,0,0,0]]

	l = [2,2,2,4]


	p = [(x,y) for x in xrange(4) for y in xrange(4)]
	#p = tuple(temp,temp) 
	

	def __init__(self):
		self.score = 0
		self.moves = {
		       'a': self.left,
		       'd': self.right,
		       'w': self.up,
		       's': self.down
		 	}

		init_point = random.sample(self.p,2)
		init_num = [random.choice(self.l),random.choice(self.l)]

		for i in xrange(2):
			self.v[init_point[i][0]][init_point[i][1]] = init_num[i]
		
		
		
	def move(self):
		
		m=raw_input()
		direction = self.moves.get(m,self.default)()
		print direction
		#if self.isMerge(direction):
		self.update()

	def default(self):
		print "input error"

	def up(self):
	
		for i in xrange(4):
			temp_v=[self.v[j][i] for j in xrange(4)]

			temp_v = [num for num in temp_v if num != 0]
			while len(temp_v) < 4:
				temp_v.append(0)
			for j in xrange(4):
				self.v[j][i] = temp_v[j]
				

		for i in xrange(4):
			for j in xrange(3):
				if self.v[j][i] == self.v[j+1][i]:
					self.v[j][i] = self.v[j][i]*2
					self.v[j+1][i] = 0

		for i in xrange(4):
			temp_v=[self.v[j][i] for j in xrange(4)]

			temp_v = [num for num in temp_v if num != 0]
			while len(temp_v) < 4:
				temp_v.append(0)

			for j in xrange(4):
				self.v[j][i] = temp_v[j]

		return 'ver'


	def down(self):
		for i in xrange(4):
			temp_v=[self.v[j][i] for j in xrange(4)]

			temp_v = [num for num in temp_v if num != 0]
			while len(temp_v) < 4:
				temp_v.insert(0,0)
			for j in xrange(4):
				self.v[j][i] = temp_v[j]
				

		for i in xrange(4):
			for j in xrange(3,0,-1):
				if self.v[j][i] == self.v[j-1][i]:
					self.v[j][i] = self.v[j][i]*2
					self.v[j-1][i] = 0

		for i in xrange(4):
			temp_v=[self.v[j][i] for j in xrange(4)]

			temp_v = [num for num in temp_v if num != 0]
			while len(temp_v) < 4:
				temp_v.insert(0,0)

			for j in xrange(4):
				self.v[j][i] = temp_v[j]

		return 'ver'
			

	def left(self):
		for i in xrange(4):
			temp_v = [num for num in self.v[i] if num != 0]
			while len(temp_v) < 4:
				temp_v.append(0)
			self.v[i] = temp_v

		for i in xrange(4):
			for j in xrange(3):
				if self.v[i][j] == self.v[i][j+1]:
					self.v[i][j] = self.v[i][j]*2
					self.v[i][j+1] = 0
		for i in xrange(4):
			temp_v = [num for num in self.v[i] if num != 0]
			while len(temp_v) < 4:
				temp_v.append(0)
			self.v[i] = temp_v

		return 'hor'
		# for i in xrange(3):
		# 	if 0 in [x-y for x,y in zip(self.v[i],self.v[i+1])]:

		# 		return True


	def right(self):
		for i in xrange(4):
			temp_v = [num for num in self.v[i] if num != 0]
			print temp_v
			while len(temp_v) < 4:
				temp_v.insert(0,0)
			print temp_v
			self.v[i] = temp_v

		for i in xrange(4):
			for j in xrange(3,0,-1):
				if self.v[i][j] == self.v[i][j-1]:
					self.v[i][j] = self.v[i][j]*2
					self.v[i][j-1] = 0
		for i in xrange(4):
			temp_v = [num for num in self.v[i] if num != 0]
			while len(temp_v) < 4:
				temp_v.insert(0,0)
			self.v[i] = temp_v

		return 'hor'



	def update(self):
		zero_point = [(x,y) for x in xrange(4) for y in xrange(4) if self.v[x][y] == 0]
		new_num = random.choice(self.l)
		new_point = random.choice(zero_point)
		print new_point,'=',new_num
		self.v[new_point[0]][new_point[1]] = new_num

	def display(self):
		print "┏━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┓"

		for i in xrange(4):
			print '┃       ┃       ┃       ┃       ┃'
			
			print '┃',
			for j in xrange(4):
				if self.v[i][j]==0:
					print '     ','┃',
				else:
					if self.v[i][j]<10:
						print ' ',self.v[i][j],'  ┃',
					elif 10<self.v[i][j]<100:
						print ' ',self.v[i][j],' ┃',
					elif 100<self.v[i][j]<1000:
						print '',self.v[i][j],' ┃',
					elif self.v[i][j]>1000:
						print '',self.v[i][j],'┃',
			print 
			print '┃       ┃       ┃       ┃       ┃'
			if i<3:
				print "┣━━━━━━━╋━━━━━━━╋━━━━━━━╋━━━━━━━┫"
			else:
				print "┗━━━━━━━┻━━━━━━━┻━━━━━━━┻━━━━━━━┛"
			# print '-----------------'
			# print #┏━━━━━━━━━━━━┓┗━━━━━━━━━━━━┛┃┃┫╋┣┳┻
		print "score:",self.score
	
	def over(self):
		zero_point = [(x,y) for x in xrange(4) for y in xrange(4) if self.v[x][y] == 0]
		#print zero_point
		if not len(zero_point) and not self.isMerge(0):
			print "the game is over!"
			return True
		else:
			return False	
		

	def isMerge(self,direction):
		#不包括零
		if direction == 0:
			for i in xrange(4):
				for j in xrange(3):
					if  self.v[i][j] == self.v[i][j+1] and not self.v[i][j]:
						return True

			for i in xrange(3):
				if 0 in [x-y  for x,y in zip(self.v[i],self.v[i+1]) if x==y!=0]:

					return True

			return False
		elif direction == 'hor':
			for i in xrange(4):
				for j in xrange(3):
					if  self.v[i][j] == self.v[i][j+1] and self.v[i][j]!=0:
						return True
			return False
		elif direction == 'ver':
			for i in xrange(3):
				if 0 in [x-y  for x,y in zip(self.v[i],self.v[i+1]) if x==y!=0]:

					return True

			return False


#if __name__ == "__main__":
g = Game2048()
i = 0
while(True):
		
	#print '\n'*100
	g.display()
	if g.over():
		break
	g.move()


	i+=1
		



	

		
		
