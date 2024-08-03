from kivymd.app import MDApp
from kivy.lang import Builder

code = '''
MDLabel:
	text : "Hello!"
'''

class MyApp(MDApp):	
	def build(self):
		return Builder.load_string(code)


MyApp().run()