class New_Customer_Details:
	
	def __init__(self):
		Customer_count=0
		Customer_count = Customer_count+1
		
	def Details_Cust_New():
		Name = raw_input("Enter New Customer Name:")
		DOB = raw_input("Enter DOB of Customer(dd/mm/yyyy):")
		Phone_number = raw_input("Enter phone number:")
		Email_id = raw_input("Enter mail ID:")
		Address = raw_input("Enter Cust Address:")
		return Name,DOB,Phone_number,Email_id,Address
	
def Cust_Details():
	New_Customer_Details.Details_Cust_New()
	print "Customer Name:",Name
	print "Date of Birth:",DOB
	print "Phone Numebr",Phone_number
	print "Email ID:",Email_id
	print "Address of Cust:",Address
	
	
class Savings_Account:

	def __init__(self):
		self.balance=0

	def deposit(self,amount):
		self.balance= self.balance+amount
		print "Deposited amount:", amount
		
	def draw(self,amount):
		print "Moeny Withdrawn:", amount
		self.balance = self.balance-amount
		
	def balance_show(self):
		print "Customer balance: %s" %(self.balance)
		
def Savings_Account_details():
	Savings_Account()
	print "Deposited amount:",deposit.amount()
	print "Money Withdrawn:",draw.amount()
	print "Closing Balance:",balance


class CreditCrad_Account:
	
	def __init__(self):
		self.Credit_limit = input("Enter Credit Limit:")
		
	def deposit(self,damount):
		self.Credit_limit = Credit_limit+damount
			
	def transaction(self,tamount):
		self.Credit_limit = Credit_limit-tamount
	
def CreditCard_Account_details():
	CreditCrad_Account_Account()
	print "Deposited amount:",damount
	print "Transaction:",tamount
	print "Closing Balance:",Credit_limit


	
New_Cust = New_Customer_Details()
New_Cust.Details_Cust_New('selena','12/12/2006','9696969696','selena@gmail.com','Hyd')

	