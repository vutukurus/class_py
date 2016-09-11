#Oops-2
class Bank:

	def __init__(self):
		self.balance=0

	def deposit(self,amount):
		self.balance= self.balance+amount
		a=10+10
		print "vaue of a is", a
		print "deposited amount", amount
		
	def draw(self,amount):
		print "moeny withdranw", amount
		self.balance = self.balance-amount #900
		
	def balance_show(self):
		print "your balance %s" %(self.balance)
		
#obeject
user1=Bank()
user1.deposit(1000)

#second object..
user2=Bank()
user2.deposit(2000)

user1.balance_show()
user2.balance_show()

user1.draw(100)
user1.balance_show()
user2.balance_show()







