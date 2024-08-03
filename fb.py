import requests
class Firebase:
	def __init__(self , url , auth):
		self.url = url
		self.auth = auth
	
	def post_data(self , data=None , path = "default/one"):
		url = f'{self.url}/{path}.json?auth={self.auth}'
		response = requests.put(url, json = data)
		if response.ok:
			res = 'Data posted successfully'
		else:
			res = f'Error posting data: {response.text}'
		return res
	
	def get_data(self , path = "default/one"):
		url = f'{self.url}/{path}.json?auth={self.auth}'
		response = requests.get(url)
		if response.ok:
			data = response.json()
		else:
			data = f'Error getting data: {response.text}'
		return data
	
	def delete_data(self , path = "default/one"):
		url = f'{self.url}/{path}.json?auth={self.auth}'
		response = requests.delete(url)
		if response.ok:
			res = 'Data deleted successfuly'
		else:
			res = f'Error deleting data: {response.text}'
		return res
	
	def post_image(self, path="default/one", type="png" , img_path = ""):
		url = f'{self.url}/{path}.json?auth={self.auth}'
		headers = {'Content-Type': f'image/{type}'}
		file = open(img_path , "rb")
		image_data = file.read()
		file.close()
		response = requests.put(url, headers=headers, data=image_data)
		if response.ok:
			res = 'Image posted successfully'
		else:
			res = f'Error posting image: {response.text}'
		return res