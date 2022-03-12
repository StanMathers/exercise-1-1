from bank import *

class Player:
	def __init__(self, health: int = 10):
		self.health = health

		self.bank = Bank()
		self.topic_name = self.bank.topic_name()
		self.obj_name = self.bank.get_object_from_list(self.topic_name)
		
        # Shape
		self.__shape = ['_' for i in range(len(self.obj_name))]

	@property
	def is_valid_letter(self):
		return self.bank.validate_letters(self.user_prompt, self.obj_name)

	def get_shape(self): # For displaying shape (Debugging)
		print(self.__shape)

	def update_shape(self, user_prompt: str):
		self.user_prompt = user_prompt # Defining global variable for flexibility
		if (self.is_valid_letter != None and len(self.user_prompt) == 1): # Updating an entire shape
			self.__shape.pop(self.is_valid_letter)
			self.__shape.insert(self.is_valid_letter, self.user_prompt)
			print('\nNice!')
			print(self.__shape)
		else:
			if len(self.user_prompt) > 1:
				print('Please guess a single alphabet')
				self.__descrease()
			else:
				self.__descrease()
				print(self.__shape)
   
	def __descrease(self):
			print('\nNope!')
			self.health -= 1
			print(f'Lives remaining: {self.health}')

	def display_shape(self): # For displaying shape
		return self.__shape

	def is_winner(self): # Checks if player has won
		return True if '_' not in self.__shape else False

	def is_alive(self): # Checks if player is still alive
		return True if self.health != 1 else False


