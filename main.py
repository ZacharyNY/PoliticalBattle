import pygame
import sys

import crudder

class HomeScreen:
	def __init__(self):
		self.font = pygame.font.SysFont("monospace", 30)
		self.labeldem = self.font.render("Democrat", 1, (0, 0, 0))
		self.labelrep = self.font.render("Republican", 1, (0, 0, 0))
		self.labelx = 150
		self.labely = 250
		self.background_color = (255, 255, 255)
		self.demrectx = 100
		self.demrecty = 200
		self.demrectw = 300
		self.demrecth = 100
		self.rect_color = (100, 100, 100)
		self.reprectx = 100
		self.reprecty = 350
		self.reprectw = 300
		self.reprecth = 100
		self.is_dem = True

	def get_home_screen(self, screen):
		'''paints the home page to the screen'''
		screen.fill(self.background_color)
		pygame.draw.rect(screen, self.rect_color, pygame.Rect(self.demrectx, self.demrecty, self.demrectw, self.demrecth))
		screen.blit(self.labeldem, (self.labelx, self.labely))
		pygame.draw.rect(screen, self.rect_color, pygame.Rect(self.reprectx, self.reprecty, self.reprectw, self.reprecth))
		screen.blit(self.labelrep, (self.labelx, self.labely+100))
		return screen

	def is_in_dem_button(self, pos):
		xpos = pos[0]
		ypos = pos[1]
		if xpos > self.demrectx and xpos < self.demrectx+self.demrectw:
			if ypos > self.demrecty and ypos < self.demrecty+self.demrecth:
				return True
		return False

	def is_in_rep_button(self, pos):
		xpos = pos[0]
		ypos = pos[1]
		if xpos > self.reprectx and xpos < self.reprectx+self.reprectw:
			if ypos > self.reprecty and ypos < self.reprecty+self.reprecth:
				return True
		return False

class CharacterScreen():
	def __init__(self):
		self.font = pygame.font.SysFont("monospace", 15)
		self.labelPlay = self.font.render("Player", 1, (0, 0, 0))
		self.labelPlayx = 75
		self.labelPlayy = 20
		self.labelOpp = self.font.render("Opponent", 1, (0, 0, 0))
		self.labelOppx = 350
		self.labelOppy = 20
		self.labelBack = self.font.render("Back", 1, (255, 255, 255))
		self.labelStart = self.font.render("Start", 1, (255, 255, 255))
		self.labelBacky = 465
		self.labelBackx = 90
		self.labelStartx = 360
		self.background_color = (255, 255, 255)
		self.rect_color = (0, 0, 100)
		self.rect_color2 = (0, 100, 0)
		self.rect_color3 = (100, 0, 0)
		self.rectPlayx = 10
		self.rectPlayy = 50
		self.rectOppx = 280
		self.rectOppy = 50
		self.rectStarth = 25
		self.rectStartw = 100
		self.rectStartx = 330
		self.rectStarty = 460
		self.rectBackx = 60
		self.rectCharh = 400
		self.rectCharw = 200
		self.rectChoiceh = 80
		self.rectChoicew = 160
		self.rectPlayChoicex = 30
		self.rectPlayChoicey = 60
		self.rect_color4 = (0, 0, 0)
		self.rectOppChoicex = 300
	
	def get_character_screen(self, screen):
		self.loopInc = 0
		self.rectPlayChoicey = 60
		screen.fill(self.background_color)
		pygame.draw.rect(screen, self.rect_color, pygame.Rect(self.rectPlayx, self.rectPlayy, self.rectCharw, self.rectCharh))
		pygame.draw.rect(screen, self.rect_color, pygame.Rect(self.rectOppx, self.rectOppy, self.rectCharw, self.rectCharh))		
		pygame.draw.rect(screen, self.rect_color2, pygame.Rect(self.rectStartx, self.rectStarty, self.rectStartw, self.rectStarth))		
<<<<<<< HEAD
		pygame.draw.rect(screen, self.rect_color3, pygame.Rect(self.rectBackx, self.rectStarty, self.rectStartw, self.rectStarth))		
	
=======
		pygame.draw.rect(screen, self.rect_color3, pygame.Rect(self.rectBackx, self.rectStarty, self.rectStartw, self.rectStarth))
		screen.blit(self.labelPlay, (self.labelPlayx, self.labelPlayy))
		screen.blit(self.labelStart, (self.labelStartx, self.labelBacky))
		screen.blit(self.labelOpp, (self.labelOppx, self.labelOppy))
		screen.blit(self.labelBack, (self.labelBackx, self.labelBacky))		
