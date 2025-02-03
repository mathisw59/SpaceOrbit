import pygame
import os
path = os.path.dirname(os.path.realpath(__file__))

import math
class Vaisseau:
	def __init__(self):
		self.angle = math.pi/2
		self.texture = pygame.image.load('sprites/ship.png')
		self.dir = 1
		self.rect = self.texture.get_rect()
		self.rect.center = math.cos(self.angle)*250+350,math.sin(self.angle)*250+350
	def tick(self):
		self.dir *= -1
	def display(self,win):
		if self.dir == 1: toBlit = pygame.transform.rotate(self.texture,180-(self.angle/(2*math.pi))*360)
		else: toBlit = pygame.transform.rotate(self.texture,360-(self.angle/(2*math.pi))*360)
		self.rect.center = math.cos(self.angle) * 250+350, math.sin(self.angle) * 250+350
		win.blit(toBlit,(self.rect.x,self.rect.y))