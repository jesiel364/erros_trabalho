from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.slider import Slider

class Ger_tela(ScreenManager):
	pass
	
class Menu(Screen):
	pass

class Tela_inserir(Screen):
	pass
	
class Tela_ver_relatorios(Screen):
	pass


class MeuApp(App):
	def build(self):
		Window.clearcolor = (89/255, 121/255, 212/255, 1)
		return Builder.load_string('''
Ger_tela:
	Menu:
	Tela_inserir:
	Tela_ver_relatorios:

				
<Menu>:
	name: 'menu'
	
	BoxLayout:
		canvas:
			Color:
				rgba: (151/255, 20/255, 34/255, 0)
			Rectangle:
				size: self.size
				pos: self.pos
				source: 'img.png'

		size: root.width, root.height 
		orientation: 'vertical'
		spacing: 20
		padding: 40
		
		Button:
			font_size: '42sp'
			size: 200,200
			background_normal: 'History.png'
    		background: 'History.png'
			background_color: 0.88, 0.88, 0.88, 1  
    		size_hint: None, None
    		pos_hint: {'center_x': .5, 'center_y': .5}
    
		Button:
			font_size: '40sp'
			text: 'Inserir'
			size_hint: 0.5, None
			pos_hint: {'center_x': 0.5, 'center_y': .8}
			on_release: app.root.current = 'inserir'
			background_color: (255/255,0/255,0/255,1)
		
		Button:
			font_size: '42sp'
			text: 'Ver Relatórios'
			on_release: app.root.current = 'relatorios'
			size_hint: 0.5, None
			pos_hint: {'center_x': 0.5, 'center_y': .5}
			background_color: (255/255,0/255,0/255,1)

		Button: 
			text: 'Sair'
			font_size: '42sp'
			size_hint: .5, None
			pos_hint: {'center_x': 0.5, 'center_y': .2}
			on_release: quit()
			background_color: (255/255,0/255,0/255,1)

<Tela_inserir>:
	name: 'inserir'
	FloatLayout:
		size: root.size
		padding: 30
		ProgressBar:
			pos_hint: {'center_y': .9}
			max: 100
			value: 90

		Label:
			text: 'Inserir Dados: '
			font_size: '50sp'
			pos_hint: {'center_y': .95}
		
		#	Entradas
		Label:
			text: 'Erros:'
			font_size: '20sp'
			pos_hint: {'center_y': .8, 'center_x': .3}

		TextInput:
			id: erros
			hint_text: '01'
			#border: (4, 4, 4, 4)
			font_size: '40sp'
			pos_hint: {'center_y': .8, 'center_x': .5}
			size_hint: .2, .1
			text_validate_unfocus: True
			write_tab: True

		Label:
			text: 'Reposições:'
			font_size: '20sp'
			pos_hint: {'center_y': .6, 'center_x': .3}

		TextInput:
			id: repo
			hint_text: '01'
			border: (4, 4, 4, 4)
			font_size: '40sp'
			pos_hint: {'center_y': .6, 'center_x': .5}
			size_hint: .2, .1
			text_validate_unfocus: True
			write_tab: True

		Label:
			text: 'Data:'
			font_size: '20sp'
			pos_hint: {'center_y': .4, 'center_x': .3}

		TextInput:
			id: data
			hint_text: '02/04/2021'
			border: (4, 4, 4, 4)
			font_size: '40sp'
			pos_hint: {'center_y': .4, 'center_x': .5}
			size_hint: .3, .1
			text_validate_unfocus: True
			write_tab: True

		Button:
			on_release: self.app.salvar()
			text: 'Salvar'
			font_size: 50
			id: btsalvar
			size_hint: .2,.2
			pos_hint: {'center_y': .15, 'center_x': .85}
			background_color: (166/255, 138/255, 199/255, 1)

		
		Button:
			pos_hint: {'center_y': .15, 'center_x': .1}
			background_down: 'b2press.png'
			background_normal: 'b2.png'
			background_color: 0.88, 0.88, 0.88, 1
			size_hint: None, None
			size: 150,150
			on_release: app.root.current = 'menu'


<Tela_ver_relatorios>:
	name: 'relatorios'
	
	FloatLayout:
		#size_hint: .10,.10
		#pos_hint: {'top': .95, 'right': .95}

		spacing:80
		padding: 50
		#canvas:
		#	Color:
		##		pos: self.pos
		#		size: self.size


		FloatLayout:
			size_hint: .8,.8
			pos_hint: {'top': .90, 'right': .90}
			canvas:
				Color:
					rgba: (159/255, 197/255, 211/255, 1)
				Rectangle:
					pos: self.pos
					size: self.size

			FloatLayout:
				font_size: '60sp'
				Button:
					pos_hint: {'center_y': .1, 'center_x': .15}
					background_down: 'b2press.png'
					background_normal: 'b2.png'
					background_color: 0.88, 0.88, 0.88, 1
					size_hint: None, None
					size: 150,150
					on_release: app.root.current = 'menu'
				
				Label:
					text: 'Lorem ipsum dolor sit amet.'
					pos_hint: {'x': .1, 'y': .1}
				Label:
					text: 'Lorem ipsum dolor sit amet.'
					pos_hint: {'x': .1, 'y': .15}
				Label:
					text: 'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
					pos_hint: {'x': .1, 'y': .2}

		Label:
			text: 'Registros'
			font_size: '49sp'
			pos_hint: {'center_x': .5, 'center_y': .95}
			color: (49/255, 50/255, 62/255,1)

		
		''')
	def salvar():
		print('deu certo')
		
MeuApp().run()