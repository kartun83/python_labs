from cl_container import *
import codecs, sys, os

class App(UIFunc):	
	def __init__(self):
		super().__init__()
		self.project_title = u'Lab project 01'	
		# Container instance
		self.container = Container()

		# Description for quit method
		setattr(App.interface_quit,self.p_desc_field,"Exit application");	

		# Collect invokable methods from all inheritors of UIFunc
		self.functions = list()
		for classRef in self.inheritors(UIFunc):
			self.functions += classRef.get_functions(classRef)

		#Available functions, exported from container class
		#self.functions = self.container.get_functions() #
		#self.functions += self.get_functions()
		#print(self.functions)
		#self.functions.append(['1', u'Добавить элемент', self.container.add_element])
		#self.functions.append(['2', u'Вывести список', self.container.print_list])
		#self.functions.append(['3', u'Сохранить в файл',self.container.save_to_file])
		#self.functions.append(['4', u'Загрузить из файла',self.container.load_from_file])
		#self.functions.append(['5', u'Очистить список',self.container.clear_list])

		#Extend list with our own function for quit application
		#self.functions.append(['0', u'Выход',])
		
		pass

	#	Using klass, as "class" is a reserved keyword
	def inheritors(self,klass):
	    subclasses = set()
	    work = [klass]
	    while work:
	        parent = work.pop()
	        for child in parent.__subclasses__():
	            if child not in subclasses:
	                subclasses.add(child)
	                work.append(child)
	    return subclasses		

	def interface_quit(self):
		""" Function for leaving application """
		print("Leaveing application. BYE !")
		exit()
		pass

	def printFunctions(self, functionsList):		
		# List in functionsList : [ 0 = Class reference, 1 = method reference, 2 = Method description ]
		for idx, function in enumerate(functionsList): print('{0}. {1}'.format(idx+1,function[2]))
		pass		

	
	def cls(self):
		# Wait for user action		
		input("Press enter to continue...")
		os.system('cls' if os.name=='nt' else 'clear')			
	

	def mainLoop(self):
		command = None
		while True:			
			print(self.project_title)
			self.printFunctions(self.functions)						
			try:
				command = int(input(u'Command: '))	
				# Validate user input
				#if command > 0 and command <= len(self.functions):
				# Range doesn't include last element
				if command in range(1, len(self.functions) + 1):					
					# Call selected function
					self.functions[command-1][1](self.container)
					# Clear screen from previous functions					
				else:					
					print("Incorrect command selected")	
					pass							
				self.cls()	
			except ValueError as e:
				print('Please enter a number')
				pass
		pass

				
			

def main() :
	# Name of the project
	#app = App()
	#app.mainLoop()
	App().mainLoop()

main()	