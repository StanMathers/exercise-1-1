from player import *

class Process:
	def __init__(self):
		self.player = Player()

	def display_information(self):
		print(f'Tema: {self.player.topic_name}')
		print(f'Word is {len(self.player.obj_name)} letters long.')
		print(self.player.display_shape())

	def __start_main_game(self):
		prompt = input('Guess a letter: ')
		if self.player.is_alive():
			self.player.update_shape(prompt)
		else:
			print('You lost')
			self.__ask_for_continue()
	
	def __ask_for_continue(self):
		user_input = input('Press any key to continue, x to exit: ').lower()
		if user_input == 'x':
			quit()
		else:
			main()

	def play(self):
		if self.player.is_winner() == False:
			self.__start_main_game()
		else:
			print('You win!')
			self.__ask_for_continue()
def main():		
	p = Process()
	p.display_information()
	while True:
		p.play()
main()


