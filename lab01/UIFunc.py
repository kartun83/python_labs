import inspect

class UIFunc:
	# This is the Class attribute. Available from class reference
	# while self.blabla is reachable only from method reference or
	# class instance
	p_desc_field = "description"		
	def __init__(self):
		# Name for field where we would store description for the method
		pass

	def get_functions(self) :	
		# Build functions list available from outside
		
		# Lambdas for making longstory short
		is_function = lambda func: True if callable(func[1]) and func[0].startswith("interface_") else False
		description = lambda func: getattr(func[1], self.p_desc_field)

		result = []		
		for func in inspect.getmembers(self):
			if is_function(func): 
				result += [[self, func[1], description(func)]]
				pass	
			pass
		return result