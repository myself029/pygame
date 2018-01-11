import pygame
from 飞船 import Ship

class Settings():
	def __init__(self):
	    # 初始化游戏的设置
		# 屏幕设置
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (80,210,150)
		
		# 飞船设置
		self.ship_speed_factor = 1
		
		
		# 外星人飞船设置
		self.alien_speed_factor = 1
		self.fleet_direction = 1
		self.fleet_drop_speed = 4
		
		
		# 子弹设置
		self.bullet_limit = 4
		self.bullet_speed_factor=3
		self.bullet_width = 120
		self.bullet_height = 15
		self.bullet_color = 60,60,60