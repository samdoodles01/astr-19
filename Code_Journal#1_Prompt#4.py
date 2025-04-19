#Favorite Animal Class
class Cat:
	def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
		self.arm_length = arm_length #float in 
		self.leg_length = leg_length #float: in
		self.num_eyes = num_eyes #int 
		self.has_tail = has_tail #bool
		self.is_furry = is_furry #bool

	def describe(self):
		print("Cat Physical Characteristics:")
		print(f"- Arm Length: {self.arm_length} inches")
		print(f"- Leg Length: {self.leg_length} inches")
		print(f"- Number of Eyes: {self.num_eyes}")
		print(f"- Has a Tail: {'Yes' if self.has_tail else 'No'}")
		print(f"- Is Furry: {'Yes' if self.is_furry else 'No'}")

	def meow(self): 
		print("Meow")

#Cat Characteristics 
my_animal = Cat(arm_length=12.0, leg_length=15.0, num_eyes=2, has_tail=True, is_furry=True)

#Describe my Cat
my_animal.describe()

#Meow
my_animal.meow()
