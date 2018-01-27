import  pygame
from pygame.sprite import Sprite

    

class Bullet(Sprite):
	""" 一个对飞船发射子弹进行编组管理的类 """
	def __init__(self,ai_settings,screen,ship):
	# 引入形参
		super(Bullet,self).__init__()
		self.screen = screen
		
	# 在(0,0)创建一个子弹，然后将其赋值到正确位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
								ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		
		self.y =float(self.rect.y)
		
		self.color = ai_settings.bullet_color
		
		self.speed_factor = ai_settings.bullet_speed_factor
		
		
	def update(self):
		self.y -= self.speed_factor
		self.rect.y =  self.y
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
	
	