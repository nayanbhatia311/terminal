import os
import webbrowser as wb
from PIL import Image


def cwd():
	print(os.getcwd()) 

def browser(link="https://www.google.com"):
	wb.open(link)

def search(query):
	string=""
        
	for i in query:
		string=string+" "+i
	link="https://www.google.co.in/search?q="+string
	wb.open(link)

def image(image):
