class PersonalCard :
	'''(NULL)'''
	# Class attributes to minimize typo errors
	p_desc_field = "desc"
	p_val_field  = "value"

	def __init__(self) :
		self.attributes = []
		self.attributes.append( { "id": 1, self.p_desc_field: "First Name", self.p_val_field:"" } )
		self.attributes.append( { "id": 2, self.p_desc_field: 'Last Name', self.p_val_field:"" } )
		self.attributes.append( { "id": 3, self.p_desc_field: 'Birth date', self.p_val_field:"" } )
		self.title = "PersonalCard"
		pass

	def request_data(self) :		
		for attribute in self.attributes:
			attribute[self.p_val_field] = input("{0}: \t".format(attribute[self.p_desc_field]))
			pass
		pass

	def print_data(self) :
		print(self.title)
		for attribute in self.attributes:
			print('{}: {}'.format(attribute[self.p_desc_field], attribute[self.p_val_field]))
			pass	