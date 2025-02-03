import math,pygame,random
class Meteore:
	def __init__(self,angle):
		self.used = False
		self.color = [(60, 193, 36),(211, 42, 42),(41, 209, 184),(201, 0, 201),(201, 123, 0),(255, 242, 5)][random.randint(0,5)]
		self.coords = [350.+20*math.cos(angle),350.+20*math.sin(angle)]
		self.vect = [math.cos(angle)*3.5,math.sin(angle)*3.5]
	def tick(self,shipRect,win):
		#J'aimerai trouver un raccourci pour ca
		self.coords[0],self.coords[1] = self.coords[0]+self.vect[0],self.coords[1]+self.vect[1]
		rect = pygame.Rect([self.coords,(40,40)])
		rect.center = self.coords[0],self.coords[1]
		pygame.draw.circle(win, self.color, (int(self.coords[0]),int(self.coords[1])), 20, 0)
		if rect.colliderect(shipRect): return True
