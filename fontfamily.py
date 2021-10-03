# importing button widget from kivy framework
from kivy.uix.button import Button
from kivy.app import App

# importing labelbase which which
# register our custom font for application
from kivy.core.text import LabelBase
from kivy.lang import Builder


# this is the main class which will
# render the whole application
class uiApp(App):

	# method which will render our application
	def build(self):
		return Builder.load_string("""

# adding our button
Button:

	# text which will appear on first button
	text:"first button"

	# specifying the fontstyle name that we
	# have registered in main.py file
	font_name:"Lemonada"
	font_size:65
								""")


# registering our new custom fontstyle
LabelBase.register(name='Lemonada',
fn_regular="a.ttf")

# running the application
uiApp().run()
