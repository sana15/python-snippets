################count files in a folder #############
import os #########os module
pathOfFolder = /Desktop/
# count = 0
def CountFiles(path):
	count = 0
	for file in os.listdir(path):
		count = count+1
	print(count)


##files of .mp4

def VideoCountFiles(path):
	count = 0
	for file in os.listdir(path):
		if file.endswith(".mp4"):
			count = count+1
	print(count)
def VideoCountFiles(path):
	count = 0
	for file in os.listdir(path):
		if file.endswith(".xml"):
			count = count+1
	print(count)
