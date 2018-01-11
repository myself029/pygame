import pygame
import sys
from 初始设置 import Settings
from  飞船 import Ship
from 子弹 import Bullet
from 外星人 import Alien



def check_events(ai_settings,screen,ship,bullets):
	 # event 在本模块中已经定义了，不需要形参中加入
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_down_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_up_events(event,ship)
			
def check_down_events(event,ai_settings,screen,ship,bullets):
	# 根据上下左右方向键进行移动标志判定
	if event.key == pygame.K_RIGHT:
		ship.moving_right=True
		pygame.display.set_caption('飞船移动方向 ：right')
	elif event.key == pygame.K_LEFT:
		ship.moving_left=True
		pygame.display.set_caption("飞船移动方向 ：left" )
	elif event.key == pygame.K_UP:
		ship.moving_up=True
		pygame.display.set_caption("飞船移动方向 ：up" )
	elif event.key == pygame.K_DOWN:
		ship.moving_down=True
		pygame.display.set_caption("飞船移动方向 ：down" )
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	
		
def check_up_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False	
	if event.key == pygame.K_DOWN:
		ship.moving_down = False	
	if event.key == pygame.K_UP:
		ship.moving_up = False	
		
		
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullet_limit:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)
		pygame.display.set_caption("子弹开火中！！！" )
		
def update_bullets(ai_settings,screen,ship,bullets,aliens):
	#更新子弹群组的位置，并删除已消失的子弹
	bullets.update()
	# 为什么要在copy中遍历呢 ？
	for bullet in bullets.copy():
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
			
	# 检查是否有子弹击中了外星人
	# 如果是这样， 就删除相应的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	
	if len(aliens)==0:
		bullets.empty()
		creat_fleet(ai_settings,screen,ship,aliens)
		
def update_screen(ai_settings,screen,ship,aliens,bullets):
	# screen背景色更新，调用fill方法，并使用ai_settings的参数
	screen.fill(ai_settings.bg_color)
	# 在飞船和飞船后面绘制所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
		
	# ship 绘制在screen上，但是没有更新显示出来
	ship.blitme()
	
	# 可以访问主程序中创建的aliens群组
	
	aliens.draw(screen)
	# screen 更新，显示最新绘制图形,调用pygame中的display.flip函数
	pygame.display.flip()
	
	

def get_number_aliens_x(ai_settings,alien_width):  # 此处的ailen_width 只是一个形参，实际使用以实参为准名，实际传入
	"""计算每行可以容纳的外星人数量"""

	# 计算屏幕允许的最大横向 X 的放置外星人群的宽度(屏幕宽度-最小间距*2)
	available_space_x = ai_settings.screen_width - 2*alien_width
	
	# 获取屏幕允许的横向 X 的最大外星人数量
	number_aliens_x =  int(available_space_x/(2*alien_width))
	
	# 函数返回计算的数量
	return  number_aliens_x
	
def get_number_aliens_rows(ai_settings,ship_height,alien_height):
	""" 计算屏幕允许的外星人行数"""
	available_space_y = ai_settings.screen_height - 2*alien_height-	ship_height
	
	number_rows =  int(available_space_y/(2*alien_height))
	
	# 函数返回计算的数量
	return  number_rows
	

def create_alien(ai_settings,screen,aliens,alien_number,row_number):  

	"""创建1个外星人，并将其放在当前行"""
	# 创建第一个外星人实例
	alien = Alien(ai_settings,screen)
	# 获取外星人宽度和高度,同时外星人的x间距也设置为该宽度
	alien_width = alien.rect.width
	
	alien_height = alien.rect.height
	
	# 设计外星人X坐标轴的位置公式
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	
	# 设计外星人y坐标轴的位置公式
	alien.y = alien_height + 2 * alien_height * row_number
	alien.rect.y = alien.y
	
	aliens.add(alien)


def creat_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	# 创建一个外星人， 并计算需要容纳多少外星人
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows =  get_number_aliens_rows(ai_settings,ship.rect.height,alien.rect.height)

	# 通过遍历方式，创建整行外星人
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)

def change_fleet_direction(ai_settings, aliens):
	"""将整群外星人下移， 并改变它们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
		
def check_fleet_edges(ai_settings, aliens):
	"""有外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
	# 调用alien的check edges方法判断是否发生碰撞屏幕边缘
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break
								
def update_aliens(ai_settings, aliens):
	"""检查是否有外星人位于屏幕边缘， 并更新整群外星人的位置"""
	check_fleet_edges(ai_settings, aliens)
	aliens.update()
	
	
	