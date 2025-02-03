#coding: utf-8
import math,pygame,point,meteore,vaisseau,os,time,bar,keyboard
import os
path = os.path.dirname(os.path.realpath(__file__))
pygame.init()
pygame.key.set_repeat(1000)
font = pygame.font.SysFont("MV Boli", 26)
def game(scorej1,scorej2,tour):
	nitro = bar.Bar([100,75],500,100,30,(66, 244, 83),2,2,0)
	health = bar.Bar([600,75],300,75,30,(220, 0, 0),0,2,300)
	win = pygame.display.set_mode((700, 700))
	progressBar = bar.Bar([350,680],1000,500,30,(244, 196, 65),2,2,0)
	score = 0
	hInc = .2
	used = 0
	t = 0.65
	nT = time.time()
	dirT = time.time()
	s = time.time()
	d = time.time()
	ship = vaisseau.Vaisseau()
	points = [point.Point((math.pi*(float(a)/20))) for a in range(0,40)]
	meteores = []
	running = True
	while running:
		if time.time() >= s + t and pygame.mouse.get_pressed()[0]:
			s = time.time()
			coords = pygame.mouse.get_pos()
			angle = math.atan2(coords[1] - 350, coords[0] - 350)
			meteores.append(meteore.Meteore(angle))
		for evt in pygame.event.get():
			if evt.type == pygame.KEYDOWN and evt.key == pygame.K_w: ship.tick()
			elif evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE): pygame.quit; os._exit(1)
		if keyboard.is_pressed('shift') and nitro.value >= 0: ship.angle += math.pi/80 * ship.dir;nitro.value -=5; used = 50
		else : ship.angle += math.pi/192 * ship.dir

		pygame.draw.rect(win,(13,14,44), (0,0,700,700))
		#Quand je fais pas des cercles pleins, il y a des trous. Génies
		pygame.draw.circle(win, (17,19,58), (350,350), 250, 0)
		pygame.draw.circle(win, (20,21,67), (350,350), 186, 0)
		pygame.draw.circle(win, (24,27,70), (350,350), 123, 0)
		pygame.draw.circle(win, (150,66,76), (350,350), 58, 0)
		pygame.draw.circle(win, (221,40,38), (350,350), 52, 0)
		pygame.draw.circle(win, (14,43,40), (350,350), 41, 0)
		pygame.draw.circle(win, (131,147,36), (350,350), 35, 0)
		pygame.draw.circle(win, (121,135,17), (350,350), 15, 0)
		toblit = font.render("Score : " + str(score), 1, (255,255,194))
		win.blit(toblit, (350-int(toblit.get_width()/2), 25))
		for a in points:
			if a.tick(ship.rect,win): score += 1; points.remove(a)
		if len(points) == 0 : points = [point.Point((math.pi*(float(a)/20))) for a in range(0,40)]
		pygame.draw.circle(win, [225]*3, (350,350), 250, 1)
		ship.display(win)
		for m in meteores:
			if m.tick(ship.rect,win) and not m.used: health.value -=50; meteores.remove(m)
		for m in meteores:
			if m.coords[0] > 750 or m.coords[0] < -50 or m.coords[1] > 750 or m.coords[1] < -50: meteores.remove(m)
		nitro.tick(win, i = used ==0)
		if health.value <= 0: running = False
		if progressBar.value == 1000: progressBar.value = 0.; t /= 1.2; hInc += .075
		if used > 0: used -=1
		if time.time() > d + .7:health.value += hInc
		if health.value > health.max: health.value = health.max
		health.tick(win)
		progressBar.tick(win)
		pygame.display.flip()
		time.sleep(0.0166666667)

	win.blit(pygame.image.load("sprites/deathscreen.png"),(0,0))
	toblit = font.render("Score : " + str(score), 1, (255,255,194))
	if tour: scorej2 += score
	else: scorej1 += score
	tour = not tour
	win.blit(toblit, (550-int(toblit.get_width()/2), 175))
	toblit = font.render("Score du j1 : " + str(scorej1), 1, (255,255,194))
	win.blit(toblit, (150-int(toblit.get_width()/2), 75))
	toblit = font.render("Score du j2 : " + str(scorej2), 1, (255,255,194))
	win.blit(toblit, (550-int(toblit.get_width()/2), 75))
	if tour:
		toblit = pygame.font.SysFont("MV Boli", 40).render("Au tour de j2 !", 1, (255,160,160))
		win.blit(toblit, (350-int(toblit.get_width()/2), 260))
	else:
		toblit = pygame.font.SysFont("MV Boli", 40).render("Au tour de j1 !", 1, (255,160,160))
		win.blit(toblit, (350-int(toblit.get_width()/2), 260))
	pygame.display.flip()
	time.sleep(1)
	running = True
	while running:
		for evt in pygame.event.get():
			if evt.type == pygame.QUIT or (evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE): pygame.quit; os._exit(1)
			if evt.type == pygame.KEYDOWN or pygame.mouse.get_pressed()[0]: running = False
		time.sleep(0.05)
	game(scorej1,scorej2,tour)
game(0,0,False)
