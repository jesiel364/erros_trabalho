from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

with open('registros.txt', 'r') as f:
	for texto in f:
		a = texto

class Main(BoxLayout):
	def __init__(self):
		super().__init__()
		self.box = BoxLayout()
		self.lb = Label(text=a)
		
		self.add_widget(self.lb)
		
	

class Mostrar(App):
	def build(self):
		return Main()
	
		
		
		
Mostrar().run()