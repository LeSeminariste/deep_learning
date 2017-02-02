import PIL
from PIL import Image
import os

inputfolder = "/home/ph/IA/deep_learning/classe1_org/"
outputfolder = "/home/ph/IA/deep_learning/classe1/"

for path, dirs, files in os.walk(inputfolder):
	for filename in files :
		print(filename)
		img = Image.open(inputfolder+filename)
		img = img.convert('L')
		img = img.resize((64,64), PIL.Image.ANTIALIAS)
		name = outputfolder + filename
		img.save(name)
