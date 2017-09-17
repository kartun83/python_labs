from EmployeeCard import *
from types import FunctionType
from UIFunc import UIFunc
import pickle

class Container(UIFunc) :
	'''This is a container class. Nothing to add'''

	## Default filename for file operations
	filename = 'data.pickle'
	def __init__(self) :
		super().__init__()
		## Actual data storage
		self.p_storage = [] # container[*cl_employee_card]				
		# Add description for interface methods. Attrubutes attached to
		# class methods, not to the instance
		setattr(Container.interface_add_element,self.p_desc_field,"Add element");
		setattr(Container.interface_print_list,self.p_desc_field,"Print list");
		setattr(Container.interface_save_to_file,self.p_desc_field,"Save to file");
		setattr(Container.interface_load_from_file,self.p_desc_field,"Load from file");
		setattr(Container.interface_clear_list,self.p_desc_field,"Clear list");
		pass

	def interface_add_element (self) :	
		''' Requests data for attributes from stdin. In real life it would be 	
		 	much more convinient to break up attribute setting and data request 
			either via method reference or other techniques '''
		print("Adding new element")		
		## Here we could also invoke inheritors like it's done in App
		# to build complete list of all available classes and provide
		# greater flexibility. Also it allow to avoid code changes
		# when new classes are added
		create_instance = lambda i: PersonalCard() if int(i) == 1 else EmployeeCard()
		new_item = create_instance(input("1 for PersonalCard, others for EmployeeCard:"))
		#new_item = EmployeeCard()
		new_item.request_data()
		self.p_storage.append( { id: len(self.p_storage), "obj": new_item })
		# returns 
		pass

	def interface_print_list (self) :		
		'''Output list contents to SDTOUT'''
		print("List of available cards")
		for obj in self.p_storage:
			obj["obj"].print_data()
			pass
		# returns 
		pass

	def interface_save_to_file (self) :		
		'''Data is saved into fixed location: defined in filename attribute'''
		print("Saving data")
		with open(self.filename, 'wb') as f:
			pickle.dump(self.p_storage, f)
		# returns bool
		pass

	def interface_load_from_file (self) :		
		'''Data is loaded from fixed location: defined in filename attribute'''
		print("Loading from file")
		with open(self.filename, 'rb') as f:
			self.p_storage = pickle.load(f)		
		# returns bool
		pass	

	def interface_clear_list (self) :		
		'''Clear list'''
		print("Clearing list")
		del self.p_storage[:]
		# returns 
		pass