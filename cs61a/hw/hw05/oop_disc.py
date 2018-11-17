class foo:

	x = 5
	def __init__(self,x):
		self.x = x
	def bar(self):
		return self.x + 1

class foo2(foo):
	x = 7

	# no init so jump/inherit from foo
	def bar(self):
		return self.x + 2
	def bark():
		print('woof')


f = foo2(6) #calls foo init
f.bark() #Error
foo2.bark() #woof
foo.bark() #Error
f.bar() # 8
foo.bar(f) #7
#foo.bar refers to function bar in class foo, f

#lookup from instance -> class -> superclass -> error