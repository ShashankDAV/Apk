from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import FadeTransition
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.scrollview import MDScrollView
import fb
import json
from kivymd.toast import toast

code = '''
<DrawerClickableItem@MDNavigationDrawerItem>
<Content>
	adaptive_height: True

MDNavigationLayout:
	ScreenManager:
		id : manager

		MDScreen:
			name : 'home'
			FitImage:
				source : "bg.png"
			MDIconButton:
				icon : "menu"
				on_release : app.root.ids.drawer.set_state("open")
				pos_hint : {"center_x" : 0.1 , "center_y" : 0.95}
			Image:
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.75}
				size_hint : (0.9 , 0.45)
				source : "img.png"
			MDBoxLayout:
				orientation : "vertical"
				padding : "4dp"
				md_bg_color : 1,1,1,1
				size_hint : 0.94 , 0.5
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.3}
				radius : [20]
				MDLabel:
					text : "Updates"
					bold : True
					pos_hint : {"center_x" : 0.85 , "center_y" : 0.95}
					font_size : "30dp"
					underline : True
				MDBoxLayout:
					MDLabel:
						id : update1
						text : "No Internet"
						font_size : "17dp"
						halign: "left"
				MDBoxLayout:
					MDLabel:
						id : update2
						text : "No Internet"
						font_size : "17dp"
						halign: 'left'
				MDBoxLayout:
					MDLabel:
						id : update3
						text : "No Internet"
						font_size : "17dp"
						halign: 'left'
		
		MDScreen:
			name : 'player_stats'
			FitImage:
				source : "bg.png"
			MDIconButton:
				icon : "menu"
				on_release : app.root.ids.drawer.set_state("open")
				pos_hint : {"center_x" : 0.1 , "center_y" : 0.95}
			MDTextField:
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.865}
				mode : "rectangle"
				hint_text : "Enter player name."
				size_hint : (0.9 , 0.09)
				on_text_validate: app.show_player_stats(self.text)
			MDBoxLayout:
				id : player_stat
				orientation: "vertical"
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.4}
				size_hint : (0.9 , 0.7)
				MDLabel:
					id : player_bat
					bold : True
					pos_hint : {"center_x" : 0.85 , "center_y" : 0.95}
					font_size : "30dp"
					text : ""
				MDLabel:
					id : bat_stat
					text : ""
				MDLabel:
					id : player_bowl
					bold : True
					pos_hint : {"center_x" : 0.845 , "center_y" : 0.65}
					font_size : "30dp"
					text : ""
				MDLabel:
					id : bowl_stat
					text : ""
				MDLabel:
					id : player_cap
					bold : True
					pos_hint : {"center_x" : 0.8, "center_y" : 0.35}
					font_size : "30dp"
					text : ""
				MDLabel:
					id : cap_stat
					text : ""
				
		MDScreen:
			name : 'tour_stats'
			FitImage:
				source : "bg.png"
			MDIconButton:
				icon : "menu"
				on_release : app.root.ids.drawer.set_state("open")
				pos_hint : {"center_x" : 0.1 , "center_y" : 0.95}
	
		MDScreen:
			name : "rankings"
			FitImage:
				source : "bg.png"
			MDIconButton:
				icon : "menu"
				on_release : app.root.ids.drawer.set_state("open")
				pos_hint : {"center_x" : 0.1 , "center_y" : 0.95}
			MDScrollView:
				size_hint : (0.9 , 0.85)
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.475}
				MDBoxLayout:
					id : ranks_layout
					orientation: 'vertical'
					size_hint : (1,1)
					pos_hint : {"center_x" : 0.5 , "center_y" : 0.5}
					spacing : "15dp"
					
		MDScreen:
			name : "edit"
			FitImage:
				source : "bg.png"
			MDIconButton:
				icon : "menu"
				on_release : app.root.ids.drawer.set_state("open")
				pos_hint : {"center_x" : 0.1 , "center_y" : 0.95}
			MDTextField:
				id : edit_path
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.865}
				mode : "rectangle"
				hint_text : "Enter path."
				size_hint : (0.9 , 0.09)
			MDTextField:
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.665}
				mode : "rectangle"
				text : "Sample Data : {'stats' : [[runs , innings , not outs , hs , avg , 50s , 100s , 150s] , [wickets , 3ws] , [in_played , in_won , in_lost , win%]]}"
				readonly : True
				multiline : True
				size_hint : (0.9 , 0.27)
			MDTextField:
				id : edit_data
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.465}
				mode : "rectangle"
				hint_text : "Enter data."
				size_hint : (0.9 , 0.09)
			MDTextField:
				id : edit_pass
				pos_hint : {"center_x" : 0.5 , "center_y" : 0.365}
				mode : "rectangle"
				hint_text : "Enter password."
				size_hint : (0.9 , 0.09)
			MDRaisedButton:
				pos_hint : {"center_x" : 0.35 , "center_y" : 0.265}
				text : "Post Data"
				on_release : app.edit_data()
			MDRaisedButton:
				pos_hint : {"center_x" : 0.65 , "center_y" : 0.265}
				text : "Get Data"
				on_release : app.get_data()
		
	MDNavigationDrawer:
		id : drawer
		MDNavigationDrawerMenu:
			MDNavigationDrawerHeader:
				source : 'icon.png'
				title : 'CricStats'
				spacing : '20dp'
				padding : '20dp',0,0,'5dp'

			MDNavigationDrawerDivider:
			DrawerClickableItem:
				id : home
				text : 'Home'
				icon : 'home'
				on_release : app.change_sc('home')
			DrawerClickableItem:
				id : rankings
				text : 'Rankings'
				icon : 'format-list-numbered'
				on_release : app.load_rankings()
			DrawerClickableItem:
				id : player_stats
				text : 'Player Stats'
				icon : 'account'
				on_release : app.change_sc('player_stats')
			
			MDNavigationDrawerDivider:
			DrawerClickableItem:
				id : edit
				text : 'Edit Stats'
				icon : 'circle-edit-outline'
				on_release : app.change_sc('edit')
'''

