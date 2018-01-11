import sys
import pygame
from 飞船 import Ship
from 初始设置 import Settings
import 函数块 as gf
from pygame.sprite import Group
import time




def run_game():
	# 初始化游戏，并创建一个屏幕对象
	
	pygame.init()
	ai_settings = Settings()
 
	screen = pygame.display.set_mode(
				(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("邓明星大战外星人！")
	
	bg_color = ai_settings.bg_color
	
	ship = Ship(ai_settings,screen)
	
	aliens = Group()
	
	bullets = Group()

	# 创建外星人群
	gf.creat_fleet(ai_settings,screen,ship,aliens)
	
	# 主循环开始
	while True:
		gf.check_events(ai_settings,screen,ship,bullets)
		
		ship.update()
		
		gf.update_bullets(ai_settings,screen,ship,aliens,bullets)	
		
		gf.update_aliens(ai_settings, aliens)
		
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
	
run_game()

