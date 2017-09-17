from cl_personal_card import *
class EmployeeCard (PersonalCard) :
	'''(NULL)'''
	def __init__(self) :
		# Call superclass to fill attributes
		super().__init__()		
		# Extend existing attributes with our new shiny attributes
		self.attributes.append( { "id": 4, "desc": "Job title", "value":"" } )
		self.title = "Employee Card"		
		pass