################count files in a folder #############
import os #########os module
pathOfFolder = /Desktop/
# count = 0
def CountFiles(path):
	count = 0
	for file in os.listdir(path):
		count = count+1
	print(count)
