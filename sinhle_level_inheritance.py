# #single level inheritance


# class Ball:
	
# 	def __init__(self, radius, texture = None, bounce = None, weight = None, color = None):
# 		self.radius = radius
# 		self.shape = 'Sphere'
# 		self.texture = texture
# 		self.bounce = bounce
# 		self.weight = weight
# 		self.color = color
	
# 	def get_game_type(self):
# 		return self.game_type

# 	def __repr__(self):
# 		return f'Ball : {self.radius} , {self.texture}'


# class Tennis(Ball):
	
# 	def __init__(self, radius, texture, bounce = None, weight = None, color = None):
# 		super().__init__(radius,texture,bounce,weight,color)
# 		self.game_type = 'Tennis Game'


# class BasketBall(Ball):
# 	def __init__(self, radius, texture, bounce = None, weight = None, color = None):
# 		self.game_type = 'Basketball Game'
# 		super().__init__(radius,texture,bounce,weight,color)



# # t = Tennis(6, 'fur', color = 'Red', weight = '200 gm', bounce = 0.9)
# # print(t.__dict__)
# # print(t)
# # print(t.game_type)

# b = BasketBall(15, 'rough-fabric', color = 'Red and Black', weight = '800 gm', bounce = 0.6)
# print(b.__dict__)
# print(b.game_type)
# print(b.get_game_type())



#multiple inheritance

class A:
	def area(self):
		print('im grandparent: A area')

#inheritance from A
class B(A):
	def perimeter(self):
		print('im perimeter of B')
	
	def area(self):
		print('im parent B area')
		super().area()

class C(A):
	def area(self):
		print('im parent C area')
		super().area()

	def volume(self):
		print('im volume of c')

class E(C, B):
	pass


# a = A()
# print(a.area())
# b = B()
# print(b.area())
# c = C()
# print(c.area())
e = E()
print(e.area())
print(e.perimeter())
print(e.volume())
