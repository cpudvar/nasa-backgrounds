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
import ctypes

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 2
FILE_PATH = 'C:\\Users\\Caleb\\Documents\\GitHub\\nasa-backgrounds\\photos\\'

def access_pic():
	p = {'hd': True}
	request = requests.get('https://api.nasa.gov/planetary/apod?api_key=ec4yVEhGhkIalbKYxqY0rpkY7q113yEZfNNUdC29', params=p)
	parsed = request.json()
	hd = parsed['hdurl']

	return hd

def set_directory():
	os.chdir(FILE_PATH)
	print(os.getcwd())

def save_img(img_url):
	response = requests.get(img_url, stream=True)
	with open((str(date.today())+'.jpg'), 'wb') as f:	
		shutil.copyfileobj(response.raw, f)

	dir_loc=FILE_PATH+str(date.today())+'.jpg'
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, dir_loc, SPIF_UPDATEINIFILE)

def main():	
	img_url = access_pic()
	set_directory()
	save_img(img_url)
	

main()

