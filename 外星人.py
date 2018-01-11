import  pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	""" 一个对外星人进行编组管理的类 """
	def __init__(self,ai_settings,screen):
	# 引入形参
		super(Alien,self).__init__()
		self.screen = screen
		
		self.ai_settings = ai_settings
		
	# 加载飞船图像并获其外接矩形
	# 使用pygame的image模块的load方法加载图像，并初始赋值给surface变量对象 self.image
	
		self.image = pygame.image.load(r'D:\python35\pygame\images\alien.bmp') 
	# image 模块包含了加载和保存图像的函数，同时转换为 Surface 对象支持的格式。
	# 注意：没有 Image 类；当一个图像被成功载入后，将转换为 Surface 对象。
	# Surface 对象允许你在上边画线、设置像素、捕获区域等。故可以使用surface的方法和属性对image进行渲染
	# image 为surface 对象中的一种，故加载成功后，可以使用surface的get_rect方法
	# 利用矩形函数get_rect方法获取抽象image矩形对象的rect属性，并赋值给实际image对象 ship的self.rect属性
	# ship作为image的实际名称，也就具有surface对象的所有属性和方法。
	
		self.rect = self.image.get_rect() 
		
	# 将飞船加载指屏幕中间位置
	# 将矩形screen屏幕对象的centerx位置属性（即对象的x轴方向的中心值）值赋值给image对象的centerx 
		self.rect.x = self.rect.width
		
	# 将矩形screen屏幕对象的bottom位置属性（即对象的x轴方向的中心值）值赋值给image对象的bottom 
		self.rect.y = self.rect.height
		
	# 在飞船的属性center中存储小数值(把rect.centerx整型转换为 float型)
		self.x = float(self.rect.x)
	

	def check_edges(self):
	# 检查是否发生外星人碰撞屏幕边缘
	# 首先要获取屏幕的rect属性，并赋值给变量 screen_rect
		screen_rect = self.screen.get_rect()
		
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
				
	def update(self):
	# 向右移动外星人
	# line11  本类中导入了 	self.ai_settings = ai_settings  实例作为自己的属性实例
		self.x  += (self.ai_settings.ship_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x
	

		
	def blitme(self):
	# 在指定位置绘制外星人 
	# blit(source, dest, area=None, special_flags = 0) -> Rect，draw one image onto another 
	# 此处将surface对象image画在另外一个surface对象上面，同时获取一个矩形图像rect
	# source, dest分别表示绘制的原图和目标位置，本处即为将image按照上文中的rect属性绘图在screen上面
		self.screen.blit(self.image, self.rect)
	# 调用此blitme方法即绘制该image 对象到 screen 对象上面