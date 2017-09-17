from PersonalCard import *
class EmployeeCard (PersonalCard) :
	'''This class extends Personal card with additional attributes.'''
	'''All other logic is implemented elsewhere'''
	def __init__(self) :
		# Call superclass to fill attributes
		super().__init__()		
		# Extend existing attributes with our new shiny attributes
		self.attributes.append( { "id": 4, "desc": "Job title", "value":"" } )
		self.title = "Employee Card"		
		pass