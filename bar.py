import pygame

class Bar:
	def __init__(bar,pos,max,width,height,color,increment,outRadius,defautValue):
		bar.pos = pos
		bar.max = max
		bar.value = float(defautValue)
		bar.width = width
		bar.height = height
		bar.increment = increment
		bar.color = color
		bar.outRadius = outRadius
	def tick(bar,win, i = True):
		black = (255,255,255)
		filledWidth = (bar.value / bar.max) * bar.width

		pygame.draw.circle(win,black,(bar.pos[0]-bar.width/2,bar.pos[1]),int(bar.height/2)+bar.outRadius,0)
		pygame.draw.rect(win,black,(bar.pos[0]-bar.width/2,bar.pos[1]-bar.height/2-bar.outRadius,bar.width,bar.height+bar.outRadius*2))
		pygame.draw.circle(win,black,(bar.pos[0]+bar.width/2,bar.pos[1]),int(bar.height/2)+bar.outRadius,0)

		pygame.draw.circle(win,bar.color,(bar.pos[0]-bar.width/2,bar.pos[1]),int(bar.height/2),0)
		pygame.draw.rect(win,bar.color,(bar.pos[0]-bar.width/2,bar.pos[1]-bar.height/2,filledWidth,bar.height))
		pygame.draw.circle(win,bar.color,(bar.pos[0]+int(filledWidth)-bar.width/2,bar.pos[1]),int(bar.height/2),0)

		if bar.value < bar.max and i: bar.value += bar.increment