>>>>>>> 67f657ebe1288c4d90ce46a980e6abc46cc9c67c
		#loop to create boxes for the character choices
		while self.loopInc < 4:
			pygame.draw.rect(screen, self.rect_color4, pygame.Rect(self.rectPlayChoicex, self.rectPlayChoicey, self.rectChoicew, self.rectChoiceh))
			pygame.draw.rect(screen, self.rect_color4, pygame.Rect(self.rectOppChoicex, self.rectPlayChoicey, self.rectChoicew, self.rectChoiceh))
			self.rectPlayChoicey = self.rectPlayChoicey + 90
			self.loopInc = self.loopInc + 1	
		return screen

	def set_play_choice(self, party):
		self.party = party

	def is_in_start_button(self, pos):
		xpos = pos[0]
		ypos = pos[1]
		if xpos > self.rectStartx and xpos < self.rectStartx+self.rectStartw:
			if ypos > self.rectStarty and ypos < self.rectStarty+self.rectStarth:
				return True
		return False

	def is_in_back_button(self, pos):
		xpos = pos[0]
		ypos = pos[1]
		if xpos > self.rectBackx and xpos < self.rectBackx+self.rectStartw:
			if ypos > self.rectStarty and ypos < self.rectStarty+self.rectStarth:
				return True
		return False


class GameScreen():
	def __init__(self):
		self.font = pygame.font.SysFont("monospace", 30)
		self.background_color = (255, 255, 255)
		#box with the attacks
		self.attboxx = 0
		self.attboxy = 400
		self.attboxh = 400
		self.attboxw = 100
		self.attboxc = (100, 100, 100)
		#four boxes for the attacks
		self.attboxesx = [0, 200, 0, 200]
		self.attboxesy = [300, 300, 400, 400]
		self.attboxesw = 200
		self.attboxesh = 100
		#box for the options box
		self.opboxx = 400
		self.opboxy = 400
		self.opboxw = 100
		self.opboxh = 100
		self.opboxc = (200, 200, 200)
		self.playimgx = 0
		self.playimgy = 300
		self.oppimgx = 400
		self.oppimgy = 0
	
	def set_chars(self, player, opponent):
		'''this function currently assumes that the images will be jpegs
		   so we will probably need to change that'''
		self.playimg = pygame.image.load("images/{play}.jpg"\
			.format(play = player))
		self.oppimg = pygame.images.load("images/{opp}.jpg"\
			.format(opp = opponent))

	def get_game_screen(self, screen):
		screen.fill((255, 255, 255))
		#screen.blit(self.playimg, (playimgx, playimgy))
		#screen.blit(self.oppimg, (oppimgx, oppimgy))
		pygame.draw.rect(screen, self.attboxc, pygame.Rect(self.attboxx, self.attboxy, self.attboxw, self.attboxh))
		pygame.draw.rect(screen, self.opboxc, pygame.Rect(self.opboxx, self.opboxy, self.attboxw, self.attboxh))
		for x in range(0, 4):
			pygame.draw.rect(screen, self.attboxc, pygame.Rect(self.attboxesx[x], self.attboxesy[x], self.attboxesw, self.attboxesh))


def main():
	'''
	runs the main game loop and
	manages everything
	'''

	pygame.init()
	screen = pygame.display.set_mode((500, 500))

	hs = HomeScreen()
	cs = CharacterScreen()
	gs = GameScreen()

	# -- this would need to be worked out --
	#if 1, then were at the home screen
	#if 2, were at character selection
	#if 3, in the game
	game_state = 1

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if game_state == 1:
					if hs.is_in_dem_button(pygame.mouse.get_pos()):
						game_state = 2
						cs.set_party("DEM")
					if hs.is_in_rep_button(pygame.mouse.get_pos()):
						game_state = 2
						cs.set_party("REP")
				if game_state == 2:
				  	if cs.is_in_start_button(pygame.mouse.get_pos()):
						game_state = 3
					elif cs.is_in_back_button(pygame.mouse.get_pos()):
						game_state = 1
		if game_state == 1:
		 	screen = hs.get_home_screen(screen)
		elif game_state == 2:
		 	screen = cs.get_character_screen(screen)
		elif game_state == 3:
		    	screen = gs.get_game_screen(screen)
		pygame.display.update()
		pygame.display.flip()


if __name__ == "__main__":
	main()
