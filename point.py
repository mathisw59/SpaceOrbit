#coding: utf-8
import math,pygame
class Point:
	def __init__(self,angle):
		self.angle = angle
		self.rect = pygame.Rect(int(math.cos(self.angle)*250+350),int(math.sin(self.angle)*250+350),5,5)
	def tick(self,shipRect,win):
		pygame.draw.circle(win, [225]*3, (self.rect.x,self.rect.y), 5, 0)
		#collide_circle est malheuresement bugué et flemme de faire un masque
		if self.rect.colliderect(shipRect): return True