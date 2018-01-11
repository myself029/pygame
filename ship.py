import pygame

# ship 父类创建
#class Ship():
#	"""初始化飞船并设置期初始位置"""
	# 需要调用screen中的属性参数，故本次的init动作包括screen参数
	
#	def __init__(self,screen):
	# 初始化，并导入形参screen
#		self.screen = screen
		
	# 加载ship图片
	# pygame.image.load 返回1个Surface，
	# 该surface对象赋值给 self.image 变量名称，该变量名称随意，必须包含 self
	# 利用rect_get方法获取 self.image也就是加载的surface的rect属性
#		self.image = pygame.image.load(r'D:\python35\pygame\作业\images\ship.bmp') 
	
	
#		self.rect = self.image.get_rect()
		
	# 利用rect_get方法获取形参screen的rect属性，因为screen也是Surface对象
	# 利用上述获取的rect值赋值给self.screen_rect变量,该变量名称随意，必须包含 self
class Ship():
	"""初始化飞船并设置期初始位置"""
	# 需要调用screen中的属性参数，故本次的int动作包括screen参数
	def __init__(self,ai_settings,screen):
	
		self.screen = screen
		
		self.ai_settings = ai_settings
		
	# 加载飞船图像并获其外接矩形
	# 使用pygame的image模块的load方法加载图像，并初始赋值给surface变量对象 self.image
	
		self.image = pygame.image.load(r'D:\python35\pygame\images\ship.bmp') 
	# image 模块包含了加载和保存图像的函数，同时转换为 Surface 对象支持的格式。
	# 注意：没有 Image 类；当一个图像被成功载入后，将转换为 Surface 对象。
	# Surface 对象允许你在上边画线、设置像素、捕获区域等。故可以使用surface的方法和属性对image进行渲染
	# image 为surface 对象中的一种，故加载成功后，可以使用surface的get_rect方法
	# 利用矩形函数get_rect方法获取抽象image矩形对象的rect属性，并赋值给实际image对象 ship的self.rect属性
	# ship作为image的实际名称，也就具有surface对象的所有属性和方法。
	
		self.rect = self.image.get_rect() 
	# screen 也是surface 一种对象，所有也可以像image一样调用surface的方法和属性		
	# 利用get_rect方法获取screen对象矩形属性，并赋值给self的screen_rect变量属性	
		self.screen_rect = screen.get_rect()  
			
	# 将飞船加载指屏幕中间位置
	# 将矩形screen屏幕对象的centerx位置属性（即对象的x轴方向的中心值）值赋值给image对象的centerx 
		self.rect.centerx = self.screen_rect.centerx
		
	# 将矩形screen屏幕对象的bottom位置属性（即对象的x轴方向的中心值）值赋值给image对象的bottom 
		self.rect.bottom = self.screen_rect.bottom
		
	# 设置移动标志，即识别移动方向的flag
		self.moving_right = False
		self.moving_left = False	
		self.moving_down = False		
		self.moving_up = False	
		
	# 在飞船的属性center中存储小数值(把rect.centerx整型转换为 float型)
		self.center = float(self.rect.centerx)
	
	
	
	def update(self):
	# 如果下面的第一if语句之后都采用elif 语句，会有什么效果呢？ 可以试验下
    # 如果同时按下→ 和 ← 方向键，event.key检查到两个事件，这个时候两个事件如何执行 ？？
	# 更新飞船的center值，而不是 rect值。
	# Setting类中包含self.ship_speed_factor = 1.5
	
		if self.moving_right and self.rect.right < self.screen_rect.right:
				self.center +=self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > self.screen_rect.left:
				self.center -=self.ai_settings.ship_speed_factor		
		if self.moving_up and self.rect.top > self.screen_rect.top:
				self.rect.centery -=1
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
				self.rect.centery +=1
		# 根据self.center更新rect对象
		self.rect.centerx = self.center
				
	def blitme(self):
	# 在指定位置绘制飞船 
	# blit(source, dest, area=None, special_flags = 0) -> Rect，draw one image onto another 
	# 此处将surface对象image画在另外一个surface对象上面，同时获取一个矩形图像rect
	# source, dest分别表示绘制的原图和目标位置，本处即为将image按照上文中的rect属性绘图在screen上面
		self.screen.blit(self.image, self.rect)
	# 调用此blitme方法即绘制该image 对象到 screen 对象上面