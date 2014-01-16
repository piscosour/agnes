
class Person:
	
	def __init__(self, name, description):
		self.name = name
		self.description = description


people = [

	Person(name='sam',
	       description='Mission commander.'),

	Person(name='alex',
		   description='Lead pilot'),

	Person(name='gordon',
		   description='Auxiliary pilot and Agnes on board maintenance engineer. Previously research scientist at Black Mesa Lambda compound, involved in the incident. Selected for this mission because of his acquaintance with extraterrestrial life forms.'),

	Person(name='gladys',
		   description='Operations officer. Previously support officer in the Aperture Science main research and testing facility, in charge of human subject testing and facilities management.'),

	Person(name='dave',
		   description='Lead on board research scientist. Machine hater. Future star child.'),

	Person(name='jim',
		   description='Lead designer and product manager in the Dunder Mifflin Paper and Aerospace Company, assigned to project Agnes. Previously worked at the Scranton research and development laboratory. Responsible for the design, development and implementation of Agnes prior to mission launch.')

]