class Car:
	#variant = 0
	def geartype(self,a):
		#self.a=a
		self.a=a 
		if (a==1):
			print ("geartype is automatic")
		else:
			print ("geartype is manual")
	def color(self,b):
		self.b=b
		#b = self.variant 
		if (b==1):
			print ("color is black")
		else:
			print ("color is white")
	def nightvision(self,c):
		self.c=c
		#c = self.variant 
		if (c==1):
			print ("yes")
		else:
			print ("no")
class Bikes(Car):
	def wheels(self):
		#self.d=d
		print("two wheeler")
			
audi=Car()
bmw=Car()
Honda=Bikes()
audi.geartype(1)
audi.color(1)
audi.nightvision(1)
bmw.geartype(2)
Honda.geartype(1)
Honda.wheels()
