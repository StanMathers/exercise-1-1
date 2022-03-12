import random
import re

class Bank:
	colours = ['red','blue']
	animals = ['dog','cat']
	topic_names = ['Colours','Animals']
	topics = {'Colours':colours,'Animals':animals}

	def topic_name(self):
		choice = random.choice(self.topic_names)
		return choice

	def get_object_from_list(self, func):
		obj_choice = random.choice(self.topics[func])
		return obj_choice

	def validate_letters(self, func, letter: str):
		match = re.search(func, letter)
		return match.start() if match else None
