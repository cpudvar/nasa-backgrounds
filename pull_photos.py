'''
Created by Caleb Pudvar

Downloads NASA's Photo of the Day and sets that photo as my desktop background.

Makes use of APOD api via api.nasa.gov

ec4yVEhGhkIalbKYxqY0rpkY7q113yEZfNNUdC29
'''
import requests
import shutil
import os
from datetime import date

def access_pic():
	p = {'hd': True}
	request = requests.get('https://api.nasa.gov/planetary/apod?api_key=ec4yVEhGhkIalbKYxqY0rpkY7q113yEZfNNUdC29', params=p)
	parsed = request.json()

	hd = parsed['hdurl']
	print(hd)
	print(request.url)
	return hd

def set_directory():
	file_path = 'C:\\Users\\Caleb\\Documents\\GitHub\\nasa-backgrounds\\photos\\'
	os.chdir(file_path)
	print(os.getcwd())

def save_img(img_url):
	response = requests.get(img_url, stream=True)
	with open((str(date.today())+'.jpg'), 'wb') as f:	
		shutil.copyfileobj(response.raw, f)

	del response

def set_bg():
	pass

def main():	

	img_url = access_pic()
	#img = img_url.split('/')
	#apod = (img[len(img)-1])
	#print(img_url)
	#apod = file_path+img_url
	set_directory()
	save_img(img_url)
	set_bg()

main()

