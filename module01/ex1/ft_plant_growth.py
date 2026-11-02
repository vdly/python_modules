class	Plant:
	def	__init__(self, name, height, age):
		self.name = name
		self.height = height
		self.age = age
	
	def	grow(self):
		self.height += 0.8

	def	aged(self):
		self.age += 1

	def	show(self):
		print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")

def		ft_plant_growth():
	print("=== Garden Plant Growth ===")

	rose = Plant("Rose", 25, 30)

	day = 1
	rose.show()
	for day in range(1, 8):
		print(f"=== Day {day} ===")
		rose.aged()
		rose.grow()
		rose.show()

	total_growth = round(0.8 * day, 1)
	print(f"Growth this week: {total_growth}cm")
		
ft_plant_growth()