class MyApp(MDApp):
	def on_start(self):
		self.root.ids.manager.transition = FadeTransition(clearcolor = [1,1,1,1])
		self.updates()
	
	def build(self):
		self.theme_cls.primary_palette = "Gray"
		self.theme_cls.primary_hue = "900"
		self.db = fb.Firebase('https://website-shashankdav-default-rtdb.firebaseio.com/' , '')
		self.first_time = True
		return Builder.load_string(code)
	
	def change_sc(self , name):
		self.root.ids.manager.current = name
	
	def updates(self):
		try:
			data = self.db.get_data(path = "updates")
			self.root.ids.update1.text = data["update1"]
			self.root.ids.update2.text = data["update2"]
			self.root.ids.update3.text = data["update3"]
		except:
			pass
	
	def show_player_stats(self , name):
		try:
			player_data = self.db.get_data(path = name.lower())["stats"]
			bat = player_data[0]
			bowl = player_data[1]
			cap = player_data[2]
			self.root.ids.player_bat.text = "Batting"
			self.root.ids.player_bowl.text="Bowling"
			self.root.ids.player_cap.text = "Captaincy"
			avg = bat[0] / (bat[1] - bat[2])
			if not cap[0] == 0:
				win = str(int(cap[1]/cap[0]*100)) + "%"
			else:
				win = "N/A"
			bat_text = f'Runs : {bat[0]}    Innings : {bat[1]}    NOs : {bat[2]}    Avg : {int(avg)}\nHS : {bat[3]}      50s : {bat[4]}            100s : {bat[5]}   150s : {bat[6]}'
			bowl_text = f'Wickets : {bowl[0]}                          3-wicket hauls : {bowl[1]}'
			cap_text = f"Innings : {cap[0]}    Win : {cap[1]}    Loss : {cap[2]}    Win% : {win}"
		except:
			bat_text = ""
			bowl_text = ""
			cap_text = ""
			self.root.ids.player_bat.text = ""
			self.root.ids.player_cap.text = ""
			self.root.ids.player_bowl.text = "Error"
		self.root.ids.bat_stat.text = bat_text
		self.root.ids.bowl_stat.text = bowl_text
		self.root.ids.cap_stat.text = cap_text
	
	def load_rankings(self):
		if self.first_time:
			try:
				ranks = ["bat","bowl","all-round"]
				for rank in ranks:
					data = self.db.get_data(path = f"rankings/{rank}")["data"]
					row_data = sorted(data , key=lambda x: x[1], reverse=True)
					if rank=="all-round":
						heading = "All-round"
					else:
						heading= rank.capitalize() + "ing"
					datatable = MDDataTable(
					elevation = 0,
					size_hint=(1 , 0.8),
					column_data=[
						("No.", dp(15)),
						("Name", dp(18)),
						(f"{heading} Rating", dp(24))
					],
					row_data=[(str(i+1), player[0], str(player[1])) for i, player in enumerate(row_data)],
					rows_num = len(row_data)
					)
					self.root.ids.ranks_layout.add_widget(datatable)
				self.change_sc("rankings")
				self.first_time = False
			except:
				pass
		else:
			self.change_sc("rankings")
			return
	
	def edit_data(self):
		path = self.root.ids.edit_path.text
		data = json.loads(self.root.ids.edit_data.text)
		pass_ = self.root.ids.edit_pass.text
		if path:
			if pass_ == "1605":
				self.db.post_data(data=data , path = path)
				self.root.ids.edit_path.text = ""
				self.root.ids.edit_data.text = ""
				self.root.ids.edit_pass.text = ""
				toast("Data Posted Successfully ")
		else:
			toast("Wrong Password")
	
	def get_data(self):
		path = self.root.ids.edit_path.text
		pass_ = self.root.ids.edit_pass.text
		if path:
			if pass_ == "1605":
				d = str(self.db.get_data(path = path))
				self.root.ids.edit_path.text = ""
				self.root.ids.edit_data.text = d.replace("'" , '''"''')
				self.root.ids.edit_pass.text = ""
		else:
			toast("Wrong Password")

MyApp().run()